"use strict";


class Document {
  constructor (text = '') {
    this.n = 0; // current version.
    this.m = 0; // remote version.
    this.text = text; // document text.
  }
}

class Diff {
  constructor (doc1, doc2) {
    this.doc1 = doc1;
    this.doc2 = doc2;
  }

  extract () {
    // Format [[edit, position]]
    // Eg [['+a', 12], ['-bc', 20]]
    return [];
  }
}

class Patch {
  constructor (diff) {
    this.diff = diff;
  }

  apply (doc) {
    doc += this.diff
  }
}

class StrictPatch extends Patch {}
class FuzzyPatch extends Patch {}

class Peer {
  constructor () {
    this.doc = new Document();
    this.shaddow = new Document();
    this.backup = new Document();
    this.edits = []
  }
}


let clientShaddow = new Shaddow();
let clientLiveCopy = new Copy();
let clientBackupShaddow = new Shaddow();
let clientEditsStack = [];
let nClient = 0; // client version number stored on the client.
let mClient = 0; // server version number stored on the client.

let serverShaddow = new Shaddow();
let serverLiveCopy = new Copy();
let serverBackupShaddow = new Shaddow();
let serverEditsStack = [];
let nServer = 0; // client version number strored on the server.
let mServer = 0; // server version number stored on the server.

client.on('change', () => {
  let clientEdits = diff(clientLiveCopy, clientShaddow); // 1. compute edists
  clientShaddow.replaceContent(clientLiveCopy); // 2. replace shaddow content.
  let checksum = clientShaddow.checksum(); // 2.1. extract checksum of the client shaddow.
  sendToServer(clientEdits, checksum, nClient, mClient); // 3. send edits, checksum and client-side, and server-side version.
  nClient += 1 // 4. after sending we increment the client's version.
});

server.on('edits', (clientEdits, checksum, nReceived, mReceived) => {
  try {
    // 4. Apply edits to the server's shaddow (which should be in sync with the
    // client shaddow, hence the different patch).
    if (nReceived === nServer && mReceived == mServer) {
      exactPatch(serverShaddow, clientEdists);
      nServer += 1
    }
    else {
      throw new Error('Server shaddow not in sync with the client version')
    }
    if (checksum != serverShaddow.checksum()) { // 4.1. verify the checksum of the pattern.
      throw new Error('Failed checksum of the server shaddow');
    }
    // 5. Apply edists to server copy.
    fuzzyPatch(serverLiveCopy, clientEdits);
    // 6. Update the backup shaddow
    exactPath(serverBackupShaddow, clientEdits)
  }
  catch (exception) {
    console.log('Fuzzy patch failed', exception);
  }
  let serverEdits = diff(serverLiveCopy, serverShaddow, nServer, mServer); // 5. extract edits from the server.
  sendToClient(serverEdits);
  mServer += 1
});

client.on('edits', (serverEdits) => {
  try {
    fuzzyPatch(clientLiveCopy, serverEdits);
  }
  catch (exception) {
    console.log('Fuzzy patch failed', exception);
  }
});
