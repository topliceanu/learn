var React = require('react');

var Main = require('./components/Main.jsx');
var DataModel = require('./lib/DataModel.js');
var getTeams = require('./lib/getTeams.js');
var conf = require('./conf.js');


var data = new DataModel();
var content = document.getElementById('content');


// Fetch teams json data, bootstrap the data model and start rendering the app.
getTeams(conf.http.url, function (teams) {
    data.bootstrap(teams);
    React.render(<Main data={data}/>, content);
});
