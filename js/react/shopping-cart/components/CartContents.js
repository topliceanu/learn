import React from 'react'

import CartItem from './CartItem.js'


let CartContents = React.createClass({
    propTypes: {
        items: React.PropTypes.arrayOf(React.PropTypes.shape({
            id: React.PropTypes.any.isRequired,
            count: React.PropTypes.number,
            value: React.PropTypes.number,
            desc: React.PropTypes.string
        })),
        inc: React.PropTypes.func.isRequired,
        dec: React.PropTypes.func.isRequired,
    },
    getDefaultProps () {
        return {
            items: []
        };
    },
    render () {
        let cartItems = this.props.items.map((item, index) => {
            return <CartItem ref={'item'+index} item={item} key={index} inc={this.props.inc} dec={this.props.dec}/>
        });
        return (<div>{cartItems}</div>);
    }
});

export default CartContents;
