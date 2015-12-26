'use strict';

var tpc = require('../../index')


describe('Two-Phase Commit Protocol', () => {

  it('should successfully process a transaction', (done) => {
    const cohort1 = new tpc.Cohort({host: 'localhost', port: 10001});
    const cohort2 = new tpc.Cohort({host: 'localhost', port: 10002});

    cohort1.listen()
    cohort2.listen()

    const coordinator = new tpc.Coordinator({
      cohorts: [
        {host: 'localhost', port: 10001},
        {host: 'localhost', port: 10002}
      ],
      transaction: {
        id: '123',
        params: '[1,2,3]'
      }
    });

    coordinator.process().then((success) => {
      done()
    }, (err) => {
      done(err);
    });
  });

});
