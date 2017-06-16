(function ($) {
    var default1={
        titleText:"提示信息",
        submitBtnText:"确 定",
        cancelBtnText:"取 消",
        width:"550",
        height:"200",
        resizable:true,
        draggable:true,
        openCall:function(){
			
		},
        closeCall:function(){
			
		},
        submitCall:function(){
        	//default1.jq.dialog('close');
        },
		modal:true,
        position:{my: "center", at: "center", of: window },
        jq:"" ,//jquery对象 $("#alert")
        msg:"",//提示内容
		url:""
    };
    $.openDialog = function (option){
        var opt = $.extend({},default1,{
        	closeCall:function(){
        		option.jq.dialog('close');
    		},
            submitCall:function(){
            	option.jq.dialog('close');
            }
        },option);
		var dialogParent =  opt.jq.parent();
		var dialogOwn =  opt.jq.clone();
		dialogOwn.hide();
        var db = opt.jq.dialog({
            modal:opt.modal,
            title:opt.titleText,
            width:opt.width,
            height:opt.height,
            position:opt.position,
            resizable:option.resizable,
            draggable:option.draggable,
            buttons: [
                {
				   text:opt.submitBtnText,
                   click:function(){
					   opt.submitCall();
				   }
                },
				{
				   text:opt.cancelBtnText,
				   click:function(){
					   opt.closeCall();
				   }
				}
            ],
            open:function(even,ui){
                if ($.isFunction(opt.openCall)) {
                    opt.openCall();
                }
            },
            focus: function( event, ui ) {
            	if ($.isFunction(opt.focusCall)) {
                    opt.focusCall();
                }
            },
            close:function(even,ui){
				dialogOwn.appendTo(dialogParent);
				$(this).dialog("destroy").remove()
            }
        });
		db.load(opt.url);
		//db.dialog('open');
    };
	
	$.popAlert = function (msg,opt){
		var db =  $("<div ><p id='alertInfo' class='text-center'></p></div>");
		var dialogParent = db.parent();
		var dialogOwn = db.clone();
		dialogOwn.hide();
		var opt = $.extend({},default1,opt);
        db.dialog({
            modal:opt.modal,
            title:opt.titleText,
            width:opt.width,
            height:opt.height,
            position:opt.position,
            resizable:false,
            draggable:false,
            buttons: [
                {
				   text:opt.submitBtnText,
                   click:function(){
                	   db.dialog('close');
				   }
                }
            ],
			open:function(event,ui){  
				msg = msg+"";
				var str = "";
				if(msg.indexOf("/n") != -1){
					msg = msg.split("/n");
					$(msg).each(function(idx,item){
						str += item+"</br>";
					});
				}else{
					str = msg;
				}
               $("#alertInfo").html(str);
            },
			close:function(){
				dialogOwn.appendTo(dialogParent);
				$(this).dialog("destroy").remove();
			}
        });
    };
})(jQuery);
