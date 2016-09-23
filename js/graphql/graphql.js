const crypto = require("crypto");

const graphql = require("graphql");
const expressGraphql = require("express-graphql");

const schema = graphql.buildSchema(`
  type RandomDie {
    numSides: Int!
    rollOnce: Int!
    roll(numRolls: Int!): [Int]
  }

  input MessageInput {
    content: String
    author: String
  }

  type Message {
    id: ID!
    content: String
    author: String
  }

  type Query {
    getDie(numSides: Int): RandomDie
    getMessage(id: ID!): Message
  }

  type Mutation {
    createMessage(input: MessageInput): Message
    updateMessage(id: ID!, input: MessageInput): Message
  }
`);

class Message {
  constructor(id, {content, author}) {
    this.id = id;
    this.content = content;
    this.author = author;
  }
}

class RandomDie {
  constructor (numSides) {
    this.numSides = numSides;
  }
  rollOnce () {
    return 1 + Math.floor(Math.random() * (this.numSides || 6));
  }
  roll ({numRolls}) {
    const output = [];
    for (let i = 0; i <= numRolls; i ++) {
      output.push(this.rollOnce());
    }
    return output;
  }
}

const db = {};
const rootValue = {
  getDie ({numSides}) {
    return new RandomDie(numSides || 6);
  },
  getMessage ({id}) {
    if (!db[id]) {
      throw new Error(`Cannot find message with id ${id}`);
    }
    return new Message(id, db[id]);
  },
  createMessage ({input}) {
    const id = crypto.randomBytes(10).toString("hex");
    db[id] = input;
    return new Message(id, input);
  },
  updateMessage ({id, input}) {
    if (!db[id]) {
      throw new Error(`Cannot find message with id ${id}`);
    }
    db[id] = input;
    return new Message(id, input);
  }
};

module.exports = expressGraphql({
  schema: schema,
  rootValue: rootValue,
  graphiql: true,
});
