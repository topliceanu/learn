curl -XPOST http://192.168.33.11:9200/test_companies/company/_search?pretty=true -d '{
    "size": 2,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "name": "wellington"
                    }
                },
                {
                    "match": {
                        "bank": "hsbc"
                    }
                },
                {
                    "nested": {
                        "path": "descriptions",
                        "query": {
                            "match": {
                                "value": "awesome company"
                            }
                        }
                    }
                },
                {
                    "nested": {
                        "path": "contacts",
                        "query": {
                            "multi_match": {
                                "query": "Church",
                                "fields": ["first_name", "last_name", "title", "phone", "role", "email", "title", "url", "director"]
                            }
                        }
                    }
                },
                {
                    "nested": {
                        "path": "addresses",
                        "query": {
                            "multi_match": {
                                "query": "Church",
                                "fields": ["address_line_1", "address_line_2", "address_line_3", "address_line_4", "county", "postcode"]
                            }
                        }
                    }
                },
                {
                    "nested": {
                        "path": "tokens",
                        "query": {
                            "match": {
                                "value": "COURT"
                            }
                        }
                    }
                }
            ]
        }
    }
}'
