"use strict";


class Cohort {
  constructor (options) {
    /* @param {Object} options
     * @param {Object} options.host
     * @param {Object} options.port
     * @param {Function} options.transactionFactory
     * @param {Function} options.thriftServerFactory
     */
    this.port = options.port;
    this.host = options.host;
    this.currentTransactions = new Map(); // tid -> state machine.
    this.transactionFactory = options.transactionFactory;
    this.server = options.thriftServerFactory({
      queryToCommit: this.queryToCommit.bind(this),
      commit: this.commit.bind(this),
      rollback: this.rollback.bind(this)
    });
  }

  queryToCommit (tid, tbody, result) {
    if (!this.currentTransactions.has(tid)) {
      this.currentTransactions.set(tid, this.transactionFactory(tid, tbody));
    }
    return this._processMessage(tid, 'query', result);
  }

  commit (tid, result) {
    return this._processMessage(tid, 'commit', result)
               .then(this._removeTransaction(tid))
  }

  rollback (tid, result) {
    return this._processMessage(tid, 'rollback', result)
               .then(this._removeTransaction(tid));
  }

  _processMessage (tid, messageType, result) {
    if (!this.currentTransactions.has(tid)) {
      return result(new Error(`Unknown transaction with ${tid}`));
    }
    this.currentTransactions.get(tid).receive(messageType).then((response) => {
      result(null, response);
    }, (error) => {
      result(error);
    });
  }

  _removeTransaction (tid) {
    return () => {
      this.currentTransactions.delete(tid);
      return Promise.resolve(true);
    }
  }
}


module.exports = Cohort;
