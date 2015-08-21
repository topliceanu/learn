# Crawler

## Specs

- should only parse a single domain, ie. ignore outgoing links.
- cli tool with a single argument, a seed url
- should output a site map
- for each page display which static assets each page depends on: images, css, js, video, etc.
- prevent infinite loops, make sure you don't crawl pages you already crawled
- focus on the speed of the crawler
- handle the case when the same page has different urls.

## Architecture

To make the crawling faster, in a single thread async env, such as a javascript process,
we need to batch the fetching of pages. The speedup comes from the fact that, even though
we initiate and process HTTP requests sequentially, the waiting for each request is done
in parallel.

```
           +--------+
           | Domain |
           +--------+
             | | | |
             v v v v
           +---------+
      +----| crawler |<---+
      |    +---------+    |
      v                   v
  +-------+           +---------+
  | Queue |<----------| SiteMap |
  +-------+           +---------+
                           ^
                           |
                       +------+
                       | init |
                       +------+
```

## Data Structures
- Page - contains all information about a page
```
{
    parentUrl:String, // contains only the path and query string portions of the url.
    parent:Page, // reference to the parent page
    domain:String, // contains the domain of the url
    url:String, // contains only the path and query string portions of the url.
    asserts:{
        js:[String],
        css:[String],
        img: [String]
    },
    children:{
        url: Page
    },
    html:String,
}
```

- SiteMap - a tree structure holding all the Page objects, the root is the Page corresponding to the seed.
```
{
    root: Page,
    byUrl: { // Page index, usefull for retrieving a page by their URL.
        url: Page
    },
    byChecksum: { // Page index, usefull for retrieving pages by checksum of their HTML.
        checksum: Page
    }
}
```

- Queue - a simple queue containing un-parsed pages, allows the fetcher to download more pages at a time.
```
[Page]
```

## Components

- init
    - extract (domain, path) from the input seed url.
    - Build the first Page object and insert it into the Queue.
    - start the parser.
    - when the parser finished, print the SiteMap
- Parser
    - retrieve a batch of Pages from the queue.
    - instruct the fetcher to retrieve contents for a batch of Pages.
    - extract static assets from the html of each page.
    - extract links from the html of each page.
    - for each page, populate checksum and check with SiteMap for a possible already-parsed alias page, if so populate alias field.
    - for each link, check with SiteMap data structure if the page was already processed.
        - if not, create new Page objects for these links and push them into the queue.
    - push all populated pages into the SiteMap.
    - stop when
- Fetcher
    - to speed up DNS lookup, resolve hostname once for the entire website and use the IP to fetch pages.
    - fetch configurable number of Page objects from the Queue.
    - initiate GET requests in parallel for each one of these Pages, then populate the html field.
        - all errored pages, push them into an ErroredPagesQueue.
    - return all the successully fetched pages to the parser.

## Code
- a function which splits the domain from path&query from the url. Should ignore the hash fragment.

1. A tree data structure which holds the results.
    - Each page is a node
        - each node contains a list of all static assets in a page
    - the seed page is the root.
    - are we interested in circular links?
2. A hash table which holds the hashed contents of each page as key and a list
   of alias urls to that page as value.
2. A stack data structure which contains pages that have not yet been parsed.
3. A parser component, ie. a collection of functions:
    - a function which extracts all the links to other pages
    - a filter function which filters out all the links belonging to other domains.
    - a function which returns all the js/img/css static file urls given a page.
4. A set containing all the urls that have been parsed so far.
5. A system to fetch a group of pages in parallel, ie. amortize the wait on
   http requests to return a response.
    - use Q and request
6. A function which splits the domain name and the url.
    - strip out all the hash parts.

## Dependencies
- Q, for promises
- requst, for easy http request.

## References
1. [Design and Implementation of a High Performance Distributed Web-Crawler](http://cis.poly.edu/suel/papers/crawl.pdf)
