import React from 'react'


let CartItemTotal = React.createClass({
    propTypes: {
        count: React.PropTypes.number,
        value: React.PropTypes.number
    },
    getDefaultProps () {
        return {
            count: 0,
            value: 0
        };
    },
    computePrice () {
        return this.props.count * this.props.value;
    },
    render () {
        return (<div>{this.computePrice()}</div>);
    }
});

export default CartItemTotal;
