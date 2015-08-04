var React = require('react');

var League = require('./League.jsx');
var conf = require('../conf.js');


var Main = React.createClass({
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

    getInitialState: function () {
        return {items: this.props.data.items};
    },

    socket: null,

    format: function (update) {
        var output = JSON.parse(update);
        output.homeGoals = +output.homeGoals;
        output.awayGoals = +output.awayGoals;
        return output;
    },

    componentWillMount: function () {
        var that = this;
        this.socket = new WebSocket(conf.ws.url);
        this.socket.onmessage = function (event) {
            that.props.data.update(that.format(event.data));
            that.setState({items: that.props.data.items});
        }
    },

    componentWillUnmount: function () {
        this.socket.close();
    },

    render: function () {
        return (
            <League data={this.state.items} />
        );
    }
});


module.exports = Main;
