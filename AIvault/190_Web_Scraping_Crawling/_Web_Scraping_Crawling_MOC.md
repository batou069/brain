---
tags:
  - web_scraping
  - web_crawling
  - data_extraction
  - html
  - css
  - javascript
  - moc
  - concept
  - spider
  - bot
aliases:
  - Web Scraping MOC
  - Web Crawling MOC
  - Data Extraction Web MOC
  - Web Crawler
  - Spidering
  - Web Spider
  - Web Bot
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[160_Python_Libraries/Requests_Library|Requests Library]]"
  - "[[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|Beautiful Soup MOC]]"
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy MOC]]"
  - "[[Selenium_WebDriver|Selenium WebDriver]]"
  - "[[Playwright_Library]]"
  - "[[HTML_Basics]]"
  - "[[CSS_Selectors]]"
  - "[[XPath_Selectors]]"
  - "[[JavaScript_Basics_for_Scraping|JavaScript Basics for Scraping]]"
  - "[[Static_vs_Dynamic_Web_Pages]]"
  - "[[_Web_Scraping_Crawling_MOC]]"
  - "[[What_is_Web_Scraping]]"
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy Framework]]"
  - "[[Robots_txt]]"
  - "[[Sitemaps_XML]]"
worksheet:
  - WS_WebScraping_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Web Scraping and Crawling MOC 🕸️⛏️

This section covers the concepts, techniques, tools, and ethical considerations involved in **web scraping** (extracting data from websites) and **web crawling** (systematically browsing the World Wide Web, typically for web indexing or data mining).

## Core Concepts
-   [[What_is_Web_Scraping|What is Web Scraping?]]
    -   [[Data_Extraction_Web|Data Extraction Techniques]]
-   [[What_is_Web_Crawling|What is Web Crawling (Spiders/Bots)?]]
-   [[HTML_Basics|Understanding HTML Structure (Tags, Attributes)]]
    -   [[HTML_Common_Tags|Common HTML Tags for Scraping]]
    -   [[HTML_Common_Attributes|Common HTML Attributes for Selection]]
-   [[DOM_Document_Object_Model|DOM (Document Object Model)]]
-   [[HTML_Parsing|HTML Parsing]]
-   [[CSS_Selectors|Using CSS Selectors for Extraction]]
-   [[XPath_Selectors|Using XPath for Extraction]]
-   [[Static_vs_Dynamic_Web_Pages|Static vs. Dynamic Web Pages]]
    -   Impact of [[JavaScript_Basics_for_Scraping|JavaScript]] on Scraping
-   [[Handling_Dynamic_Content_Scraping|Handling Dynamic Content (AJAX, XHR)]]
-   [[Web_Drivers_for_Scraping|Using Web Drivers (e.g., Selenium, Playwright)]] for dynamic sites.
-   [[User_Agent_Web_Scraping|User-Agents and Their Role]]
-   [[Robots_txt|Understanding `robots.txt`]]
-   [[Ethical_Considerations_Web_Scraping|Ethical and Legal Considerations in Web Scraping]]
    -   [[Scraping_vs_Theft|Scraping vs. Theft: The Line]]
-   [[Challenges_in_Web_Scraping|Common Challenges in Web Scraping]]
    -   Anti-scraping measures, CAPTCHAs, IP blocking.
    -   [[DOS_Attack_Defenses_Impact_Scraping|Defenses Against DOS Attacks and Their Impact]]
    -   Rate limiting.
    -   Handling website structure changes.
-   [[Web_Scraping_Best_Practices|Best Practices for Responsible Web Scraping]]

## Key Tools & Libraries (Python Focus)
-   **HTTP Requests:**
    -   [[160_Python_Libraries/Requests_Library|Requests Library]]
-   **HTML/XML Parsing:**
    -   [[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|Beautiful Soup]]
    -   `lxml`
-   **Web Crawling Frameworks:**
    -   [[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy Framework]]
-   **Browser Automation (for Dynamic Sites):**
    -   [[Selenium_WebDriver|Selenium WebDriver]]
    -   [[Playwright_Library|Playwright]]
    -   `pyppeteer` (Puppeteer for Python)

## Questions Addressed
-   [[How_to_Scrape_Unknown_HTML_Structure|How can you scrape if the HTML structure is unknown?]]
-   [[Scraping_Interactive_Web_Pages|Solutions for web pages accessible only through interactions (e.g., login)?]]
-   [[Tricking_Target_Server_Identity|Can you trick the target server into believing you are someone else?]]

## Notes in this Section
```dataview
LIST
FROM "190_Web_Scraping_Crawling"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC") AND !contains(file.folder, "HTML_Elements")
SORT file.name ASC
```

### HTML Elements Sub-Section
```dataview
LIST
FROM "190_Web_Scraping_Crawling/HTML_Elements"
WHERE file.folder != this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---

# Web Crawling (Spidering)

## Definition
**Web Crawling**, also known as **spidering** or **web spidering**, is the process of systematically browsing the World Wide Web, typically for the purpose of web indexing, data mining, or [[What_is_Web_Scraping|web scraping]] across multiple pages of a website or multiple websites. A program or automated script that performs crawling is called a **web crawler**, **spider**, or **bot**.

Crawlers start with a list of URLs to visit, called seeds. As the crawler visits these URLs, it identifies all the hyperlinks in the page and adds them to the list of URLs to visit, called the crawl frontier. URLs from the frontier are recursively visited according to a set of policies.

## Purpose of Web Crawling
-   **Search Engine Indexing:** The most well-known use. Search engines like Google, Bing, and DuckDuckGo use crawlers (e.g., Googlebot) to discover and download web pages, which are then indexed to build their search database.
-   **Web Archiving:** Archiving websites for historical purposes (e.g., Internet Archive's Wayback Machine).
-   **Data Mining & Analysis:** Collecting large amounts of data from the web for analysis, such as market research, sentiment analysis, price monitoring, or academic research.
-   **[[What_is_Web_Scraping|Web Scraping]] at Scale:** When data needs to be extracted from many pages within a website (e.g., all product pages in an e-commerce site, all articles in a news archive), a crawler is needed to discover and visit these pages before scraping data from each one.
-   **Website Health Monitoring:** Checking for broken links, monitoring website changes, or ensuring website availability.
-   **Information Retrieval:** Finding specific types of information across many sites (e.g., job postings, academic papers).

## How Web Crawlers Work (Simplified Process)

[d2]
```d2
direction: TB
shape: sequence_diagram

