import * as Immutable from './my-immutable.js'
import {globalStateQueue} from './state.js'


class View {

    constructor (data, path = []) {
        // Build an immutable object.
        this.data = Immutable.fromJS(data);
        this.prefixPath = path;
    },

    subView (path) {
        // Create a subview by passing a new path.
        let fullPath = this.prefixPath.slice().concat(path);
        return new View(this.data, fullPath);
    },

    getIn (path) {
        // When accessing values, pass the relative path.
        let absolutePath = this.prefixPath.slice().concat(path);
        return this.data.getIn(absolutePath);
    },

    setIn (path, value) {
        // When setting values, pass the relative path.
        let absolutePath = this.prefixPath.slice().concat(path)
        let snapshot = this.data.set(absolutePath, value);
        globalStateQueue.push(snapshot);
    }
}

export default View
