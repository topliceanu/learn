'use strict';

let Coordinator = require('../../lib/Coordinator');
let Cohort = require('../../lib/Cohort');
let Transaction = require('../../lib/Transaction');


describe('Two-Phase Commit Protocol', () => {
  beforeEach(() => {
    this.cohort1 = new Cohort({host: 'localhost', port: 10001});
    this.cohort2 = new Cohort({host: 'localhost', port: 10002});
    this.transaction = new Transaction([1,2,3,4]);
    this.coordinator = new Coordinator(this.transaction, [this.cohort1, this.cohort2]);
  });

  it('should continue to completion if the voting yields success', (done) => {
    this.coordinator.process().then(() => {
      done()
    }, (error) => {
      done(error);
    })
  });

  it('should stop the transaction if the at least on cohort votes no', (done) => {
  });
});
