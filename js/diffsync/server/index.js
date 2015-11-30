var Peer = require('../peer');


class Server {
  constructor () {
    this.peers = {};
  }

  addPeer (peer) {
    this.peers[peer.uuid] = peer;
  }
}
