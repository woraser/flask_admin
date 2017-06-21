/**
 * Created by chenhui on 2017/6/20.
 */
var sensorDetailController = {
    init:function () {
        sensorDetailController.sensorDataTableInit();

    },
    sensorDataTableInit:function () {
        $('#sensorDataTable').dataTable({
			serverSide:true,
            processing: true,
            searching:false,
            paging: true,
            pagingType:   "full_numbers",
			ordering:false,
			pageLength:20,
            bLengthChange:false,
            showNEntries: true,
            scrollCollapse: true,
            bInfo : false,
            destroy:true,
            sDom: '<"top"l>rt<"bottom_right"p><"clear">',
			language: {
			  emptyTable: "暂无数据",
              oPaginate : {
                    "sFirst" : "首页",
                    "sPrevious" : "上一页",
                    "sNext" : "下一页",
                    "sLast" : "末页"
                }
			},
           ajax: {
                url:"/common/dataTable/SensorData",
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
                },
               dataSrc:function(json){
                    var data = json.data;
                    for(var i in data){
                        data[i]["created_time"] = dateFormatCommon(parseInt(data[i]["created_time"])*1000)
                    }
                    return data;
               }
            },
            columns: [
                { "title":"id","data": "id","orderable":false },
                { "title":"传感器编号","data": "sensor_no","orderable":false },
                { "title":"采集时间","data": "created_time","orderable":false },
                { "title":"采集数据","data": "val","orderable":false }
            ],
            fnDrawCallback:function(){



            }
        });
    }

};


$(document).ready(function() {
	sensorDetailController.init();
});


