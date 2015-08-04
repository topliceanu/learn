var React = require('react')


var Team = React.createClass({
    propTypes: {
        data: React.PropTypes.shape({
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
        })
    },

    render: function () {
        return (
            <tr>
                <td>{this.props.position + 1}</td>
                <td>{this.props.data.name}</td>
                <td>{this.props.data.played}</td>
                <td>{this.props.data.won}</td>
                <td>{this.props.data.drawn}</td>
                <td>{this.props.data.lost}</td>
                <td>{this.props.data.goalsFor}</td>
                <td>{this.props.data.goalsAgainst}</td>
                <td>{this.props.data.goalDifference}</td>
                <td>{this.props.data.points}</td>
            </tr>
        );
    }
});


module.exports = Team;
