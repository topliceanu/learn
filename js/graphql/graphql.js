const crypto = require("crypto");

const graphql = require("graphql");
const expressGraphql = require("express-graphql");

const rootValue = require('./schema');

module.exports = expressGraphql({
  schema: schema,
  rootValue: rootValue,
  graphiql: true,
});
