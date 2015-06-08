import React from 'react'
import {serialize, render} from 'react-component-tree'
import * as Immutable from 'immutable'

import Cart from './components/Cart.js'
import Truth from './lib/Truth.js'


let rawItems = [
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
let container = document.getElementById('container');


let app = new Truth(rawItems, Cart, container);
app.render()
