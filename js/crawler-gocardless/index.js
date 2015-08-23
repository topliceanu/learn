/**
 * Entry point for the module. It has a simple command line interface.
 * All the action is happening in the lib/crawler#crawl() method
 *
 * Usage:
 *  node index.js <seed page to crawl>
 */


var crawler = require('./lib/crawler');
var SiteGraph = require('./lib/SiteGraph');
var str = require('./lib/str');
var util = require('./lib/util');


var graph = new SiteGraph;
var seed = graph.newPage(str.parse(process.argv[2]));
var queue = [seed];


util.log('info', 'Started crawling domain '+seed.host);
crawler.crawl(seed, queue, graph).then(function (graph) {
    util.log('info', 'Stopped crawling domain '+seed.host);
    console.log(JSON.stringify(graph.toTree(), null, 1));
}, function (error) {
    util.log('error', error);
});
