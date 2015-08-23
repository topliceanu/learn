React = require('react');

getShows = require('../lib/getShows.js');
TourDates = require('./TourDates.jsx');


var ResultRow = React.createClass({
    propTypes: {
        artist: React.PropTypes.shape({
            id: React.PropTypes.string.required,
            name: React.PropTypes.string.required,
            url: React.PropTypes.string.required,
            isOnTour: React.PropTypes.string.required
        })
    },
    getInitialState: function () {
        return {
            showTourDates: false
        }
    },
    showTourDates: function () {
        var toggle = this.state.showTourDates === true ? false : true;
        this.setState({showTourDates: toggle});
    },
    render: function () {
        var displayShows, onTour;
        if (this.props.artist.isOnTour) {
            onTour = (<span>(on tour)</span>);
            if (this.state.showTourDates === true) {
                displayShows = (
                    <div>
                        <a onClick={this.showTourDates}>hide tour dates</a>
                        <TourDates artistId={this.props.artist.id}/>
                    </div>
                );
            }
            else {
                displayShows = (
                    <div>
                        <a onClick={this.showTourDates}>show tour dates</a>
                    </div>
                );
            }
        }
        else {
            onTour = (<span>(not touring)</span>);
            displayShows = (<span>No announced shows!</span>);
        }
        return (
            <li href="#" className="list-group-item">
                <h4 className="list-group-item-heading">{this.props.artist.name} {onTour}</h4>
                <p className="list-group-item-text">
                    <a href={this.props.artist.url}>Artist page on SongKick</a>
                </p>
                {displayShows}
            </li>
        );
    }
});


module.exports = ResultRow;
