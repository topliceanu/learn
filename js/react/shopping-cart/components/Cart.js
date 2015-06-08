import React from 'react'

import CartContents from './CartContents.js'
import CartTotal from './CartTotal.js'


let Cart = React.createClass({
    propTypes: {
        items: React.PropTypes.arrayOf(React.PropTypes.shape({
            id: React.PropTypes.any.isRequired,
            count: React.PropTypes.number,
            value: React.PropTypes.number,
            desc: React.PropTypes.string
        }))
    },
    getDefaultProps () {
        return {
            items: [],
        };
    },
    getInitialState () {
        return this.props
    },
    findItemById (itemId) {
        let found = this.state.items.filter((item) => {
            return item.id == itemId;
        });
        if (found !== undefined) {
            return found[0];
        }
    },
    incrementItem (itemId) {
        let item = this.findItemById(itemId);
        if (item === undefined) {
            return;
        }
        item.count += 1;
        this.setState({items: this.state.items});
    },
    decrementItem (itemId) {
        let item = this.findItemById(itemId);
        if (item === undefined) {
            return;
        }
        item.count -= 1;
        this.setState({items: this.state.items});
    },
    render () {
        return (<div>
                    <CartContents ref="contents" items={this.state.items} inc={this.incrementItem} dec={this.decrementItem}/>
                    <CartTotal ref="total" items={this.state.items}/>
                </div>);
    }
});

export default Cart;
