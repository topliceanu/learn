var log = function (tag, err) {
    /** Utility method just to get better formating from errors and other
    * log messages
    * @param {String} tag
    * @param {Object} err
    */
    if (tag === 'error') {
        console.log('['+tag+']['+(new Date)+']')
        console.log(err.message);
        console.log(err.stack);
    }
    else {
        console.log('['+tag+']['+(new Date)+']')
        console.log(err);
    }
};


exports.log = log;
