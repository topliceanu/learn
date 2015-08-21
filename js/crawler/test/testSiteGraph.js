var SiteGraph = require('../lib/SiteGraph');
var str = require('../lib/str');


describe('SiteGraph', function () {
    describe('.newPage()', function () {
        it('should produce a correct new page given a '+
           'template page and an incomplete url', function () {
            var siteGraph = new SiteGraph();

            opts = str.parse('index.html') // partial url
            var template = {
                href: 'https://nodejs.org/api/index.html',
                protocol: 'https:',
                host: 'nodejs.org',
                path: '/api/index.html',
                assets: { js: [], css: [], img: [] },
                children: {},
                aliases: [],
                html: undefined,
                checksum: undefined
            }
            var page = siteGraph.newPage(opts, template);
            chai.assert.equal(page.protocol, 'https:', 'should borrow the protocol');
            chai.assert.equal(page.host, 'nodejs.org', 'should borrow the hostname');
            chai.assert.equal(page.path, '/index.html');
        });
    });

    describe('.toTree()', function () {
        it('should export a tree of the pages', function () {
            var siteGraph = new SiteGraph();

            var root = siteGraph.newPage(str.parse('/'), {});
            var page1 = siteGraph.newPage(str.parse('/page1'), {});
            var page2 = siteGraph.newPage(str.parse('/page2'), {});

            root.children['/page1'] = page1;
            root.children['/page2'] = page2;

            var actual = siteGraph.toTree('/');
            var expected = {
                path: '/',
                assets: { js: [], css: [], img: [] },
                children: {
                    '/page1': {
                        path: '/page1',
                        assets: { js: [], css: [], img: [] },
                        children: {}
                    },
                    '/page2': {
                        path: '/page2',
                        assets: { js: [], css: [], img: [] },
                        children: {}
                    }
                }
            };
            chai.assert.deepEqual(actual, expected,
                'should compose the correct sitemap tree')
        });
    });
});
