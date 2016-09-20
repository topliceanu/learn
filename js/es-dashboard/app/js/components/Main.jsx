App.Main = React.createClass({
    getInitialState: function () {
        return {
            filters: {},
            results: []
        };
    },

    addFilter: function (key, value) {
        App.dataModel.setQueryKey(key, value);
        this.setState({filters: App.dataModel.query});
    },

    removeFilter: function (key) {
        App.dataModel.removeQueryKey(key);
        this.setState({filters: App.dataModel.query});
    },

    updateFilter: function (key, value) {
        App.dataModel.query[key] = value;
        this.setState({filters: App.dataModel.query});
    },

    handleSearch: function () {
        var that = this;
        var query = App.dataModel.buildQuery()
        App.dataModel.fetchData(query).then(function (res) {
            that.setState({results: res.hits.hits});
        });
    },

    render: function () {
        return (
            <div className="container">

                <div className="row">
                    <div className="col-sm-12">
                        <h1>Companies Search</h1>
                    </div>
                </div>

                {/* query building section */}
                <App.QueryBuilder filters={this.state.filters}
                    addFilter={this.addFilter.bind(this)}
                    removeFilter={this.removeFilter.bind(this)}
                    updateFilter={this.updateFilter.bind(this)}/>
                {/* end query building section */}

                <div className="row">
                    <div className="col-sm-2 col-sm-offset-4">
                        <button className="btn btn-lg btn-primary" type="button"
                            onClick={this.handleSearch.bind(this)}>
                            Search
                        </button>
                    </div>
                </div>

                {/* search results section */}
                <div className="row">
                    <div className="col-sm-12">
                        <h3>Results</h3>
                    </div>
                </div>

                {<App.SearchResults results={this.state.results}/>}
                {/* end search results section */}

            </div>
        );
    }
});
