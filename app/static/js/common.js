/**
 * Created by chenhui on 2017/5/24.
 */

function _ajax(method, url, data, callback) {
    $.ajax({
        type: method,
        url: url,
        data: data,
        dataType: 'json'
    }).done(function(r) {
        if (r && r.error) {
            return callback && callback(r);
        }
        return callback && callback(null, r);
    }).fail(function(jqXHR, textStatus) {
        return callback && callback({error: 'HTTP ' + jqXHR.status, message: 'Network error (HTTP ' + jqXHR.status + ')'});
    });
}

function getApi(url, data, callback) {
    if (arguments.length === 2) {
        callback = data;
        data = {};
    }
    _ajax('GET', url, data, callback);
}

function postApi(url, data, callback) {
    if (arguments.length === 2) {
        callback = data;
        data = {};
    }
    _ajax('POST', url, data, callback);
}

