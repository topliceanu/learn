var path = require('path');


module.exports = {
    entry: './app/index.jsx',
    output: {
        path: path.join(__dirname, 'app'),
        filename: 'bundle.js'
    },
    module: {
        loaders: [{
            test: /\.jsx$/,
            exclude: '/node_modules/',
            loader: 'jsx-loader'
        }]
    }
};
