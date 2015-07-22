import {writeFile, readFile} from 'fs'


class Log {
    // Write-Ahead Log algorithm.
    // @see http://en.wikipedia.org/wiki/Algorithms_for_Recovery_and_Isolation_Exploiting_Semantics

    constructor (logPath) {
        this.logPath = logPath;
    },

    write (operation) {
        operation.serialize().then((string) => {
        });
    },

    recovery (id) {
        // Replys all operations starting from id+1 onward.
    },

    checkpoint () {}
}


export default Log
