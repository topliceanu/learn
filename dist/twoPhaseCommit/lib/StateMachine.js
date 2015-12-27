'use strict';

var events = require('events');


class StateMachine extends events.EventEmitter {
  constructor (initialState, transitions) {
    super();
    this.state = initialState;
    this.transitions = transitions;
  }

  getState () {
    return this.state;
  }

  changeState (newState) {
    if (!this.transitions[this.state] || !this.transitions[this.state][newState]) {
      return false;
    }
    const args = [newState, this.state].concat([].slice.call(arguments, 1))
    this.state = newState;
    this.emit.apply(this, args);
  }
}


module.exports = StateMachine;
