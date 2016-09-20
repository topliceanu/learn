var DataModel = function () {
    /**
     * @param Object<String, String> the token included in the query.
     */
    this.query = {};
    this.keys = ['name', 'bank', 'descriptions', 'contacts', 'addresses', 'tokens']
    this.esClient = new elasticsearch.Client({
        host: App.conf.es.host
    });
};

DataModel.prototype.setQueryKey = function (key, value) {
    if (this.keys.indexOf(key) === -1) {
        throw new Error('This key is not allowed '+key);
    }
    this.query[key] = value;
};

DataModel.prototype.removeQueryKey = function (key) {
    delete this.query[key];
};

DataModel.prototype.getRemainingKeys = function () {
    var that = this;
    return this.keys.filter(function (key) {
        return that.query[key] === undefined;
    });
};

DataModel.prototype.buildQuery = function () {
    /** Builds the exact query for the elastic search.
    * @return {Object}
    */
    var query = {
        "bool": {
            "should": []
        }
    };
    var that = this;
    Object.keys(this.query).forEach(function (key) {
        if (key === 'name') {
            query.bool.should.push({
                "match": {
                    "name": that.query[key]
                }
            });
        }
        else if (key === 'bank') {
            query.bool.should.push({
                "match": {
                    "bank": that.query[key]
                }
            });
        }
        else if (key === 'descriptions') {
            query.bool.should.push({
                "nested": {
                    "path": "descriptions",
                    "query": {
                        "match": {
                            "value": that.query[key]
                        }
                    }
                }
            });
        }
        else if (key === 'contacts') {
            query.bool.should.push({
                "nested": {
                    "path": "contacts",
                    "query": {
                        "multi_match": {
                            "query": that.query[key],
                            "fields": ["first_name", "last_name", "title", "phone", "role", "email", "title", "url", "director"]
                        }
                    }
                }
            });
        }
        else if (key === 'addresses') {
            query.bool.should.push({
                "nested": {
                    "path": "addresses",
                    "query": {
                        "multi_match": {
                            "query": that.query[key],
                            "fields": ["address_line_1", "address_line_2", "address_line_3", "address_line_4", "county", "postcode"]
                        }
                    }
                }
            });
        }
        else if (key === 'tokens') {
            query.bool.should.push({
                "nested": {
                    "path": "tokens",
                    "query": {
                        "match": {
                            "value": that.query[key]
                        }
                    }
                }
            });
        }
    });
    return query;
};

DataModel.prototype.fetchData = function (query) {
    /** */
    return this.esClient.search({
        index: App.conf.es.index,
        type: App.conf.es.type,
        body: {
            'query': query
        }
    });
};


App.dataModel = new DataModel();
