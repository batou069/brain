# Automating mail grab

### \#\# Part 1: Google API Setup (One-Time Task)

This is the most tedious part, but you only have to do it once. We need to create "credentials" so our script can log in to Gmail on your behalf without storing your password.

1.  **Go to the Google Cloud Console:** [https://console.cloud.google.com/](https://console.cloud.google.com/)
2.  **Create a New Project:**
      * Click the project selector at the top of the page and then click "**NEW PROJECT**".
      * Give it a name like "Obsidian Email Parser" and click "**CREATE**".
3.  **Enable the Gmail API:**
      * Make sure your new project is selected.
      * In the search bar at the top, search for "**Gmail API**" and select it.
      * Click the "**ENABLE**" button.
4.  **Create Credentials:**
      * Once enabled, click the "**CREATE CREDENTIALS**" button on the top right.
      * For "Credential Type", select "**User data**" and click **Next**.
      * For "App name", enter "Obsidian Parser".
      * For "User support email", choose your email address.
      * Leave "App logo" blank. Under "Developer contact information", enter your email again and click "**SAVE AND CONTINUE**".
      * On the "Scopes" screen, click "**ADD OR REMOVE SCOPES**". In the filter, type "**Gmail**", find `.../auth/gmail.readonly` and check the box next to it. Click "**UPDATE**". Then click "**SAVE AND CONTINUE**".
      * For "OAuth Client ID", select "**Desktop app**" from the dropdown. Give it a name if you wish. Click "**CREATE**".
5.  **Download the Credentials File:**
      * You'll see a confirmation screen. Click the "**DOWNLOAD**" button to download your credentials file.
      * **Rename this file to `credentials.json`**. This is very important.
      * Create a new folder on your computer for this project (e.g., `gmail_parser`) and place the `credentials.json` file inside it.

-----

### \#\# Part 2: Python Environment Setup

Now, we need to install the Python libraries that will communicate with Google and parse the email HTML.

1.  Open your terminal or command prompt.
2.  Install the libraries by running this command:

<!-- end list -->

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib beautifulsoup4
```

-----

### \#\# Part 3: The Python Script

Here is the complete script. Save this file as `process_alerts.py` inside the same folder where you put your `credentials.json` file.

**Action Required:** You must change the `OBSIDIAN_VAULT_PATH` variable in the script to the full path of your Obsidian vault folder.

````python
import os
import base64
import re
from pathlib import Path
from datetime import datetime

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- CONFIGURATION ---
# 1. SET THIS TO THE FULL PATH OF YOUR OBSIDIAN VAULT
OBSIDIAN_VAULT_PATH = "/path/to/your/obsidian/vault/folder" 
# Example for Windows: "C:/Users/YourUser/Documents/ObsidianVault"
# Example for Mac/Linux: "/Users/YourUser/Documents/ObsidianVault"

# 2. (Optional) Change the subfolder and note title format
OUTPUT_SUBFOLDER = "Daily Alerts" # A subfolder within your vault
NOTE_TITLE_FORMAT = "%Y-%m-%d Swing Alerts" # YYYY-MM-DD Swing Alerts.md

# --- GMAIL API SETTINGS ---
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']
TARGET_SENDER = "support@clickcapital.io"
TARGET_SUBJECT = "Swing Trade Alerts for"
# --- END CONFIGURATION ---


def authenticate_gmail():
    """Handles the OAuth 2.0 flow to get valid credentials."""
    creds = None
    token_path = Path('token.json')
    creds_path = Path('credentials.json')

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            
    return build('gmail', 'v1', credentials=creds)

def parse_email_content(html_body):
    """Parses the HTML of the email to extract alert information."""
    soup = BeautifulSoup(html_body, 'html.parser')
    alerts = {}
    
    # Find all table cells that act as headers for the alert sections
    headers = soup.find_all('td', string=re.compile(r'(Entry|Adjustment|Cancellation|Exit) Alerts'))
    
    for header in headers:
        header_text = header.get_text(strip=True)
        # Navigate up to the parent table containing this header and its content
        alert_box_table = header.find_parent('table')
        if not alert_box_table:
            continue
            
        # Find the specific content cell within this box
        content_cell = alert_box_table.find('td', id=re.compile(r'bodyText-'))
        if content_cell:
            # Get text, using newlines for <br> tags, and clean it up
            lines = content_cell.get_text(separator='\n', strip=True).splitlines()
            # Filter out empty lines
            clean_lines = [line.strip() for line in lines if line.strip()]
            alerts[header_text] = clean_lines
            
    return alerts

def format_alerts_for_obsidian(alerts, email_date):
    """Formats the extracted alerts into a Markdown string for Obsidian."""
    
    # Use the email's subject date for the note header
    date_str = email_date.strftime('%B %d, %Y')
    
    output = [f"# Swing Alerts for {date_str}\n"]
    
    alert_order = ["Entry Alerts", "Adjustment Alerts", "Cancellation Alerts", "Exit Alerts"]
    
    for alert_type in alert_order:
        output.append(f"## {alert_type}")
        content = alerts.get(alert_type)
        if content:
            # If "None today" is present, just write that.
            if any("none today" in line.lower() for line in content):
                output.append("None Today")
            else:
                # Format other content into a code block
                output.append("```")
                output.extend(content)
                output.append("```")
        else:
            output.append("Not found in email.")
        output.append("") # Add a blank line for spacing
        
    return "\n".join(output)

def main():
    """Main function to run the email fetching and processing."""
    print("Authenticating with Gmail...")
    service = authenticate_gmail()
    
    # Build search query
    query = f"from:({TARGET_SENDER}) subject:('{TARGET_SUBJECT}') is:unread"
    
    try:
        print(f"Searching for unread emails with query: {query}")
        response = service.users().messages().list(userId='me', q=query).execute()
        messages = response.get('messages', [])

        if not messages:
            print("No new emails found. Exiting.")
            return

        # Process the most recent unread email
        msg_id = messages[0]['id']
        print(f"Found email with ID: {msg_id}. Fetching content...")
        
        message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        
        # Get date from email headers for the title
        headers = message['payload']['headers']
        date_header = next((h['value'] for h in headers if h['name'].lower() == 'date'), None)
        email_date = datetime.strptime(date_header, '%a, %d %b %Y %H:%M:%S %z') if date_header else datetime.now()

        payload = message['payload']
        html_body = None

        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/html':
                    data = part['body']['data']
                    html_body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break
        
        if not html_body:
            print("Could not find HTML part in the email. Exiting.")
            return

        print("Parsing email content...")
        extracted_alerts = parse_email_content(html_body)

        if not extracted_alerts:
            print("Could not parse any alerts from the email body. Exiting.")
            return

        print("Formatting alerts for Obsidian...")
        markdown_content = format_alerts_for_obsidian(extracted_alerts, email_date)

        # Create file path
        vault_path = Path(OBSIDIAN_VAULT_PATH)
        output_dir = vault_path / OUTPUT_SUBFOLDER
        output_dir.mkdir(parents=True, exist_ok=True) # Ensure the subfolder exists
        
        note_title = email_date.strftime(NOTE_TITLE_FORMAT) + ".md"
        output_file = output_dir / note_title

        print(f"Writing alerts to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        # Mark the email as read so it's not processed again
        print(f"Marking email {msg_id} as read.")
        service.users().messages().modify(
            userId='me', 
            id=msg_id, 
            body={'removeLabelIds': ['UNREAD']}
        ).execute()

        print("\n✅ Success! The new Obsidian note has been created.")

    except HttpError as error:
        print(f"An error occurred: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()

````

### **How to Run It (First Time)**

1.  Open your terminal/command prompt.
2.  Navigate to the folder containing `process_alerts.py` and `credentials.json`.
3.  Run the script: `python process_alerts.py`
4.  Your web browser will open, asking you to log in to your Google account and grant permission. **You must approve this.**
5.  Once you approve, the script will continue. It will create a `token.json` file in the folder. You will not have to approve it again unless you delete this file. The script will then find your latest unread alert email and create the Obsidian note.

-----

### \#\# Part 4: Automation

Now, let's make this run automatically every day.

#### **On Windows (using Task Scheduler)**

1.  Open the Start Menu and search for "Task Scheduler".
2.  In the right-hand Actions panel, click "**Create Basic Task...**".
3.  Give it a name like "Obsidian Email Parser" and click **Next**.
4.  For the Trigger, choose "**Daily**" and click **Next**.
5.  Set a time you want it to run (e.g., 9:00 AM) and click **Next**.
6.  For the Action, choose "**Start a program**" and click **Next**.
7.  In the "Program/script" box, you need the full path to your Python executable. To find it, open Command Prompt and type `where python`. Copy this path.
8.  In the "Add arguments" box, type the full path to your `process_alerts.py` script.
9.  Click **Next** and then **Finish**.

#### **On macOS / Linux (using cron)**

1.  Open your terminal.

2.  Type `crontab -e` to edit your cron jobs.

3.  Add the following line to the end of the file. You will need to replace the paths with the correct full paths on your system.

      * To find your Python path, type `which python3` in the terminal.
      * To find your script path, navigate to the folder and type `pwd`.

    <!-- end list -->

    ```cron
    # Run the Obsidian email parser every day at 9:00 AM
    0 9 * * * /usr/bin/python3 /path/to/your/project/folder/process_alerts.py
    ```

4.  Save and close the file. Your script is now scheduled to run daily.