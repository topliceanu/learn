'use strict';

const thrift = require('thrift');

const TPC = require('./thrift/TPC');


class Coordinator {
  constructor (options) {
    this.cohorts = options.cohorts.map((address) => {
      const con = thrift.createConnection(address.host, address.port);
      return thrift.createClient(TPC, con);
    });
  }

  process (transaction) {
    return this._voting(transaction).then((doCommit) => {
      if (doCommit === true) {
        return this._completionSuccess(transaction)
      }
      return this._completionFailure(transaction)
    });
  }

  // @return {Promise} resolves to Boolean
  _voting (transaction) {
    return Promise.all(this.cohorts.map((cohort) => {
      return this._queryToCommit(cohort, transaction);
    })).then((responses) => {
      const doCommit = responses.every((response) => { return response === true });
      return Promise.resolve(doCommit);
    });
  }

  _completionSuccess (transaction) {
    return Promise.all(this.cohorts.map((cohort) => {
      return this._commit(cohort, transaction);
    })).then((responses) => {
      const acked = responses.every((response) => { return response === true });
      return Promise.resolve(acked)
    });
  }

  _completionFailure (transaction) {
    return Promise.all(this.cohorts.map((cohort) => {
      return this._rollback(cohort, transaction);
    })).then((responses) => {
      const acked = responses.every((response) => { response === true });
      return Promise.resolve(acked);
    });
  }

  // @return {Promise} resolves to Boolean.
  _queryToCommit(cohort, transaction) {
    return new Promise(function (resolve, reject) {
      cohort.queryToCommit(transaction.id, transaction.params, (err, response) => {
        if (err) return reject(err);
        return resolve(response);
      });
    });
  }

  // @return {Promise} resolves to Boolean.
  _commit(cohort, transaction) {
    return new Promise(function (resolve, reject) {
      cohort.commit(transaction.id, function (err, response) {
        if (err) return reject(err);
        return resolve(response);
      });
    });
  }

  // @return {Promise} resolves to Boolean.
  _rollback(cohort, transaction) {
    return new Promise(function (resolve, reject) {
      cohort.rollback(transaction.id, function (err, response) {
        if (err) return reject(err);
        return resolve(response);
      });
    });
  }
}


module.exports = Coordinator;
