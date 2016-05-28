// This module only exports a method which calls the given url and passes the
// response back to the given callback.
//
// It makes no attempt to handle browser inconsistencies when it comes to ajax
// implementations or possible connection errors.
//
// TODO use a specialized tool like jQuery.ajax or superagent.
module.exports = function (url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            callback(JSON.parse(xhr.responseText));
        }
    };
    xhr.open('GET', url);
    xhr.send();
};
