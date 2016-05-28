import {globalStateQueue} from './state.js'


let render = () => {
    // Repeatedly re-render the app whenever there's a new snapshot.
    let snapshot = globalStateQueue.shift();
    if (snapshot !== undefined) {
        let container = document.getElementById('container');
        React.render(<Cart state={snapshot}/>, container);
    }
    // Om does this at 60 FPS. And also does batching of snapshots.
    setTimeout(render, 0);
};


// Start rendering.
render();
