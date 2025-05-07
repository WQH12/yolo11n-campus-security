function cllshuaxin() {

     $.ajax({
		 url:'/cllshuaxin',                     //从gettime这个视图函数获取数据，一会编写
                type:'get',                         //采用get方法
                dataType:'JSON',
                success:function(cll) {
			           var hallChart = echarts.init(document.getElementById('hallLost'));
        var option3 = {
			    toolbox: { //可视化的工具箱

show: true,

feature: {

dataView: { //数据视图

show: true

},

restore: { //重置

show: true

},



saveAsImage: {//保存图片

show: true

},


}

},
        	    tooltip : {
        	        trigger: 'axis',
        	        textStyle:{color:'blue'}
        	    },
        	    legend: {
        	        data:['校园实时人流量',''],
        	    },

        	    grid: {
        	        left: '4%',
        	        right: '4%',
        	        bottom: '4%',
        	        containLabel: true
        	    },
        	    xAxis : [
        	        {
        	            type : 'category',
        	            boundaryGap : false,
        	            data : ['西门入口','水塘','体育场','综合楼','东门入口',' 大道'],
        	            splitLine:{show:false},
        	        	axisLabel:{textStyle:{color:'white'}}
        	        }
        	    ],
        	    yAxis : [
        	             {
							 type : 'value',
             	           splitNumber:4,
             	           splitLine:{
             	        		 show:true,
             	        		 lineStyle:{
             	        			 width: 1,
             	        			 type: 'dotted',
                                     color:'white'
                                    //  这一块来改标线的颜色
             	        		 }
             	        		},
             	            axisLabel : {
             	                formatter: '{value}',
             	               textStyle:{color:'white'}
             	            }
             	        }

        	    ],
        	    series : [
					{
					    name:'实时人流量',
					    type:'line',
					    data:[cll[0]['num'], cll[1]['num'], cll[2]['num'], cll[3]['num'], cll[4]['num'], cll[5]['num']],
                        itemStyle: {
                            normal: {
                                label: {
                                    show: true,
                                    position: 'top',
                                    formatter: '{c}'
                                }
                            }
                        }
					}
        	    ]
        	};
		hallChart.setOption(option3);
                }
     })
  }
setInterval(cllshuaxin,10000)
