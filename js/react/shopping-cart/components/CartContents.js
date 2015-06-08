import React from 'react'

import CartItem from './CartItem.js'


let CartContents = React.createClass({
    /*
    propTypes: {
        items: React.PropTypes.arrayOf(React.PropTypes.shape({
            id: React.PropTypes.any.isRequired,
            count: React.PropTypes.number,
            value: React.PropTypes.number,
            desc: React.PropTypes.string
        }))
    },
    */
    render () {
        let cartItems = this.props.items.map((index) => {
            let subView = this.props.subView(['items', index])
            return <CartItem key={index} ref={'item'+index} item={subView}/>
        });
        return (<div>{cartItems}</div>);
    }
});

export default CartContents;
