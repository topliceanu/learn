import React from 'react'


let CartItemDescription = React.createClass({
    propTypes: {
        desc: React.PropTypes.string
    },
    getDefaultProps () {
        return {
            desc: ''
        };
    },
    render () {
        return (<div>{this.props.desc}</div>);
    }
});

export default CartItemDescription;
