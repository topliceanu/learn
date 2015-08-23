React = require('react');


var TourDates = React.createClass({
    propTypes: {
        artistId: React.PropTypes.string.required
    },
    getInitialState: function () {
        return {
            shows: []
        };
    },
    componentWillMount: function () {
        if (!this.props.artistId) {
            return;
        }
        var that = this;
        getShows(this.props.artistId, function (shows) {
            that.setState({shows: shows});
        });
    },
    render: function () {
        if (this.state.shows.length > 0) {
            return (
                <div className="table-responsive">
                    <table className="table table-bordered">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Show</th>
                                <th>Venue</th>
                                <th>Location</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.state.shows.map(function (show) {
                                return <tr>
                                           <td>{show.date}</td>
                                           <td>{show.title}</td>
                                           <td>{show.venue}</td>
                                           <td>{show.location}</td>
                                       </tr>
                            })}
                        </tbody>
                    </table>
                </div>
            );
        }
        return (<span>Loading tour shows...</span>);
    }
});


module.exports = TourDates;
