var url = require('url');

var _ = require('underscore');


var parse = function (link) {
    /** Method parses a link into bits of interest.
     * @see: https://nodejs.org/api/url.html#url_url
     * @param {String} link
     * @return {Object} format {href, protocol, host, path}
     */
    var parsed = url.parse(link);
    return _.pick(parsed, ['href', 'protocol', 'host', 'path']);
};


var extract = function (text, regex) {
    /** Function applies regex recursively on the input text.
     * @param {String} text, haystack
     * @param {RegExp} regex, needle
     * @return {Array<String>} list of substrings from text which match regex.
     */
    var output = [];
    while ((found = regex.exec(text)) !== null) {
        output.push(found[1]);
    }
    return output;
};

var format = function (obj) {
    /** Alias to node's url.format. */
    return url.format(obj);
};


exports.extract = extract;
exports.format = format;
exports.parse = parse;
