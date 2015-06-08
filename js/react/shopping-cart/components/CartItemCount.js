import React from 'react'


let CartItemCount = React.createClass({
    /*
    propTypes: {
        itemId: React.PropTypes.any.isRequired,
        count: React.PropTypes.number,
        inc: React.PropTypes.func.isRequired,
        dec: React.PropTypes.func.isRequired
    },
    */
    onIncClick () {
        let currentCount = this.props.getIn(['count']);
        this.props.setIn(['count'], currentCount + 1);
    },
    onDecClick () {
        let currentCount = this.props.getIn(['count']);
        this.props.setIn(['count'], currentCount - 1);
    },
    render () {
        return (
            <div>
                <button onClick={this.onIncClick}> + </button>
                <div>{this.props.count}</div>
                <button onClick={this.onDecClick}> - </button>
            </div>
        );
    }
});


export default CartItemCount;
