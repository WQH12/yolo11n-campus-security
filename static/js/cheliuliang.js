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
        	        data:['高铁站实时人流量',''],
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
        	            boundaryGap : true,
        	            data : ['售票厅','候车厅','站台','停车场','入口',' 地铁'],
        	            splitLine:{show:false},
        	        	axisLabel:{textStyle:{color:'black'}}
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
                                     color:'blue'
                                    //  这一块来改标线的颜色
             	        		 }
             	        		},
             	            axisLabel : {
             	                formatter: '{value}',
             	               textStyle:{color:'black'}
             	            }
             	        }

        	    ],
        	    series : [
					{
					    name:'实时人流量',
					    type:'line',
					    data:[0, 3, 2, 4, 2, 5],
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


