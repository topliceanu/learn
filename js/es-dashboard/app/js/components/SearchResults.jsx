App.SearchResults = React.createClass({
    render: function () {
        return (
            <div className="row">
                <div className="col-sm-12">
                    <ul className="list-group">
                        {this.props.results.map(function (item, index) {
                            return <App.SearchResult key={item._id} data={item}/>
                        })}
                    </ul>
                </div>
            </div>
        );
    }
});
