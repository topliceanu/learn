# 9.3 Web crawler

1. Scope the problem
- features: no loops, no duplicate pages, download all public pages
- size: 10billing pages * 50KB/page
2. Assumptions
- pages will not fit on one machine
- you can have different links (even different domains) to the same page
- you CAN'T have the same link produce different pages (cookies, user agent). Only store one version.
3. Diagram
- use case - crawl a page:
  - pick url from queue. Check if the url has been visited before. If positive go to 1.
  - download the page.
  - checksum the page. Check if the checksum was already generated. If positive go to 1.
  - store the page in the database.
  - update the page checksum and visited url hashes
  - extract links from it and put them on the queue
  - consume the url from the queue.
- ![diagram](https://excalidraw.com/#json=5095315308806144,Xbo-KWwrtoKE9t4rGcAdTg)
4. Key issues
- it's challenging to determine identical pages: You can't do it based on url or content.
  Solution: calculate a signature for each page.
  Solution: each url on the queue has a priority => priority queue.
- we may never finish crawling the Internet. Solution: prune the queue to remove urls with low priority

