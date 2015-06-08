import React from 'react'


let CartTotal = React.createClass({
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
            items: []
        }
    },
    computeTotal () {
        return this.props.items.reduce((collector, item) => {
            return collector + item.count * item.value;
        }, 0)
    },
    render () {
        return (<div>Total: {this.computeTotal()}</div>);
    }
});


export default CartTotal;