User: "User/System"
Crawler: "Web Crawler" {
  shape: process
  style.fill: "#E0F2F7"
  SeedURLs: "Seed URLs" {shape: step; style.fill: "#FFF9C4"}
  URLFrontier: "URL Frontier (Queue/Priority Queue)" {shape: data; style.fill: "#FFF9C4"}
  Downloader: "HTTP Downloader" {shape: process; style.fill: "#C8E6C9"}
  Parser: "HTML/Link Parser" {shape: process; style.fill: "#C8E6C9"}
  DataStore: "Data Storage (Optional)" {shape: database; style.fill: "#FFCCBC"}
  VisitedSet: "Visited URLs Set" {shape: data; style.fill: "#FFF9C4"}
}
WebServer: "Web Server(s)" {
  shape: Zylinder # Using Zylinder for server representation
  style.fill: "#D1C4E9"
}

User -> Crawler.SeedURLs: "1. Provide Initial Seed URLs"
Crawler.SeedURLs -> Crawler.URLFrontier: "2. Add to Frontier"

loop {
  Crawler.URLFrontier -> Crawler.Downloader: "3. Get Next URL"
  Crawler.Downloader -> WebServer: "4. Fetch Page (HTTP GET)"
  WebServer -> Crawler.Downloader: "5. Return HTML Response"
  Crawler.Downloader -> Crawler.Parser: "6. Pass HTML"
  Crawler.Parser -> Crawler.DataStore: "7. Extract & Store Data (Scraping)"
  Crawler.Parser -> Crawler.URLFrontier: "8. Extract New Links, Add to Frontier (if not visited & allowed)"
  Crawler.Downloader -> Crawler.VisitedSet: "9. Mark URL as Visited"
}

style User { icon: "🧑‍💻" }
style Crawler { icon: "🕷️" }
style WebServer { icon: "🌐" }
```

1.  **Initialization:** The crawler starts with a list of initial URLs, known as **seeds**.
2.  **URL Frontier:** These seeds are added to a **URL frontier** (often a queue or priority queue) which manages the list of URLs to be visited.
3.  **Fetching:** The crawler picks a URL from the frontier.
4.  **DNS Resolution & HTTP Request:** It resolves the URL's domain name to an IP address and makes an HTTP request (usually GET) to the web server to download the page content. It should respect [[Robots_txt|`robots.txt`]] rules.
5.  **Parsing:** The downloaded page (typically HTML) is parsed.
6.  **Link Extraction:** The crawler extracts all hyperlink URLs (`<a>` tags with `href` attributes) found on the page.
7.  **URL Filtering & Normalization:**
    -   Extracted URLs are normalized (e.g., converting relative URLs to absolute, removing fragments).
    -   URLs are checked against a set of **visited URLs** to avoid re-crawling already processed pages and getting into loops.
    -   Crawling policies are applied (e.g., stay within the same domain, respect crawl depth limits, filter by URL patterns).
8.  **Adding to Frontier:** New, valid, and unvisited URLs are added to the URL frontier.
9.  **Data Processing/Storage (Optional):** If the crawler is also a scraper, it extracts desired data from the parsed page and stores it. If it's for indexing, it might store the page content or extracted text.
10. **Loop:** The process repeats from step 3 until the frontier is empty, a crawl limit (e.g., number of pages, time) is reached, or the crawler is stopped.

## Key Considerations for Crawling
-   **[[Robots_txt|`robots.txt` (Robots Exclusion Protocol)]]:** Crawlers should respect the `robots.txt` file of websites, which specifies which parts of the site should not be accessed by crawlers.
-   **Crawl Rate / Politeness:** Making too many requests in a short period can overload a web server. Polite crawlers limit their request rate (e.g., by adding delays between requests, respecting `Crawl-delay` in `robots.txt`).
-   **[[User_Agent_Web_Scraping|User-Agent]]:** Crawlers should identify themselves with a clear User-Agent string, often including contact information.
-   **Duplicate Content Detection:** Avoiding processing the same content multiple times (e.g., due to different URLs pointing to the same page).
-   **Handling Different Content Types:** Beyond HTML, crawlers might encounter PDFs, images, etc.
-   **Scalability:** For large-scale crawling, distributed crawlers are used.
-   **Dynamic Content:** Crawling [[Static_vs_Dynamic_Web_Pages|dynamic websites]] that rely heavily on JavaScript may require [[Web_Drivers_for_Scraping|browser automation tools]] or techniques to execute JavaScript.
-   **Crawl Traps:** Websites might have structures (e.g., infinitely deep directory structures generated by parameters) that can trap a naive crawler in an infinite loop.
-   **[[Sitemaps_XML|Sitemaps]]:** XML sitemaps provided by websites can help crawlers discover URLs more efficiently.

Frameworks like [[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy]] provide many of these features (politeness, `robots.txt` handling, link extraction, request scheduling) out-of-the-box, simplifying the development of web crawlers.

---