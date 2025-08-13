
# neessary changes
## producer 
-  does not need to check redis for already queued urls since producer is the first to put urls in a queue, those are the seeds

## fetcher
- should create a mongodb entry with the url and the html, then publishing the url only to `pages_to_parse`

## parser
- pulls a url from the `pages_to_parse` queue, which makes him pull the html from mongodb.
- Parses the HTML to extract the page title and all unique internal links, not the content since its already in mongodb as raw html
- For each link it checks redis, only new urls are then added to the  `urls_to_crawl` queue for the fetcher to process later

## What will be saved to MongoDB? 

```
   1     {
   2         "url": "https://example.com/page",
   3         "title": "Page Title",
   4         "links": ["https://de.wikipedia.org/link1", "https://de.wikipedia.org/link2"],
   5         "raw_html": { /* just the raw html */ },
   6         "domain": de  /* the subdomain of the page */
   7     }
```


## what about the saver?
i think we dont need one, it is true that the parser does also parse out title and links AND saves to database, however putting a whole raw html into the rabbitmq queue might no be optimal, too