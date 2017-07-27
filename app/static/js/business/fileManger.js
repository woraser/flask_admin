/**
 * Created by chenhui on 2017/7/26.
 */
var fileMangerController = {
    fileTable:null,
    init:function () {
        fileMangerController.sensorDataTableInit();
        //上传当前的配置文件
        $("#uploadFile").click(function(){
           fileMangerController.uploadConfigFile();
        });
        //刷新table
        $("#reloadTable").click(function(){
           fileMangerController.reloadTable();
           bootbox.alert("刷新成功!");
        });

    },
    sensorDataTableInit:function () {
        fileMangerController.fileTable = $('#sensorDataTable').dataTable({
			serverSide:true,
            processing: true,
            searching:false,
            paging: false,
			ordering:false,
            bLengthChange:false,
            showNEntries: false,
            scrollCollapse: true,
            bInfo : false,
            pageLength:1000,
            destroy:false,
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
                url:"/fileTableList",
                type:"GET",
                contentType : "application/json"
            },
            columns: [
                { "title":"id","data": "objectId","orderable":false ,visible:false},
                { "title":"上传时间","data": "uploadTime","orderable":false },
                 { "title":"文件大小(Byte)","data": "fileSize","orderable":false }
            ],
            columnDefs:[{
                targets: 3,
                render: function (data, type, row, meta) {
                    return '<a type="button" class="" href="#" onclick=fileMangerController.downloadFile("' + row.objectId + '") >下载</a>' +' | '+
                        '<a type="button" class="" href="#" onclick=fileMangerController.enableFile("' + row.objectId + '") >启用</a>';
                }
            },
                { "orderable": false, "targets": 3 }
            ],
            fnDrawCallback:function(){



            }
        });
    },
    uploadConfigFile:function(){
        $.get("/fileUpload",function(res){
            var result = JSON.parse(res);
            if (result["status"] != 1){
                bootbox.alert("上传失败！");
                return;
            }
            var data = result["data"];
            if(!data || data["result"] !="upload success"){
                bootbox.alert("上传失败！");
                return;
            }
            bootbox.alert("上传成功！");
            return;
        });
    },
    reloadTable:function(){
        fileMangerController.fileTable.api().ajax.reload();
    },
    //从服务器下载文件
    downloadFile:function (id) {
        $.get("/downloadFile/"+id,function(res){
            var result = JSON.parse(res);
            if(result && result["status"] == 1){
                bootbox.alert("下载成功！");
                return;
            }
            bootbox.alert("下载失败！");
            return;
        });

    },
    //项目启用该配置文件
    enableFile:function (id) {
        bootbox.confirm({
                message: "启用该配置文件需要重启服务，是否重启？",
                buttons: {
                    confirm: {
                        label: '是',
                        className: 'btn-success'
                    },
                    cancel: {
                        label: '否',
                        className: 'btn-danger'
                    }
                },
                //        返回结构 true 是 false 否
                callback: function (result) {
                    console.log('This was logged in the callback: ' + result);
                    if (result == true){

                    }else{
                        return;
                    }
                }
});
        
    }

};

$(document).ready(function() {
	fileMangerController.init();
});


