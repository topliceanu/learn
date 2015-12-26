var thrift = require('thrift');

var UserStorage = require('./gen-nodejs/UserStorage');
var ttypes = require('./gen-nodejs/user_types');


var connection = thrift.createConnection('localhost', 9090);
var client = thrift.createClient(UserStorage, connection);


var newUser = new ttypes.UserProfile({
  uid: 1,
  name: 'Alex',
  blurb: 'js programmer'
});


client.store(newUser, function (err, response) {
  if (err) {
    return console.log('error: ', err);
  }
  console.log('server stored new user ', response);

  client.retrieve(1, function (err, response) {
    if (err) {
      return console.log('error: ', err);
    }

    console.log('retrieved from server', response);
    connection.end();
  });
});
