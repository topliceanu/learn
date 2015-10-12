(function (global) {
  var Pusher = function (url) {
    var that = this;
    that.handlers = {};
    that.connected = new Promise(function (resolve, reject) {
      that.ws = new WebSocket(url);
      that.ws.onopen = resolve;
      that.ws.onerror = reject;
      that.ws.onmessage = that.handler;
    });
  };

  Pusher.prototype.publish = function (channel, data) {
    var that = this;
    that.connected.then(function () {
      that.ws.send(JSON.stringify({"channel": channel, "data": data}));
    });
  };

  Pusher.prototype.subscribe = function (channel, handler) {
    var that = this;
    if (!that.handlers[channel]) {
      that.handlers[channel] = [];
    }
    if (that.handlers[channel].indexOf(handler) != -1) {
      return;
    }
    that.connected.then(function () {
      that.ws.send(JSON.stringify({"subscribe": channel}));
      that.handlers[channel].push(handler);
    });
  };

  Pusher.prototype.unsubscribe = function (channel, handler) {
    var that = this;
    that.ws.send(JSON.stringify({"unsubscribe": channel}));
    if (!that.handlers[channel]) {
      return;
    }
    delete that.handlers[channel];
  };

  Pusher.prototype.handler = function (event) {
    var that = this;
    var message = JSON.parse(event.data);
    var channel = message['channel'];
    var data = message['data'];
    if (!channel || !that.handlers[channel]) {
      return;
    }
    that.handlers[channel].forEach(function (handler) {
      handler(data);
    });
  };

  global.Pusher = Pusher;
})(this);
