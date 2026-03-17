http = require('http');

chai = require('chai');
Q = require('q');

Page = require('../lib/Page');
net = require('../lib/net');


describe('net', function () {

    before(function () {
        this.server = http.createServer(function (req, res) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.end('Hello!');
        });
        this.server.listen(3000, '0.0.0.0');
    });

    after(function (done) {
        this.server.close(done);
    });

    describe('.get()', function () {
        it('should fetch and populate the html given a page', function (done) {
            var page = new Page({
                protocol: 'http:',
                host: 'localhost:3000',
                path: '/'
            });

            net.get(page).then(function () {
                chai.assert.equal(page.html, 'Hello!',
                    'should have produced the correct html');
            }).then(function () {done();}, done);
        });
    });

    describe('.getParallel()', function () {
        it('should fetch multiple pages at once', function (done) {
            var page1 = new Page({
                protocol: 'http:',
                host: 'localhost:3000',
                path: '/'
            });
            var page2 = new Page({
                protocol: 'http:',
                host: 'localhost:3000',
                path: '/'
            });
            var page3 = new Page({
                protocol: 'http:',
                host: 'localhost:3000',
                path: '/'
            });

            net.getParallel([page1, page2, page3]).then(function () {
                chai.assert.equal(page1.html, 'Hello!',
                    'should have fetched the contents of first page');
                chai.assert.equal(page2.html, 'Hello!',
                    'should have fetched the contents of second page');
                chai.assert.equal(page3.html, 'Hello!',
                    'should have fetched the contents of third page');
            }).then(function () {done();}, done);
        });
    });
});
