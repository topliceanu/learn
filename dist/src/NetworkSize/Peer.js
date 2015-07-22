import * as events from 'events'

import * as nssocket from 'nssocket'

import _ from 'underscore'


class Peer extends events.EventEmmiter {
    /* Peer for determining the size of a network using an anti-entropy protocol.
     *
     * Each peer stops when it's own average is different by the average
     * received by less than this.options.avgError.
     */
    constructor (ips, options={}) {
        this.ips = ips;
        this.id = Math.floor(Math.random() * Math.pow(10, 10));
        this.avg = 1;

        var defaults = {
            interval: 100, // Interval to call other peers.
            port: 3000, // Port on which to send/receive requests for sync.
            avgError: 0.001 // Precision to aim for.
        };
        this.options = _.extend(defaults, options);
    }

    start () {
        /** This method starts the computation for the number of peers in the
         * network.
         */
        this.broadcastAvg()
        this.listenToOtherPeers()
    }

    broadcastAvg () {
        setTimeout(() => {
            var randomPeer = _.sample(this.ips);
            this.callOtherPeer(randomPeer).then(() => {
                this.broadcastAvg()
            });
        }, this.options.interval);
    }

    callOtherPeer (otherIp) {
        /* Client code which calls a server to do sync.
         */
        var outbound = new nssocket.NsSocket();
        outbound.send(['sync', {'avg': this.avg, 'id': this.id}]);
        outbound.data(['sync'], this.processMessage);
        outbound.connect(this.options.send, otherIp);
    }

    listenToOtherPeers () {
        nssocket.createServer((socket) => {
            socket.data(['sync'], this.processMessage);
            socket.send(['sync', {'avg': this.avg, 'id': this.id}]);
        }).listen(this.options.port.receive);
    }

        Client: outbound.send(['sync', {'avg': this.avg, 'id': this.id}]);
        Server: socket.data(['sync'], this.processMessage);
        Server: socket.send(['sync', {'avg': this.avg, 'id': this.id}]);
        Client: outbound.data(['sync'], this.processMessage);

    processMessage (message) {
        {avg, id} = message
        if (id < this.id) {
            this.id =id
            this.avg = avg
        }
        else {
            this.avg = (this.avg + avg) / 2
        }
    }
}

export default Peer
