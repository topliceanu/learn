# Search App for SongKick

## Architecture

Two components:
- the rendering part
    - a React components tree manages the data rendering. See `app/components/Main.jsx` for the entry point.
- the data fetching part
    - fetch artists whose name matches the input keywords.
        - uses `bacon.js` to manage the stream of data from the input field.
        - bacon makes sure requests and responses are sequential, even if a later response comes back earlier.
    - fetch the shows that an artist has scheduled during his/her current tour.
        - this is performed only when the user expands the shows view and is only available for artists who are currently touring.

## Build

```bash
$ npm install # installs all the dependencies for production and testing.
$ npm test # runs the automated test suite.
$ npm run build # builds the js for running the app.
$ npm run serve # opens up a static http server on localhost:8888
```
