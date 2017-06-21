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

var dateFormatCommon = function(date, format) {
	if (!date)
		return;
	if (!format)
		format = "yyyy-MM-dd HH:mm:ss";

	switch (typeof date) {
		case "string":
			//"2015-05-13T16:00:00.000+0000"
			var reg=/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.?\d{0,3}[Z\-+]?(\d{2}:?\d{2})?/;
			var _zone = 0;
			var _zone_minute = 0;
			var _date_date = date.split("\.");
			if(reg.test(date)){
				var reg_Z=/[+](\d{0,4})/;
                if(_date_date.length == 2){
                	if(_date_date[1].indexOf("+") >=0){
                		_zone = _date_date[1].split("+")[1];
                	}else if(_date_date[1].indexOf("-") >=0){
                		_zone = -_date_date[1].split("-")[1];
                	}else if(_date_date[1].indexOf("Z") >=0){
                		_zone = _date_date[1].split("Z")[1];
                	}
                	_zone = parseInt(_zone);
                	var _n_date = new Date();
                	var _n_zone = reg_Z.exec(_n_date.toString())[1];
                	_zone = _zone+parseInt(_n_zone);
                	_zone_minute = _zone % 100;
                	_zone = _zone / 100;
                }
                _date_date[0] = _date_date[0].replace("T"," ");
			}
			//兼容IE
			_date_date[0] = _date_date[0].replace(/-/g,"/");
			date = new Date(_date_date[0]);
			//时区变化
			date.setHours(_zone+date.getHours());
			date.setMinutes(_zone_minute+date.getMinutes());
			break;
		case "number":
			date = new Date(date);
			break;
	}

	if (!date instanceof Date)
		return;
	var dict = {
		"yyyy" : date.getFullYear(),
		"M" : date.getMonth() + 1,
		"d" : date.getDate(),
		"H" : date.getHours(),
		"m" : date.getMinutes(),
		"s" : date.getSeconds(),
		"MM" : ("" + (date.getMonth() + 101)).substr(1),
		"dd" : ("" + (date.getDate() + 100)).substr(1),
		"HH" : ("" + (date.getHours() + 100)).substr(1),
		"mm" : ("" + (date.getMinutes() + 100)).substr(1),
		"ss" : ("" + (date.getSeconds() + 100)).substr(1)
	};
	return format.replace(/(yyyy|MM?|dd?|HH?|ss?|mm?)/g, function() {
		return dict[arguments[0]];
	});
}
