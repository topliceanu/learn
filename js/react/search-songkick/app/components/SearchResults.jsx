var React = require('react');

var ResultRow = require('./ResultRow.jsx');


var SearchResults = React.createClass({
    propTypes: {
        artists: React.PropTypes.arrayOf(React.PropTypes.shape({
            id: React.PropTypes.string.id,
            name: React.PropTypes.string.required,
            url: React.PropTypes.string.required,
            isOnTour: React.PropTypes.string.required
        }))
    },
    render: function () {
        return (
            <ul className="list-group">
                {this.props.artists.map(function (artist) {
                    return <ResultRow key={artist.id} artist={artist}/>
                })}
            </ul>
        );
    }
});


module.exports = SearchResults
