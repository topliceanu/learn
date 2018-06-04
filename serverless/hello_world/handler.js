'use strict';

module.exports.helloWorld = (event, context, callback) => {
  const response = {
    statusCode: 200,
    headers: {
      'Access-Control-Allow-Origin': '*', // Required for CORS support to work
    },
    body: JSON.stringify({
      message: 'Go Serverless v1.0! Your function executed successfully!',
      input: event,
    }),
  };

  callback(null, response);
};

// static database, it might get removed.
var db = []

module.exports.create = (event, context, callback) => {
  const newID = db.length
  const {item, err} = parseBody(event)
  if (err) {
    return respond(callback, 400, err)
  }
  item.id = newID
  db[newID] = item
  respond(callback, 201, item)
}

module.exports.read = (event, context, callback) => {
  const id = event.pathParameters.id
  if (id >= db.length) {
    return respond(callback, 404, {})
  }
  const item = db[id]
  respond(callback, 200, item)
}

module.exports.replace = (event, context, callback) => {
  const id = event.pathParameters.id
  if (id >= db.length) {
    return respond(callback, 404, {})
  }
  const {item, err} = parseBody(event)
  if (err) {
    return respond(callback, 400, err)
  }
  item.id = id
  db[id] = item
  respond(callback, 200, item)
}

module.exports.delete = (event, context, callback) => {
  const id = event.pathParameters.id
  if (id >= db.length) {
    return respond(callback, 404, {})
  }
  db.splice(id, 1)
  respond(callback, 200, {})
}

module.exports.readall = (event, context, callback) => {
  respond(callback, 200, db)
}

// HELPERS

const parseBody = (event) => {
  try {
    const item = JSON.parse(event.body)
    return {item, err: null}
  } catch (err) {
    return {item: null, err: err}
  }
}

const respond = (callback, statusCode, body) => {
  callback(null, {
    statusCode: statusCode,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  })
}
