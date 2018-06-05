'use strict';

const AWS = require('aws-sdk')

let id = 1
const db = new AWS.DynamoDB.DocumentClient()

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

module.exports.create = (event, context, callback) => {
  const {item, err} = parseBody(event)
  if (err) {
    return respond(callback, 400, err)
  }
  id = id + 1
  item.id = ''+id
  db.put({
    TableName: process.env.DYNAMODB_TABLE,
    ITEM: item,
  }, (err) => {
    if (err) {
      return respond(callback, 500, err)
    }
    respond(callback, 201, item)
  })
}

module.exports.delete = (event, context, callback) => {
  const id = event.pathParameters.id
  db.delete({
    TableName: process.env.DYNAMODB_TABLE<
    KEY: {
      id: id,
    },
  }, (err) => {
    if (err) {
      return respond(callback, 500, err)
    }
    respond(callback, 200, {})
  })
}

module.exports.readall = (event, context, callback) => {
  db.scan({
    TableName: process.env.DYNAMODB_TABLE,
  }, (err, result) => {
    if (err) {
      return respond(callback, 500, err)
    }
    return respond(callback, 200, result.Items)
  })
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
