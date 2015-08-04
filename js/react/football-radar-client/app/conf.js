// Configuration module.
// PLEASE update this for your local environment.
module.exports = {
    ws: {
        // WebSockets endpoints to receive updates.
        url: 'ws://192.168.33.11:8080/games'
    },
    http: {
        // REST Endpoint to fetch the teams json.
        url: 'http://192.168.33.11:8080/teams'
    }
};
