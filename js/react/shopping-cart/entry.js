import React from 'react'
import {serialize, render} from 'react-component-tree'

import Cart from './components/Cart'


let items = [
    {
        id: 1,
        count: 1,
        value: 1000,
        desc: 'bike'
    },
    {
        id: 2,
        count: 1,
        value: 500,
        desc: 'suit'
    },
]

let container = document.getElementById('container')
let cart = React.render(<Cart items={items}/>, container);


// Export/Import state.
window._exportState = () => {
    return serialize(cart);
};
window._importState = (snapshot) => {
    render({
        component: Cart,
        snapshot: snapshot,
        container: container
    });
};
