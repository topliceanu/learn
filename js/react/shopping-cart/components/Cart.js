import React from 'react'

import CartContents from './CartContents.js'
import CartTotal from './CartTotal.js'


let Cart = React.createClass({
    render () {
        return (<div>
                    <CartContents ref="contents" items={this.state.items} inc={this.incrementItem} dec={this.decrementItem}/>
                    <CartTotal ref="total" items={this.state.items}/>
                </div>);
    }
});

export default Cart;
