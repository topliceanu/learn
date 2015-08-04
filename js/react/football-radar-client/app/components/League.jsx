var React = require('react');

var Team = require('./Team.jsx')


var League = React.createClass({
    // This component only renders the actual table with all the teams and their
    // scores, sorting is handled in the parent component by it's DataModel
    // instance.
    // This is a stateless component, which receives all it's data from it's
    // parent, ie. a plain js array with team objects.
    propTypes: {
        data: React.PropTypes.arrayOf(React.PropTypes.shape({
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
    },

    // Render the table with all the teams and their scores.
    render: function () {
        return (
            <div className="table-responsive">
                <table className="table table-condensed table-hover">
                    <thead>
                        <tr>
                            <th>Pos</th>
                            <th>Team</th>
                            <th>Played</th>
                            <th>Won</th>
                            <th>Drawn</th>
                            <th>Lost</th>
                            <th>Goals For</th>
                            <th>Goals Against</th>
                            <th>Goal Difference</th>
                            <th>Points</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.data.map(function (item, index) {
                            return <Team key={item.id} data={item} position={index}/>
                        })}
                    </tbody>
                </table>
            </div>
        );
    }
});


module.exports = League;
