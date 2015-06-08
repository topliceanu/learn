import React from 'react'


let CartItemCount = React.createClass({
    propTypes: {
        itemId: React.PropTypes.any.isRequired,
        count: React.PropTypes.number,
        inc: React.PropTypes.func.isRequired,
        dec: React.PropTypes.func.isRequired
    },
    getDefaultProps () {
        return {
            count: 0
        };
    },
    onIncClick () {
        this.props.inc(this.props.itemId);
    },
    onDecClick () {
        this.props.dec(this.props.itemId);
    },
    render () {
        return (<div>
                    <button onClick={this.onIncClick}>+</button>
                    <div>{this.props.count}</div>
                    <button onClick={this.onDecClick}>-</button>
                </div>);
    }
});

export default CartItemCount;
