var _ = require('underscore');


var Page = function (opts) {
    /** Page abstraction.
     *
     * The page's unique ID is considered to be the path, ie. combination of
     * pathname and query string. The hash fragment is ignored.
     * @param {Object} opts, format {href, protocol, host, path}
     */
    _.extend(this, {
        href: undefined,
        protocol: undefined,
        host: undefined,
        path: undefined,
        assets: {
            js: [],
            css: [],
            img: []
        },
        children: {},
        html: undefined,
        processed: false
    }, opts);
};


module.exports = Page;
