var http = require('http');
var fs = require('fs');
var path = require('path');

var _ = require('underscore');
var chai = require('chai');
var express = require('express');

var crawler = require('../lib/crawler');
var SiteGraph = require('../lib/SiteGraph');
var str = require('../lib/str');


describe('crawler', function () {

    before(function (done) {
        // Extract the fixture page.
        var filePath = path.join(__dirname, 'fixtures', 'page.html');
        var that = this
        fs.readFile(filePath, {encoding: 'utf-8'}, function (err, data) {
            if (err) return done(err);
            that.html = data
            done();
        });
    });

    describe('.shiftBatch()', function () {
        it('should correctly return a subset of the input arr', function () {
            var arr = [1,2,3,4,5,6]

            var res1 = crawler.shiftBatch(arr, 4)
            chai.assert.sameMembers(res1, [1,2,3,4],
                'should produce the first complete batch');

            var res2 = crawler.shiftBatch(arr, 4)
            chai.assert.sameMembers(res2, [5,6],
                'should produce the second incomplete batch');

            var res3 = crawler.shiftBatch(arr, 4)
            chai.assert.sameMembers(res3, [],
                'should produce an empty batch');
        });
    });

    describe('.getAssets()', function () {
        it('should extract static assets from an html doc', function () {
            var page = {
                html: this.html
            };
            var actual = crawler.getAssets(page);
            var expected = {
                "css": [
                    "assets/style.css",
                    "assets/sh.css",
                ],
                "img": [
                    "assets/logo.svg",
                    "/images/logo-light.svg",
                    "assets/joyent-footer.svg",
                ],
                "js": [
                    "//use.typekit.net/mse5tqx.js",
                    "/sh_main.js",
                    "/sh_javascript.min.js",
                ]
            };
            chai.assert.deepEqual(actual, expected, 'should extract correct list');
        });
    });

    describe('.extractChildren()', function () {
        it('should extract all links to pages on the same domain', function () {
            var siteGraph = new SiteGraph()
            var page = siteGraph.newPage(str.parse('https://nodejs.org/api/index.html'));
            page.html = this.html;

            var children = crawler.extractChildren(page, siteGraph);
            children.forEach(function (child) {
                chai.assert.include(['http:', 'https:'], child.protocol,
                    'page protocol should be correctly set');
                chai.assert.equal(child.host, 'nodejs.org',
                    'sets the correct hostname to all the parsed pages')
            });
        });
    });

    describe('.crawl()', function () {
        before(function () {
            // Start a simple webserver to deliver a mockup site.
            this.pages = {
                root:  '<div>'+
                            '<h1>Root</h1>'+
                            '<img src="static/awesome.jpg" alt="">'+
                            '<script src="static/jquery.js"></script>'+
                            '<link rel="stylesheet" href="static/bootstrap.css">'+
                            '<a href="/">link to home</a>'+
                            '<a href="/page1">link to page1</a>'+
                            '<a href="/page2">link to page2</a>'+
                        '</div>',
                page1: '<div>'+
                            '<h1>Page1</h1>'+
                            '<img src="static/awesome.jpg" alt="">'+
                            '<script src="static/jquery.js"></script>'+
                            '<link rel="stylesheet" href="static/bootstrap.css">'+
                            '<a href="/">link to home</a>'+
                            '<a href="/page1">link to page1</a>'+
                            '<a href="/page2">link to page2</a>'+
                        '</div>',
                page2: '<div>'+
                            '<h1>Page2</h1>'+
                            '<img src="static/awesome.jpg" alt="">'+
                            '<script src="static/jquery.js"></script>'+
                            '<link rel="stylesheet" href="static/bootstrap.css">'+
                            '<a href="/">link to home</a>'+
                            '<a href="/page1">link to page1</a>'+
                            '<a href="/page2">link to page2</a>'+
                        '</div>'
            };
            var app = express();
            var that = this;
            app.get('/', function (req, res) {
                res.send(that.pages.root);
            });
            app.get('/page1', function (req, res) {
                res.send(that.pages.page1);
            });
            app.get('/page2', function (req, res) {
                res.send(that.pages.page2);
            });
            this.server = http.createServer(app).listen(3001, 'localhost');
        });

        after(function (done) {
            this.server.close(done);
        });

        it('should successfully crawl a tree of pages', function (done) {
            var graph = new SiteGraph();
            var seed = graph.newPage(str.parse('http://localhost:3001/page1'));
            var queue = [seed];
            var that = this;

            crawler.crawl(seed, queue, graph).then(function (graph) {
                var expectedAssets = {
                    js: ['static/jquery.js'],
                    css: ['static/bootstrap.css'],
                    img: ['static/awesome.jpg']
                };

                chai.assert.equal(graph.pages['/'].html, that.pages.root,
                    'crawler fetched the html of the homepage');
                chai.assert.deepEqual(graph.pages['/'].assets, expectedAssets,
                    'produced the correct assets');
                chai.assert.deepEqual(Object.keys(graph.pages['/'].children),
                    ['/', '/page1', '/page2'],
                    'should produce the correct children list');
                chai.assert.equal(graph.pages['/page1'].html, that.pages.page1,
                    'crawler fetched the html of page1');
                chai.assert.deepEqual(graph.pages['/page1'].assets, expectedAssets,
                    'produced the correct assets');
                chai.assert.deepEqual(Object.keys(graph.pages['/page2'].children),
                    ['/', '/page1', '/page2'],
                    'should produce the correct children list');
                chai.assert.equal(graph.pages['/page2'].html, that.pages.page2,
                    'crawler fetched the html of page2');
                chai.assert.deepEqual(graph.pages['/page2'].assets, expectedAssets,
                    'produced the correct assets');
                chai.assert.deepEqual(Object.keys(graph.pages['/page1'].children),
                    ['/', '/page1', '/page2'],
                    'should produce the correct children list');
                done()
            }).fail(done);
        });
    });
});
