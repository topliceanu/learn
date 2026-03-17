var _ = require('underscore');

var Page = require('./Page');


var SiteGraph = function () {
    /** Data structure to contain all the pages in a domain. Each page
     * maintains a list of links to other pages from the same domain.
     * Pages are indexed by path, which is their unique ID.
     *
     * @param {Object} pages, a dictionary where the key is the page's path
     *                        and the value is the page reference.
     */
    this.pages = {};
};

SiteGraph.prototype.newPage = function (opts, template) {
    /** Factory which created pages corresponding to the input path. If the
     * page already exists, return that, otherwise create a new Page and index
     * it. This is the only permitted way to create new pages, because each page
     * acts like a singleton.
     * @see: https://nodejs.org/api/url.html#url_url
     * @param {Object} opts, format {href, protocol, host, path}
     * @param {Page} template, a page from where to pick up missing url props.
     * @return {Page}
     */
    if (!this.pages[opts.path]) {
        if (opts.host == null && opts.path[0] !== '/') {
            opts.path = '/'+opts.path;
        }
        opts.host = opts.host != null ? opts.host : template.host;
        opts.protocol = opts.protocol != null ? opts.protocol : template.protocol;
        this.pages[opts.path] = new Page(opts);
    }
    return this.pages[opts.path];
};

SiteGraph.prototype.lookup = function (path) {
    /** Returns a page instance by it's path.
     * @param {String} path
     * @return {Page} If undefined is returned, it means the page was not yet
     *                added to the graph.
     */
    return this.pages[path];
};

SiteGraph.prototype.toTree = function (rootPath) {
    /** Produces a Tree representation of the Page SiteGraph as a plain object.
     * @param {String} rootPath, the path corresponding to the page that is
     *                           considered the root.
     * @return {Object}
     */
    if (rootPath == null) {
        rootPath = '/';
    }

    var alreadyTraversed = {}

    var traverse = function (node) {
        if (node == null) {
            return undefined;
        }
        if (alreadyTraversed[node.path] === true) {
            return undefined;
        }
        alreadyTraversed[node.path] = true;

        var out = {
            'path': node.path,
            'assets': node.assets,
            'children': {}
        };
        _.each(node.children, function (child) {
            if (child instanceof Page) {
                out.children[child.path] = traverse(child, alreadyTraversed);
            }
        });
        return out;
    };

    return traverse(this.pages[rootPath], alreadyTraversed);
};


module.exports = SiteGraph;
