var React = require('react');


var SearchBox = React.createClass({
    /** Component captures the value of the text input field and passes it to
     * the parent component.
     */
    propTypes: {
        updateQueryString: React.PropTypes.func.required
    },
    getInitialState: function () {
        return {
            value: ''
        };
    },
    handleChange: function (event) {
        this.setState({value: event.target.value});
        this.props.updateQueryString(this.state.value);
    },
    render: function () {
        return (
            <div className="row">
                <div className="col-xs-12">
                    <form>
                        <div className="form-group">
                            <input type="text" className="form-control"
                                value={this.state.value}
                                onChange={this.handleChange}/>
                        </div>
                    </form>
                </div>
            </div>
        );
    }
});


module.exports = SearchBox;
