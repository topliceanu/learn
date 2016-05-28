var Q = require('q');
var request = require('request');

var conf = require('../conf');
var str = require('./str');
var util = require('./util')


var get = function (page) {
    /** Method fetches and populates the html content of a given page.
     * TODO handle http errors better, by incorporating a exponetial retry
     * policy in case of http timeouts of 503 response codes. Also pages which
     * failed could easily be added to a failedPagesQueue for later analysis.
     * @param {Page} page
     * @return Object, Promise resolves with the input page after it was updated.
     */
    options = {
        method: 'GET',
        url: page.protocol + '//' + page.host + page.path,
        followRedirect: false, // don't allow redirects.
        gzip: true, // accept encoded response to speed up fetching up.
        timeout: conf.timeout // num seconds timeout to download page.
    };
    return Q.nfcall(request, options).spread(function (response, body) {
        page.html = body;
        return Q(page);
    });
};

var getParallel = function (pages) {
    /** Method fetches and populates html field for multiple pages.
     * @param {Array<Object>} pages, list of lib.Page instances.
     * @return Promise resolves with all successful pages have been populated.
     */
    return Q.allSettled(pages.map(function (page) {
        return get(page);
    })).then(function (results) {
        var successful = []
        results.forEach(function (result) {
            if (result.state !== 'fulfilled') {
                return util.log('error', result.reason);
            }
            successful.push(result.value);
        });
        return successful
    });
};


exports.get = get;
exports.getParallel = getParallel;
