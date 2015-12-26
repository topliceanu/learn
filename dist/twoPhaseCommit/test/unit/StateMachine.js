const chai = require('chai');
const sinon = require('sinon');

const StateMachine = require('../../lib/StateMachine');


describe('StateMachine', () => {
  beforeEach(() => {
    this.sm = new StateMachine('initial', {
      'initial': {
        'state1': true
      },
      'state1': {
        'state1': true,
        'state2': true
      }
    });
  });

  it('should only allow predefined transitions', () => {
    changeToState2Spy = sinon.spy();
    this.sm.on('state2', changeToState2Spy);
    const hasChanged = this.sm.changeState('state2')

    chai.assert.isFalse(hasChanged,
      'should return false if the transition is not allowed');
    chai.assert.equal(this.sm.getState(), 'initial',
      'should have remained in the initial state');
    chai.assert.equal(changeToState2Spy.callCount, 0, 'should not be called');
  });

  it('should emit an event when a transition happens', () => {
    changeToState1Spy = sinon.spy();
    this.sm.on('state1', changeToState1Spy);
    const param = 123;
    this.sm.changeState('state1', param);

    chai.assert.equal(changeToState1Spy.callCount, 1,
      'should have emitted state1');
    chai.assert.equal(changeToState1Spy.args[0][0], 'initial',
      'first param is the previous state');
    chai.assert.equal(changeToState1Spy.args[0][1], param,
      'after that come all the other params');
  });
});
