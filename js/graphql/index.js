const express = require("express");

const auth = require("./auth");
const graphql = require("./graphql");

const USER = 'user';
const PASS = 'pass';
const PORT = 4000;
const HOST = '0.0.0.0';

const app = express();
app.use("/graphql", auth(USER, PASS), graphql);
app.listen(PORT, HOST, () => {
  console.log(`Server started. Go to http://${HOST}:${PORT}/graphql`);
});
