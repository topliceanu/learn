'use strict';

const chai = require('chai');
const sinon = require('sinon');

const Cohort = require('../../lib/Cohort');


describe('Cohort', () => {
  it('should handle multiple transactions at the same time', (done) => {
    const result = sinon.spy()
    const thriftServer = {
      methods: {},
      call (method, params) {
        this.methods[method].apply(null, params);
      }
    };
    const thriftServerFactory = (methods) => {
      Object.keys(methods).forEach((name) => {
        thriftServer.methods[name] = methods[name]
      });
    };
    const fakeTransaction1 = ({ receive: sinon.spy() });
    const fakeTransaction2 = ({ receive: sinon.spy() });

    const cohort = new Cohort({
      transactionFactory: (tid, tbody) => {
        if (tid === '1') return fakeTransaction1;
        else if (tid === '2') return fakeTransaction2;
      },
      thriftServerFactory: thriftServerFactory
    });

    thriftServer.call('queryToCommit', ['1', '[1,2]']);
  });
});
