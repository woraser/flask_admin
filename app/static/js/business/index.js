/**
* Created by chenhui on 2017/6/15.
*/

var dashboardController = {
	init:function(){
		var cpuPie = dashboardController.cpuPieInit();
		var ramPie = dashboardController.ramPieInit();
		setInterval(function () {
			dashboardController.reloadPieAjax(cpuPie["selector"],cpuPie["option"],ramPie["selector"],ramPie["option"])
        },5000);
		dashboardController.loadingLineData();
		//
		$("#doConfig").click(function(){
			dashboardController.showDialogForConfig();
		});
	},
	cpuPieInit:function(){
		//第二个参数可以指定前面引入的主题
		var cpuPie = echarts.init(document.getElementById('dev-status-bar-wxre1'), 'dark');
		cpuPie.showLoading();
		var option1 = {
				tooltip : {formatter: "{a} <br/>{b} : {c}%"},
				toolbox: {feature: {saveAsImage: {}}},
				series: [
					{
						name: 'CPU使用率',
						type: 'gauge',
						detail: {formatter:'{value}%'},
						data: [{value: 50, name: '使用率'}]
					}]};
		return {
			"selector": cpuPie,
			"option": option1
		};
	},
	ramPieInit:function(){
		//第二个参数可以指定前面引入的主题
		var ramPie = echarts.init(document.getElementById('dev-status-bar-wxre3'), 'dark');
		ramPie.showLoading();
		var option3 = {
				tooltip : {formatter: "{a} <br/>{b} : {c}%"},
				toolbox: {feature: {saveAsImage: {}}},
				series: [
					{
						name: '内存使用率',
						type: 'gauge',
						detail: {formatter:'{value}%'},
						data: [{value: 50, name: '使用率'}]
					}]};
		return {
		"selector": ramPie,
		"option": option3
	    };

	},
	reloadPieAjax:function(cpuPie,CpuOption,ramPie,ramOption){
		 $.get("/systemPieInfo", function(result){
		 	var data = JSON.parse(result);
			var cpu_free = parseFloat(data["cpu_free"]).toFixed(2);
		 	var ram_usage = parseFloat(data["ram_usage"]).toFixed(2);

		 	CpuOption.series[0].data[0].value = (100-cpu_free);
		 	ramOption.series[0].data[0].value = ram_usage;
		 	cpuPie.setOption(CpuOption, true);
		 	ramPie.setOption(ramOption, true);
		 	cpuPie.hideLoading();
		 	ramPie.hideLoading();
		 });
	},
	cpuLineChartInit:function(){
			//第二个参数可以指定前面引入的主题
			var cpuLineChart = echarts.init(document.getElementById('dev-status-bar-wxre2'), 'dark');
			//图表显示提示信息
			var option2 = {
				tooltip: {
					trigger: 'axis',
					position: function (pt) {return [pt[0], '10%'];}},
				title: {
					left: 'center',
					text: 'CPU使用率记录',
					textStyle: {
						color: 'white',
						fontStyle: 'normal',
						fontWeight: 'bolder',
						fontFamily: 'sans-serif',
						fontSize: 18}},
				toolbox: {
					feature: {
						dataZoom: {yAxisIndex: 'none'},
						restore: {},
						saveAsImage: {}}},
				xAxis: {
					type: 'category',
					boundaryGap: false,
					data: [],
				    axisLine:{lineStyle:{color:'#9193A0'}}},
				yAxis: {
					type: 'value',
					min:0,
					max:100,
					splitNumber:10,
					boundaryGap: [0, '100%'],
					axisLine:{lineStyle:{color:'#9193A0'}}},
				dataZoom: [{
					type: 'inside',
					start: 0,
					end: 10}, {
					start: 0,
					end: 10,
					handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
					handleSize: '80%',
					handleStyle: {
						color: '#fff',
						shadowBlur: 3,
						shadowColor: 'rgba(0, 0, 0, 0.6)',
						shadowOffsetX: 2,
						shadowOffsetY: 2}}],
				series: [{
						name:'CPU使用率(%)',
						type:'line',
						smooth:true,
						symbol: 'none',
						sampling: 'average',
						itemStyle: {normal: {color: '#1CB6F7'}},
						areaStyle: {
							normal: {
								color: {
									type: 'linear',
									x: 0, y: 0, x2: 0, y2: 1,
									colorStops: [{
										offset: 0, color: '#17cbd3' // 0% 处的颜色
									}, {
										offset: 1, color: '#f9747d' // 100% 处的颜色
									}],
									globalCoord: false // 缺省为 false
								}}},
						data: []
					}
				]
			};
			return {
					"selector": cpuLineChart,
					"option": option2
					};

	},
	ramLineChartInit:function(){
			var ramLineChart = echarts.init(document.getElementById('dev-status-bar-wxre4'), 'dark');
			//图表显示提示信息
			var option4= {
				tooltip: {
					trigger: 'axis',
					position: function (pt) {
						return [pt[0], '10%'];
					}
				},
				title: {
					left: 'center',
					text: '内存使用记录',
					textStyle: {
						color: 'white',
						fontStyle: 'normal',
						fontWeight: 'bolder',
						fontFamily: 'sans-serif',
						fontSize: 18
						}},
				toolbox: {
					feature: {
						dataZoom: {
							yAxisIndex: 'none'},
						restore: {},
						saveAsImage: {}}},
				xAxis: {
					type: 'category',
					boundaryGap: false,
					data: [],
				    axisLine:{lineStyle:{color:'#9193A0'}}},
				yAxis: {
					type: 'value',
					min:0,
					max:100,
					splitNumber:10,
					boundaryGap: [0, '100%'],
					axisLine:{lineStyle:{color:'#9193A0'}}},
				dataZoom: [{
					type: 'inside',
					start: 0,
					end: 10
				}, {
					start: 0,
					end: 10,
					handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
					handleSize: '80%',
					handleStyle: {
						color: '#fff',
						shadowBlur: 3,
						shadowColor: 'rgba(0, 0, 0, 0.6)',
						shadowOffsetX: 2,
						shadowOffsetY: 2
					}
				}],
				series: [
							{
								name:'内存使用率(%)',
								type:'line',
								smooth:true,
								symbol: 'none',
								sampling: 'average',
								itemStyle: {normal: {color: '#5C60D8'}},
								areaStyle: {
									normal: {
										color: {
											type: 'linear',
											x: 0,
											y: 0,
											x2: 0,
											y2: 1,
											colorStops: [{
												offset: 0, color: '#5663D3' // 0% 处的颜色
											}, {
												offset: 1, color: '#474C76' // 100% 处的颜色
											}],
											globalCoord: false // 缺省为 false
										}
									}
								},
								data: []
					}
				]
			};
			return {
					"selector": ramLineChart,
					"option": option4
					};
	},
	loadingLineData:function(){
		var cpuLineTemp = dashboardController.cpuLineChartInit();
		var ramLineTemp = dashboardController.ramLineChartInit();
		$.get("/systemLineInfo", function(result){
			var data = JSON.parse(result);
			if(!data){
				return
			}
			var count = data.count;
			if(parseInt(count) ==0){
				return
			}
			var option_date = [];
			var cpu_option_data = [];
			var ram_option_data = [];
			var content = data.data;
			for(var i in content){
				var child = content[i];
				if(!child["collect_time"]){
					continue;
				}
                var collect_date = new Date(child["collect_time"]);
				option_date.push([collect_date.getFullYear(), collect_date.getMonth() + 1, collect_date.getDate(),collect_date.getHours(),collect_date.getMinutes(),collect_date.getSeconds()].join('/'));

				if(child["cpu_usage"]){
					cpu_option_data.push(child["cpu_usage"]);
				}
				if(child["ram_usage"]){
					ram_option_data.push(child["ram_usage"]);
				}
			}
			if(option_date.length >0){
				//cpu
				var cpu_selector = cpuLineTemp["selector"];
				var cpu_option = cpuLineTemp["option"];
				cpu_option.xAxis.data = option_date;
				cpu_option.series[0].data = cpu_option_data;
				cpu_selector.setOption(cpu_option, true);
				//ram
				var ram_selector = ramLineTemp["selector"];
				var ram_option = ramLineTemp["option"];
				ram_option.xAxis.data = option_date;
				ram_option.series[0].data = ram_option_data;
				ram_selector.setOption(ram_option, true);
			}
		 });
	},
	"showDialogForConfig":function(){
		var html_=$("#configFormDiv").html();
        var dialog = new bootbox.dialog({
            message: html_,
            title: "传感器配置",
            buttons: {
                success: {
                	label:"确认",
                    className: "btn-success",
                    callback: function() {
                	dashboardController.updateNodeConfig()
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
        // $(".modal-dialog").css({"top":"30%","left":"35%"});
    },
	updateNodeConfig:function () {
		$(".modal-dialog input").each(function(){
			if(!$(this).val()){
				bootbox.alert("请补全节点配置");
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
	dashboardController.init();

// $("#back").click(function(){
// $.openDialog({width:"700",height:"500",jq:$("#secondLevelDialog"),titleText:"配置",url:"html/iotxnew/edit.html"});
// });

});
