var React = require('react');

var SearchBox = require('./SearchBox.jsx');
var SearchResults = require('./SearchResults.jsx');
var SearchStream = require('../lib/SearchStream.js');


var Main = React.createClass({
    searchStream: new SearchStream(),
    updateQueryString: function (query) {
        this.searchStream.input.push(query);
    },
    getInitialState: function () {
        return {
            artists: []
        };
    },
    componentWillMount: function () {
        var that = this;
        this.searchStream.output.onValue(function (results) {
            that.setState({artists: results});
        });
    },
    componentWillUnmount: function () {
        this.searchStream.output.end();
    },
    render: function () {
        return (
            <div className="container-fluid">
                <div className="row">
                    <div className="col-xs-12">
                        <h1>SongKick Artist Search</h1>
                    </div>
                </div>

                <SearchBox updateQueryString={this.updateQueryString}/>

                <div className="row">
                    <div className="col-xs-12">
                        <SearchResults artists={this.state.artists}/>
                    </div>
                </div>
            </div>
        );
    }
});


module.exports = Main;
