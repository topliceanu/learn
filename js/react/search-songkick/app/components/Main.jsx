var React = require('react');

var SearchBox = require('./SearchBox.jsx');
var SearchResults = require('./SearchResults.jsx');
var SearchStream = require('../lib/SearchStream.js');


var Main = React.createClass({
    /** Main React component. It handles the fetching of query results for the
     * artists that match. Delegates rendering of results to SearchResults and
     * handling the input to SearchBox components.
     */
    searchStream: new SearchStream(),
    updateQueryString: function (query) {
        /** Wheever the user updates the value of the input field, the
         * searchStream gets an update. This will trigger an ajax request, whose
         * response is directed to the output stream.
         * @see .componentWillMount()
         */
        this.searchStream.input.push(query);
    },
    getInitialState: function () {
        return {
            artists: []
        };
    },
    componentWillMount: function () {
        /** Method reacts to responses from the ajax endpoints by updating
         * the state of the component with the appropriate results
         */
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
