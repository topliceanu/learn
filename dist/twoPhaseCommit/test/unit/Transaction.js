'use strict';

const chai = require('chai');

const Transaction = require('../../lib/Transaction');


describe('Transaction', () => {
  beforeEach(() => {
    this.tr = new Transaction('123', '[1,2,3]');
  });

  it('should not allow multiple query commands', () => {
    const message = 'should not accept query two times';
    this.tr.receive('query').then(() => {
      return this.tr.receive('query').then(() => {
        done(new Error(message));
      });
    }).catch((error) => {
      chai.assert.notEqual(error.message, message,
        'should not be the query twice error');
      done(error);
    });
  });

  it('should not allow commit without query before', () => {
    const message = 'should not commit when query was not executed before';
    this.tr.receive('commit').then(() => {
      done(new Error(message));
    }).catch((error) => {
      chai.assert.notEqual(error.message, message, 'should not accept commit')
    }).then(() => {
      done()
    }, (error) => {
      done(error)
    });
  });

  it('should not allow rollback without query before', () => {
    const message = 'should not rollback when query was not executed before';
    this.tr.receive('rollback').then(() => {
      done(new Error(message));
    }).catch((error) => {
      chai.assert.notEqual(error.message, message, 'should not accept rollback')
    }).then(() => {
      done()
    }, (error) => {
      done(error)
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
