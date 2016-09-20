App.SearchResult = React.createClass({
    render: function () {
        return (
            <li className="list-group-item" href="">
                <span>{this.props.data._source.name}</span>
            </li>
        );
    }
});
