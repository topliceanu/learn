const express = require("express");

const auth = require("./auth");
const graphql = require("./graphql");

const app = express();
app.use("/graphql", auth(USER, PASS), graphql);
app.listen(4000, "0.0.0.0", () => {
  console.log("Server started. Go to http://0.0.0.0:4000/graphql");
});
