# Crawler

Web cralwer for GoCardless


## Usage
```bash
$ npm install
$ npm test
$ node index.js https://gocardless.com >> output.txt
```

## Specs

- should only parse a single domain, ie. ignore outgoing links.
- cli tool with a single argument, a seed url
- should output a site map
- for each page display which static assets each page depends on: images, css, js, video, etc.
- prevent infinite loops, make sure you don't crawl pages you already crawled
- focus on the speed of the crawler
- handle the case when the same page has different urls.


## Features, Issues and TODOs
1. `Extracting assets from a page` is difficult because there are a lot of
types of static assets which would ammount to a complicated and hard to maintain
RegExp object. The alternative would be to use a DOM implementation (Eg jsdom)
and use that to consistenly fetch all assets. This is much more resiliant than
RegExp but it is also significantly slower and, since the key requirement of
the tool was speed, I dropped this solution. To simplify further, I'm only looking
for `<script>`, `<link>` and `<img>` tags. This can and should be expanded to
get a larger set of static dependencies from an html page.

2. `Extracting links from a page` is equally difficult, for the same above reason,
I only looked for `<a>` tags and extracted their `href` value.

3. A nice feature of my implementation is that it builds a Graph of pages, which
can be usefull in many other ways, from which the sitemap tree is extracted. The
sitemap, however, is just a plain object, so it's not very pretty to look at and it is large.
This solution could easily be extended to include a better render, eg. npm uses
[archy](https://www.npmjs.com/package/archy) to pretty print module dependency trees.

4. A test suite exists the `/test` folder, it covers the core functionality and
the most delicate methods in the code base. My intention was not to provide full
test coverage, but to aid me in developing the solution. For a production app, 100%
test coverage would be very usefull.

5. Errors produced by the parser are logged but muffled, ie. no bespoke action is taken.
In production, error aggregation and monitoring are crucial for extending the
effictiveness of the crawler.

6. Another nice feature is that you can control the number of pages to be fetched in parallel
using the configuration module. This could be used to determine empirically what is the
best performance for a specific env: crawled website, hardware performance,
available bandwith, etc.


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
  +-------+         +-----------+
  | Queue |<--------| SiteGraph |
  +-------+         +-----------+
                           ^
                           |
                       +------+
                       | init |
                       +------+
```

## Components

- init
    - extract (domain, path) from the input seed url.
    - Build the first Page object and insert it into the Queue.
    - start the cralwer.
    - when the crawler finishes, print the site map.
- crawler
    - retrieve a batch of Pages from the queue.
    - instruct the net module to retrieve contents for a batch of Pages.
    - extract static assets from the html of each page.
    - extract links from the html of each page.
    - for each link, check with SiteMap data structure if the page was already processed.
        - if not, create new Page objects for these links and push them into the queue.
    - push all populated pages into the SiteMap.
    - stop when the list of unprocessed queue is empty.
- net
    - to speed up DNS lookup, resolve hostname once for the entire website and use the IP to fetch pages.
    - fetch configurable number of Page objects from the Queue.
    - initiate GET requests in parallel for each one of these Pages, then populate the html field.
        - all errored pages, push them into an ErroredPagesQueue.
    - return all the successully fetched pages to the parser.
- SiteGraph
    - data structure to create and store all Page instances.
    - ability to build a tree representation of the SiteGraph starting with a root page.
        - it should handle cicles and it should only output each page's path, assets and children.


## Data Structures
- Page - contains all information about a page
```
{
    href:String, // initial url
    host:Page, // hostname and port
    path:String, // pathname and query string
    protocol:String // either http: or https:
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
    pages: {path: Page} // an set of Page instances indexed by their path.
}
```

- Queue - a simple queue containing un-parsed pages, allows the fetcher to download more pages at a time.
```
[Page]
```

## References
1. [Design and Implementation of a High Performance Distributed Web-Crawler](http://cis.poly.edu/suel/papers/crawl.pdf)
