var os = require('os');

var _ = require('underscore');
var Q = require('q');


var send = function (socket, message, payload) {
    var data = JSON.stringify([message, payload])+os.EOL
    return Q.nfinvoke(socket, 'write', data)
};

var receive = function (socket, message) {
    var deferred = Q.defer();
    socket.on('data', function (data) {
        deferred.resolve(data);
    });
    socket.on('error', function (err) {
        deferred.reject(err);
    });
    return deferred.promise;
};


exports.send = send;
exports.receive = receive;





































/* Usage:
 *
 * var protocol =
 *      steps: [
 *              req:
 *                  name: 'sync-req'
 *                  payload:
 *                      id: 'int'
 *                      avg: 'float'
 *      ,
 *              res:
 *                  name: 'sync-res'
 *                  payload:
 *                      id: 'int'
 *                      avg: 'float'
 *      ]
 * };
 *
 * class MyProtocol extends Tcp {
 *      interaction () {
 *          this.on
 *      }
 * }
 *
 *
 * var client = new tcp.Peer(protocol, {client: true});
 * var server = new tcp.Peer(protocol, {server: true});
 *
 * client.send('sync-req', () => {
 *      client.write({'id': this.id, avg: this.avg});
 * })
 *
 * server.on('sync-req', (data) => {
 *      if (data.id > this.id) {
 *          this.id = data.id;
 *      }
 *      that.avg = (data.avg + this.avg) / 2
 * });
 * server.send('sync-res', () => {
 *      server.write({id: this.id, avg: this.avg});
 * });
 * client.on('sync-res', (data) => {
 *      this.id = data.id;
 *      this.avg = data.avg;
 * });
 *
 */


import * as net from 'net'


class Tcp extends net.Socket{

}
