module.exports = function (obj, path) {
    /** Method extracts a value from a deeply nested object
     * @param {Object} obj
     * @param {String} path, accessor is using dot notation.
     * @return {Object} value of obj[path]
     */
    var steps = path.split('.');
    var i = 0;
    while (i < steps.length && obj[steps[i]] !== undefined) {
        obj = obj[steps[i]];
        i += 1
    }
    if (i === steps.length) {
        return obj;
    }
    return undefined;
};
