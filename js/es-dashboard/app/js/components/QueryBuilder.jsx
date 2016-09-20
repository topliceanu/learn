App.QueryBuilder = React.createClass({
    propTypes: {
        filters: React.PropTypes.object,
        addFilter: React.PropTypes.func,
        removeFilter: React.PropTypes.func,
        updateFilter: React.PropTypes.func,
    },
    getDefaultProps: function () {
        return {
            filters: {}
        };
    },
    addFilter: function () {
        var remainingKeys = [];
        App.dataModel.keys.forEach(function (key) {
            if (this.props.filters[key] === undefined) {
                remainingKeys.push(key);
            }
        }, this);
        if (remainingKeys.length !== 0) {
            this.props.addFilter(remainingKeys[0], '');
        }
    },
    render: function () {
        var output = (
            <div className="row well">
                <div className="col-sm-12">
                    {Object.keys(this.props.filters).map(function (key) {
                        return <App.QueryParam filterKey={key}
                            filterValue={this.props.filters[key]}
                            removeFilter={this.props.removeFilter}
                            updateFilter={this.props.updateFilter} />
                    }, this)}
                    <div className="row">
                        <div className="col-sm-2 col-sm-offset-4">
                            <button className="btn btn-default" type="button"
                                    onClick={this.addFilter.bind(this)}>Add Filter</button>
                        </div>
                    </div>

                </div>
            </div>
        );
        return output;
    }
});
