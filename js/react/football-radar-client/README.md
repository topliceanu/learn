# Football Radar Client


## Architecture

This app is composed of three pieces:

1. the data model `./lib/DataModel`. This class holds all the app state, handles
updates and maintains the list of teams sorted as per the specs. Because it's
so important it also has a comprehensive test suite `./test/*`
2. the view layer `./components/*`. Built using `react.js`, the components are
mostly stateless, receiving all the data they need from their parent, rendering
the data efficiently.
3. the glue: a set of simple functions which fetch data and link the first and
second sections.

## How to run

```
$ npm install
$ vi ./app/conf.js # !!! make sure the urls are correctly setup for your env.
$ npm test # to run tests for the data model.
$ npm run build # builds the front-end js application
$ npm run serve # starts a python static server on 0.0.0.0:8888
```
