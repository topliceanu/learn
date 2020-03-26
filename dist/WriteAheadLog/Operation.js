class Operation {
    // Interface for Operation that need to pas through the WAL.

    undo () {}

    redo () {}

    serialize () {}

    deserialize () {}

}


export default Operation;
