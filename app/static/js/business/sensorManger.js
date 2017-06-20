/**
* Created by chenhui on 2017/6/20.
*/

var sensorMangerController = {
	init:function(){
	     var showDetail = function(val){
        alert("21#L"+val);
    };
		sensorMangerController.sensorTableInit();
	},
	sensorTableInit:function () {
		$('#sensorTable').dataTable({
			serverSide:true,
            processing: true,
            searching:false,
            paging: false,
			ordering:false,
			pageLength:100,
            bLengthChange:false,
            showNEntries: false,
            scrollCollapse: true,
            bInfo : false,
            destroy:true,
			language: {
			  emptyTable: "暂无数据"
			},
           ajax: {
                url:"/common/dataTable/Sensor",
                type:"POST",
                contentType : "application/json",
                data: function ( d ) {
                var draw = d['draw'];
                var post_data = {
                    offset :  d['start'],
                    pageSize :  d["length"],
                    pageNumber :  (d["start"] / d["length"] + 1),
                    draw :  d['draw']
                };
                //添加额外的参数传给服务器
                return JSON.stringify(post_data);
                }
            },
            columns: [
                { "title":"id","data": "id","orderable":false,visible:false },
                { "title":"序列号","data": "sensor_no","orderable":false },
                { "title":"传感器名称","data": "sensor_name","orderable":false },
                { "title":"采集周期","data": "job_time","orderable":false },
				{ "title":"用途","data": "type","orderable":false },
				{ "title":"当前度数","data": "sensor_no","orderable":false },
				{ "title":"接口","data": "interface","orderable":false },
				{ "title":"端口","data": "sensor_name","orderable":false },
				{ "title":"上限值","data": "max_limit","orderable":false },
				{ "title":"下限值","data": "min_limit","orderable":false }
            ],
             columnDefs:[{
                targets: 10,
                render: function (data, type, row, meta) {
                    return '<a type="button" class="" href="#" onclick=sensorMangerController.showDetail(' + row.id + ') >查看详情</a>' +' | '+
                        '<a type="button" class="" href="#" onclick=sensorMangerController.updateSetting(' + row.id + ') >设置</a>';
                }
            },
                { "orderable": false, "targets": 4 }
            ]
        });
    },
    showDetail:function(val){
	    alert("123");

    },
    updateSetting:function (val) {
        sensorMangerController.showDialogForConfig(val);
    },
    "showDialogForConfig":function(val){
		var html_=$("#sensorFormDiv").html();
        var dialog = new bootbox.dialog({
            message: html_,
            title: "传感器设置",
            buttons: {
                success: {
                	label:"确认",
                    className: "btn-success",
                    callback: function() {
                	    debugger;
                	    sensorMangerController.updateSensorConfig(val)

                    }
                },
				cancel: {
				label: '取消',
				className: 'btn-danger',
				callback: function() {
                }
        }
            }
        });
        $(".modal-dialog").css({"top":"30%","left":"35%"});
        $.ajax({
			type:"GET",
			url:"/sensorInfo/"+val,
            async:false,
			success:function(result){
                var data = JSON.parse(result);
                 if(data["status"] != 1){
                     bootbox.alert("数据获取失败，请重新再试!");
                 }
                 var sensorInfo = data["data"];
                 $(".bootbox-body .unique_id").val(sensorInfo["id"]);
                 $(".bootbox-body .sensor_no").val(sensorInfo["sensor_no"]);
                 $(".bootbox-body .max_limit").val(sensorInfo["max_limit"]);
                 $(".bootbox-body .min_limit").val(sensorInfo["min_limit"]);
                 $(".bootbox-body .job_time").val(sensorInfo["job_time"]);
                }
            });
    },
    updateSensorConfig:function () {
		$(".modal-dialog input").each(function(e){
			if(!$(this).val()){
				bootbox.alert("请补全传感器配置");
				e.preventDefault();
				return;
			}
		});
		var update_config= {
			location : $(".bootbox-body .location").val().trim(),
			full_name : $(".bootbox-body .full_name").val().trim(),
			email_account : $(".bootbox-body .email_account").val().trim(),
			email_host : $(".bootbox-body .email_host").val().trim(),
			email_port : $(".bootbox-body .email_port").val().trim(),
			email_sender : $(".bootbox-body .email_sender").val().trim(),
			email_pwd : $(".bootbox-body .email_pwd").val().trim(),
			remote_address : $(".bootbox-body .remote_address").val().trim()
		};
		$.ajax({
			type:"PUT",
			url:"/nodeConfig",
			data:JSON.stringify(update_config),
			dataType:"json",
			contentType:'application/json',
			success:function(result){
				window.location.reload();
			}

		});

    }
};


$(document).ready(function() {
	sensorMangerController.init();
});
