//就是说只保存一周之类的数据库资源
function shigushuaxin() {

    $.ajax({
		 url:'/sgshuaxin',                     //从gettime这个视图函数获取数据，一会编写
                type:'get',                         //采用get方法
                dataType:'JSON',
                success:function(sg) {            //成功之后的结果，这里的t是从'/gettime'视图函数获得的返回值，如果返回值有多个，可以用json
                    //$('#timenow').load('当前时间为')//用“当前时间为：t”代替timenow也就是上面的“当前时间?"
                    if (!sg['is_null'])


                    var charts = {
                             unit: '累计发生次数',
                             names: [sg[0]['type'], '事件2'],
                             lineX: ['1', '2', '3', '4', '5', '6', '7'],
                             value: [
                                    [1, 3, 4, 5, 6, 7, sg[0]['num']],
                                    [1, 2, 3, 4, 5, 6, 7]
                                   ]

                               }
    var color = ['rgba(123,141,46', 'rgba(133,109,1']
    var lineY = []

    for (var i = 0; i < charts.names.length; i++) {
        var x = i
        if (x > color.length - 1) {
            x = color.length - 1
        }
        var data = {
            name: charts.names[i],
            type: 'line',
            color: color[x] + ')',
            smooth: true,
            areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: color[x] + ', 0.3)'
                    }, {
                        offset: 0.8,
                        color: color[x] + ', 0)'
                    }], false),
                    shadowColor: 'rgba(0, 0, 0, 0.1)',
                    shadowBlur: 10
                }
            },
            symbol: 'circle',
            symbolSize: 5,
            data: charts.value[i]
        }
        lineY.push(data)
    }

    lineY[0].markLine = {
        silent: true,
        data: [{
            yAxis: 5
        }, {
            yAxis: 100
        }, {
            yAxis: 200
        }, {
            yAxis: 300
        }, {
            yAxis: 400
        }]
    }
    var option = {

        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: charts.names,
            textStyle: {
                fontSize: 12,
                color: 'rgb(255,255,255)'
            },
            right: '4%'
        },
        grid: {
            top: '14%',
            left: '4%',
            right: '4%',
            bottom: '12%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: charts.lineX,
            axisLabel: {
                textStyle: {
                    color: 'rgb(255,255,255)'
                },

            }
        },
        yAxis: {
            name: charts.unit,
            type: 'value',
            axisLabel: {
                formatter: '{value}',
                textStyle: {
                    color: 'rgb(255,255,237)'
                }
            },
            splitLine: {
                lineStyle: {
                    color: 'rgb(255,244,237)'
                }
            },
            axisLine: {
                lineStyle: {
                    color: 'rgb(0,0,0)'
                }
            }
        },
        series: lineY
    }
    setInterval(() => {
        myChart.setOption({
            legend: {
                selected: {
                    '出口': false,
                    '入口': false
                }
            }
        })
        myChart.setOption({
            legend: {
                selected: {
                    '出口': true,
                    '入口': true
                }
            }
        })
    }, 10000)


    var myChart = echarts.init(document.getElementById("shigu"));
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

                }

	})
}
setInterval(shigushuaxin,1000)