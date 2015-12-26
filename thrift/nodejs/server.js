var thrift = require('thrift');

var UserStorage = require('./gen-nodejs/UserStorage');
var ttypes = require('./gen-nodejs/user_types');


var users = {}

var server = thrift.createServer(UserStorage, {
  store: function (user, result) {
    users[user.uid] = user;
    result(null);
  },

  retrieve: function (uid, result) {
    result(null, users[uid]);
  }
});

server.listen(9090, 'localhost');
