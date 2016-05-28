var Bacon = require('baconjs');
var jquery = require('jquery');

var access = require('./access.js');


var SearchStream = function () {
    /** Search stream class transforms a stream of string coming from the test
     * field into a stream of result arrays containing artist data whose name
     * match the strings.
     */
    this.input = new Bacon.Bus();
    var middle = this.input.debounce(100);//.skipDuplicates();
    this.output = middle.flatMapLatest(this.doSearch);
};

SearchStream.prototype.doSearch = function (query) {
    /** Given a query string return a list of artist objects.
     * @param {String} query
     * @return {Object} Promise resovles to a list with format [{id, name, url, isOnTour}]
     */
    if (query.length < 3) {
        return Bacon.once([]);
    }
    return Bacon.fromPromise(jquery.ajax({
        method: 'GET',
        url: 'http://api.songkick.com/api/3.0/search/artists.json',
        data: {
            query: query,
            apikey: 'jhevSy2yQF6HFzmb'
        },
        dataType: 'jsonp',
        jsonp: 'jsoncallback'
    }).then(function (data) {
        if (!access(data, 'resultsPage.results.artist.map')) {
            return [];
        }

        var results = data.resultsPage.results.artist.map(function (artist) {
            return {
                id: artist.id,
                name: artist.displayName,
                url: artist.uri,
                isOnTour: artist.onTourUntil !== null
            };
        });
        return results;
    }));
};


module.exports = SearchStream;
