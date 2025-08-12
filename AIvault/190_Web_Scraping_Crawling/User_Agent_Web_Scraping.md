---
tags:
  - web_scraping
  - http
  - user_agent
  - web_crawling
  - bot_detection
  - concept
aliases:
  - User-Agent String
  - HTTP User-Agent
related:
  - "[[_Web_Scraping_Crawling_MOC]]"
  - "[[HTTP_Requests_Responses]]"
  - "[[Ethical_Considerations_Web_Scraping]]"
  - "[[Challenges_in_Web_Scraping]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-18
---
# User-Agent in Web Scraping

## Definition
A **User-Agent** is a string that a client application (like a web browser or a web scraper) sends as part of an [[HTTP_Requests_Responses|HTTP request header]]. This string identifies the client software to the web server.

The User-Agent string typically includes information such as:
-   The application type (e.g., browser, crawler)
-   Operating system
-   Software vendor
-   Software version

**Example User-Agent strings:**
-   **Chrome on Windows:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
-   **Firefox on Linux:** `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0`
-   **Python Requests library (default):** `python-requests/2.25.1` (version may vary)
-   **Googlebot (Google's crawler):** `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`

## Role in Web Scraping
The User-Agent string plays a significant role in web scraping for several reasons:

1.  **Server-Side Content Adaptation:**
    -   Some websites serve different content or layouts based on the User-Agent. For example, they might serve a mobile-optimized version to mobile browser User-Agents or simplified content to known crawler User-Agents.
    -   If a scraper uses a default User-Agent (like that of `python-requests`), it might receive different content than what a regular browser sees, or it might be easily identified as a bot.

2.  **Bot Detection and Blocking:**
    -   Web servers often analyze User-Agent strings as one of the first lines of defense against unwanted bot traffic or aggressive scraping.
    -   Using a generic or obviously bot-like User-Agent (or no User-Agent at all) can lead to the scraper being blocked (e.g., receiving HTTP 403 Forbidden errors) or served CAPTCHAs.
    -   Some sites maintain lists of known "bad" bot User-Agents.

3.  **Politeness and Identification:**
    -   [[Ethical_Considerations_Web_Scraping|Ethical scraping practices]] suggest that your scraper should identify itself with a custom User-Agent string. This string should ideally include:
        -   The name of your bot/project.
        -   A way to contact you (e.g., a URL to a project page or an email address).
    -   Example of a polite custom User-Agent: `MyProductPriceScraper/1.0 (+http://myproject.com/scraper_info)`
    -   This allows website administrators to identify your scraper's activity and contact you if it's causing issues.

4.  **Mimicking Real Browsers:**
    -   To avoid immediate detection or to receive content as a regular browser would, scrapers often **rotate through a list of common, legitimate browser User-Agent strings**.
    -   This makes the scraper's requests look more like those from actual users.
    -   However, relying solely on User-Agent spoofing is often not enough, as sophisticated anti-bot systems use other techniques (IP reputation, behavioral analysis, JavaScript challenges).

## Setting User-Agent in Python Libraries

-   **[[160_Python_Libraries/Requests_Library|Requests]]:**
    ```python
    import requests
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get("http://example.com", headers=headers)
    print(response.request.headers['User-Agent'])
    ```

-   **[[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy]]:**
    -   Can be set in `settings.py`:
        ```python
        # settings.py
        USER_AGENT = 'MyCoolScraper/1.0 (+http://www.example.com/contact)'
        ```
    -   Or overridden per spider or per request. Scrapy also has middleware for User-Agent rotation.

-   **[[Selenium_WebDriver|Selenium]] / [[Playwright_Library|Playwright]]:**
    -   These tools control actual browsers, so they typically send the User-Agent string of the browser they are controlling.
    -   It's possible to override the User-Agent in browser options when launching the browser instance if needed, though this is less common as the goal is often to emulate a real browser session accurately.

## Considerations
-   **Legitimacy:** While changing User-Agents can help bypass simple blocks, continuously rotating through many different User-Agents rapidly from a single IP can itself be a suspicious pattern.
-   **`robots.txt`:** Always respect `robots.txt`. User-Agent spoofing does not absolve a scraper from adhering to these rules (though `robots.txt` can have specific rules for specific User-Agents).
-   **Ethical Implications:** Be transparent if possible. A custom User-Agent indicating your bot's purpose and contact info is a good practice, even if you also rotate common browser User-Agents for access. See [[Tricking_Target_Server_Identity]].

Managing the User-Agent string is an important, albeit small, part of developing robust and considerate web scrapers.

---