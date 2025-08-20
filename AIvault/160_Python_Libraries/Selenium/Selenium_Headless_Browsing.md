---
tags:
  - python
  - selenium
  - webdriver
  - browser_automation
  - headless
  - server_side_scraping
  - concept
  - example
aliases:
  - Selenium Headless Mode
  - Headless Chrome
  - Headless Firefox
related:
  - "[[160_Python_Libraries/Selenium/_Selenium_MOC|_Selenium_MOC]]"
  - "[[Selenium_WebDriver_Basics]]"
worksheet:
  - WS_WebScraping_1
  - WS_Automation_1
date_created: 2025-08-20
---
# Selenium: Headless Browsing

## Definition
**Headless browsing** refers to running a web browser without a graphical user interface (GUI). When you run Selenium in headless mode, the browser does everything it normally would—loading pages, executing JavaScript, rendering HTML—but it does so in the background without displaying any visible UI window.

This capability is crucial for running automated browser tasks on servers or in environments where a graphical display is not available or desired.

## Why Use Headless Mode?
-   **Server-Side Execution:** The primary reason. Most servers (e.g., Linux servers used for CI/CD pipelines, cloud virtual machines) do not have a graphical desktop environment installed. Headless mode allows Selenium scripts to run in these environments.
-   **Performance:** Running without a GUI can be slightly faster and consume fewer system resources (CPU, memory) compared to running a full browser window, as the overhead of rendering visual elements is eliminated.
-   **Parallel Execution:** When running multiple browser instances in parallel for large-scale testing or scraping, headless mode prevents numerous browser windows from cluttering the screen and consuming desktop resources.
-   **Automation & CI/CD:** Essential for integrating browser automation into continuous integration/continuous deployment (CI/CD) pipelines.

## How to Configure Headless Mode
Headless mode is enabled by setting a specific argument in the browser's `Options` object before initializing the WebDriver.

[list2tab|#Headless Configuration]
- Google Chrome
    -   **Argument:** `--headless` or (newer versions) `--headless=new`. The new headless mode is recommended as it's closer to the regular browser's behavior.
    -   **Code:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        # chrome_options = Options()
        # chrome_options.add_argument("--headless=new") # Use new headless mode
        # chrome_options.add_argument("--disable-gpu") # Often recommended for headless on some systems
        # chrome_options.add_argument("--window-size=1920,1080") # Set a window size to avoid issues with responsive design

        # driver = webdriver.Chrome(
        #     service=Service(ChromeDriverManager().install()),
        #     options=chrome_options
        # )

        # try:
        #     driver.get("http://example.com")
        #     print(f"Headless Chrome Page Title: {driver.title}")
        # finally:
        #     driver.quit()
        ```
- Mozilla Firefox
    -   **Argument:** `-headless`
    -   **Code:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        # firefox_options = Options()
        # firefox_options.add_argument("-headless")

        # driver = webdriver.Firefox(
        #     service=Service(GeckoDriverManager().install()),
        #     options=firefox_options
        # )

        # try:
        #     driver.get("http://example.com")
        #     print(f"Headless Firefox Page Title: {driver.title}")
        # finally:
        #     driver.quit()
        ```
- Microsoft Edge
    -   **Argument:** `--headless=new` (similar to Chrome)
    -   **Code:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        # edge_options = Options()
        # edge_options.add_argument("--headless=new")

        # driver = webdriver.Edge(
        #     service=Service(EdgeChromiumDriverManager().install()),
        #     options=edge_options
        # )

        # try:
        #     driver.get("http://example.com")
        #     print(f"Headless Edge Page Title: {driver.title}")
        # finally:
        #     driver.quit()
        ```

## Considerations and Potential Issues
-   **Different Behavior:** In some rare cases, websites might behave differently when they detect a headless browser. The "new" headless mode in Chrome (`--headless=new`) is designed to be more like the regular browser to mitigate this.
-   **Debugging:** Debugging can be more challenging without a visible browser window. It's often useful to develop and debug scripts in normal (headed) mode first, and then switch to headless mode for deployment.
-   **Taking Screenshots:** Even in headless mode, you can still take screenshots (`driver.save_screenshot('screenshot.png')`), which is an invaluable tool for debugging what the headless browser "sees."
-   **Window Size:** Some websites render differently based on the viewport size. It's good practice to set a realistic window size (e.g., `options.add_argument("--window-size=1920,1080")`) even in headless mode to ensure consistent rendering.

Headless browsing is an essential feature that makes Selenium a viable tool for server-side web scraping and automated testing at scale.

---