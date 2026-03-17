// Configuration module. It's javascript instead of json to allow dynamic
// generation of configuration value if needed.


module.exports = {
    numPages: 10, // number of pages to fetch via HTTP in parallel.
    timeout: 10000 // number of ms to wait for a response from a HTTP GET request.
};
