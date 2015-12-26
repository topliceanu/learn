'use strict';

var chai = require('chai');

var tpc = require('../../index');


describe('Two-Phase Commit Protocol', () => {

  beforeEach(() => {
    this.cohort1 = new tpc.Cohort({host: 'localhost', port: 10001});
    this.cohort2 = new tpc.Cohort({host: 'localhost', port: 10002});

    this.cohort1.listen()
    this.cohort2.listen()
  });

  it('should successfully process a transaction', (done) => {
    const coordinator = new tpc.Coordinator({
      cohorts: [
        {host: 'localhost', port: 10001},
        {host: 'localhost', port: 10002}
      ]
    });

    const transaction = {
      id: '123',
      params: '[1,2,3]'
    };
    coordinator.process(transaction).then((commited) => {
      chai.assert.isTrue(commited, 'should have commited the transaction');
      done();
    }, (err) => {
      done(err);
    });
  });

  it('should abort a transaction when one cohort fails', (done) => {
    const coordinator = new tpc.Coordinator({
      cohorts: [
        {host: 'localhost', port: 10001},
        {host: 'localhost', port: 10002}
      ]
    });
    const transaction = {
      id: '123',
      params: 'fail!'
    };

    coordinator.process(transaction).then((commited) => {
      chai.assert.isFalse(commited, 'should have failed the transaction');
    }).then(() => {
      done();
    }, (err) => {
      done(err);
    });
  });

  it('should process multiple transactions at the same time', (done) => {
    const coordinator = new tpc.Coordinator({
      cohorts: [
        {host: 'localhost', port: 10001},
        {host: 'localhost', port: 10002}
      ]
    });
    const successfullTransaction = {
      id: '123',
      params: '[1,2,3,4]'
    };
    const failureTransaction = {
      id: '123',
      params: 'fail!'
    };

    Promise.all([
      coordinator.process(successfullTransaction),
      coordinator.process(failureTransaction)
    ]).then((results) => {
      chai.assert.isTrue(results[0], 'should have succeeded the transaction');
      chai.assert.isFalse(results[1], 'should have failed the transaction');
    }).then(() => {
      done();
    }, (err) => {
      done(err);
    });
  });

  afterEach(() => {
    this.cohort1.close()
    this.cohort2.close()
  });
});
