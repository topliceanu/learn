App.QueryParam = React.createClass({
    propTypes: {
        filterKey: React.PropTypes.string,
        filterValue: React.PropTypes.string,
        removeFilter: React.PropTypes.func,
        updateFilter: React.PropTypes.func
    },
    removeFilter: function () {
        this.props.removeFilter(this.props.filterKey);
    },
    handleChangeKey: function (event) {
        var newKey = event.target.value;
        delete App.dataModel.query[this.props.filterKey]
        this.props.updateFilter(newKey, this.props.filterValue);
    },
    handleChangeValue: function () {
        var newValue = event.target.value;
        this.props.updateFilter(this.props.filterKey, newValue);
    },
    render: function () {
        return (
            <div className="row">
                <div className="col-sm-4">
                    <select className="form-control"
                        defaultValue={this.props.filterKey}
                        onChange={this.handleChangeKey.bind(this)}>
                            {App.dataModel.keys.map(function (key) {
                                return <option value={key}>{key}</option>
                            })}
                    </select>
                </div>
                <div className="col-sm-6">
                    <input type="text" className="form-control"
                           defaultValue={this.props.filterValue}
                           onChange={this.handleChangeValue.bind(this)}/>
                </div>
                <div className="col-sm-2">
                    <button type="submit" className="btn btn-danger"
                            onClick={this.removeFilter.bind(this)}>
                        Remove
                    </button>
                </div>
            </div>
        );
    }
});
