var _ = require('underscore');
var Q = require('q');

var conf = require('../conf');
var net = require('./net');
var str = require('./str');
var util = require('./util');


var shiftBatch = function (arr, size) {
    /** Shifts size elements from input array. If not enough elements exist in
     * the array, it will return only what it finds.
     * @param {Array} arr - note that this array gets modified!
     * @param {Number} size
     * @return {Array}
     */
    var batch = [];
    while (arr.length !== 0 && size > 0) {
        batch.push(arr.shift());
        size -= 1;
    }
    return batch;
};

var notAlreadyProcessed = function (page) {
    /** Method return True if the page was marked as processed
     * @param {Page} page
     * @return {Boolean}
     */
    return page.processed === false;
};

var getAssets = function (page) {
    /** Returns lists of static assets extracted from the input page.
     * TODO add extractors for more static resource types, like video, audio, etc.
     * @param {Page} page
     * @return {Object} format {js:[], css: [], img: []}
     */
    return {
        js: str.extract(page.html, /<script.*?src="(.*?)".*?>/gim),
        css: str.extract(page.html, /<link.*?href="(.*?)".*?>/gim)
                .filter(function (link) {
                    return link.substr(-4) === '.css';
                }),
        img: str.extract(page.html, /<img.*?src="(.*?)".*?>/gim)
    };
};

var extractChildren = function (page, graph) {
    /** Returns a list of child pages (from the same domain as page) which
     * have links in page's html.
     * @param {Page} page - page instance to extract links from
     * @return {Array<Page>} list of Page instances for each child page.
     *                       No duplicates are returned!
     */
    return str.extract(page.html, /<a.*?href="(.*?)".*?>/gim)
       .reduce(function (collector, link) {
            var parsed = str.parse(link);
            if (parsed.path) {
                collector.push(graph.newPage(parsed, page));
            }
            return collector
       }, [])
       .filter(function (child) {
            return page.host === child.host;
       });
};

var crawl = function (seed, queue, graph) {
    /** Main method for crawling a domain specified by the seed page.
     * The general idea to speed up the crawling is to initiate GET requests for
     * multiple pages and wait for the reponses in parallel.
     *
     * @param {Page} seed, the initial page to crawl.
     * @param {Array<Page>} queue, list of page unprocessed so far.
     * @param {SiteGraph} graph, data structure representing the site pages.
     * @return Promise object resolves when all reachable pages have been crawled.
     */
    var pages = shiftBatch(queue, conf.numPages).filter(notAlreadyProcessed);
    if (pages.length === 0) { // Stop when the queue of unprocessed pages is empty.
        return Q(graph);
    }
    util.log('info', 'started crawling pages '+_.pluck(pages, 'path'));
    return net.getParallel(pages).then(function () {
        pages.forEach(function (page) {
            page.assets = getAssets(page);
            var children = extractChildren(page, graph);
            page.children = _.object(_.pluck(children, 'path'), children);
            page.processed = true;

            children
                .filter(notAlreadyProcessed)
                .forEach(function (child) {
                    if (queue.indexOf(child) === -1) {
                        queue.push(child);
                    }
                });
        });
        return crawl(seed, queue, graph);
    });
};


exports.shiftBatch = shiftBatch;
exports.notAlreadyProcessed = notAlreadyProcessed;
exports.getAssets = getAssets;
exports.extractChildren = extractChildren;
exports.crawl = crawl;
