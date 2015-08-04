React = require('react');

Team = require('./Team.jsx')


var League = React.createClass({
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
                        <Team />
                        <Team />
                        <Team />
                        <Team />
                    </tbody>
                </table>
            </div>
        );
    }
});


module.exports = League;
