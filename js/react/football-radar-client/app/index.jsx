var React = require('react');

var Main = require('./components/Main.jsx');
var DataModel = require('./lib/DataModel.js');
var getTeams = require('./lib/getTeams.js');
var conf = require('./conf.js');


var data = new DataModel();
var content = document.getElementById('content');


getTeams(conf.http.url, function (teams) {
    data.bootstrap(teams);
    React.render(<Main data={data}/>, content);
});
