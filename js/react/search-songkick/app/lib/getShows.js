var jquery = require('jquery');

var access = require('./access');


module.exports = function (artistId, callback) {
    /** Method fetches the shows data for a given artistId.
     * @param {String} artistId
     * @return {Array<Object>} format [{date, title, venue, location}]
     */
    return jquery.ajax({
        method: 'GET',
        url: 'http://api.songkick.com/api/3.0/artists/'+artistId+'/calendar.json',
        data: {
            'apikey': 'jhevSy2yQF6HFzmb'
        },
        dataType: 'jsonp',
        jsonp: 'jsoncallback'
    }).then(function (data) {
        if (!access(data, 'resultsPage.results.event.map')) {
            return callback([]);
        }
        var shows = data.resultsPage.results.event.map(function (event) {
            return {
                date: event.start.date+', '+event.start.time,
                title: event.displayName,
                venue: event.venue.displayName,
                location: event.location.city
            };
        });
        return callback(shows);
    }, function (__, status, error) {
        console.log('[error]', status, error.message);
        return callback([]);
    });
};
