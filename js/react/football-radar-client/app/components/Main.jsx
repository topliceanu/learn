var React = require('react');

var League = require('./League.jsx');
var conf = require('../conf.js');


// Top-level component of the app UI.
// It handles the connection to the websocket server to update it's internal
// data model.
var Main = React.createClass({

    // Type check the part of the data model instance this component is
    // concerned about.
    propTypes: {
        data: React.PropTypes.shape({
            items: React.PropTypes.arrayOf(React.PropTypes.shape({
                id: React.PropTypes.number,
                name: React.PropTypes.string,
                played: React.PropTypes.number,
                won: React.PropTypes.number,
                drawn: React.PropTypes.number,
                lost: React.PropTypes.number,
                goalsFor: React.PropTypes.number,
                goalsAgainst: React.PropTypes.number,
                goalDifference: React.PropTypes.number,
                points: React.PropTypes.number
            }))
        })
    },

    // Initialize the component state from the props. It's a hack! but it
    // helps separate the data modeling from the data presentation.
    getInitialState: function () {
        return {items: this.props.data.items};
    },

    // Instance of window.WebSocket.
    socket: null,

    // Helper method to correctly format incomming event data from the
    // websocket notification server.
    format: function (update) {
        var output = JSON.parse(update);
        output.homeGoals = +output.homeGoals;
        output.awayGoals = +output.awayGoals;
        return output;
    },

    // Initialize the WebSocket connection when the component is just mounted.
    // Because this is the top-level component, it will only get injected once
    // per application life-cycle, thus making it the perfect place to initiate
    // the websockets connection.
    //
    // When an update is received via WS, the data model is updated and,
    // consequently the component state, which triggers a re-render.
    //
    // Note! No attempt has been made to account for browser inconsistencies
    // with regards to WebSocket API implementations.
    //
    // TODO handle socket errors!
    componentWillMount: function () {
        var that = this;
        this.socket = new WebSocket(conf.ws.url);
        this.socket.onmessage = function (event) {
            that.props.data.update(that.format(event.data));
            that.setState({items: that.props.data.items});
        }
    },

    // Cleanup component resources when it gets unmounted, in this case, close
    // the socket connection.
    componentWillUnmount: function () {
        this.socket.close();
    },

    // Simply render the League components which is the table.
    render: function () {
        return (
            <League data={this.state.items} />
        );
    }
});


module.exports = Main;
