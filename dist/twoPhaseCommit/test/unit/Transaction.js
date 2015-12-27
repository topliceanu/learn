'use strict';

const Transaction = require('../../lib/Transaction');


describe('Transaction', () => {
  beforeEach(() => {
    this.tr = new Transaction('123', '[1,2,3]');
  });

  it('should not allow multiple query commands', () => {
    this.tr.receive('query').then(() => {
      this.tr.receive('query').then(() => {
        done(new Error('should not accept query two times'));
      });
    }).catch((error) => {
      done(error);
    });
  });

  it('should not allow commit without query before', () => {
    this.tr.receive('commit').then(() => {
      done(new Error('should not commit when query was not executed before'));
    }, (error) => {
      done()
    });
  });

  it('should not allow rollback without query before', () => {
    this.tr.receive('commit').then(() => {
      done(new Error('should not rollback when query was not executed before'));
    }, (error) => {
      done()
    });
  });

  it('should not allow rollback to a commited state', () => {
    this.tr.receive('query').then(() => {
      this.tr.receive('commit').then(() => {
        this.tr.receive('rollback').then(() => {
          done(new Error('should not be allowed to rollback after commit'));
        }, (error) => {
          done();
        });
      });
    }).catch((error) => {
      done(error);
    });
  });
});
