function baifenbishuaxin() {

     $.ajax({
		 url:'/bfbxin',                     //从gettime这个视图函数获取数据，一会编写
                type:'get',                         //采用get方法
                dataType:'JSON',
                success:function(bfb) {

 const chartData = [
        {
          value: 5,
          name: "楼顶",
        },
        {
          value: 2,
          name: "吸烟",
        },
        {
          value: 3,
          name: "探出栏杆",
        },
        {
          value: bfb[0]['num'],
          name: "危险区域",
        },
        {
          value: 7,
          name: "水边",
        },
        {
          value: 4,
          name: "地面积水",
        },
      ];
      const colorList = ['#88D9FF', '#0092FF', '#81EDD2', '#B0FA93', '#63F2FF', '#9999FE'];
      const sum = chartData.reduce((per, cur) => per + cur.value, 0);
      const gap = (1 * sum) / 100;
      const pieData1 = [];
      const pieData2 = [];
      const gapData = {
        name: "",
        value: gap,
        itemStyle: {
          color: "transparent",
        },
      };

      //图标位置显示
      let lefts = ["4%", "4%", "4%", "80%", "80%", "80%"];
      let tops = ["14%", "37%", "65%", "14%", "37%", "65%"];
      let legendData = [];
      let total = 0;
      chartData.forEach((item) => {
        total += item.value;
      });

      for (let i = 0; i < chartData.length; i++) {
        // 第一圈数据
        pieData1.push({
          ...chartData[i],
          itemStyle: {
            borderRadius: 10,
          },
        });
        pieData1.push(gapData);

        // 第二圈数据
        pieData2.push({
          ...chartData[i],
          itemStyle: {
            color: colorList[i],
            opacity: 0.21,
          },
        });
        pieData2.push(gapData);

        //  分散图例
        let bfb = parseInt((chartData[i].value / total) * 100) + "%";
        legendData.push({
          show: true,
          icon: "circle", //'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
          left: lefts[i],
          top: tops[i],
          // itemWidth: '10px',
          // itemHeight:'10px',
          itemStyle: {
            color: colorList[i],
          },
          formatter:
            `{aa| ` + chartData[i].name + ` }` + `\n\n` + `{bb| ` + bfb + `}`, // 也可以是个函数return
          x: "left",
          textStyle: {
            // color: "#BAFF7F",
            rich: {
              aa: {
                color: "black",
              },
              bb: {
                color: colorList[i],
              },
            },
          },
          data: [chartData[i].name],
        });
      }
      // console.log("pieData2---------", pieData2);

      option = {
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
        backgroundColor: 'white',
        title: {

          subtext: "353",
          x: "49%",
          y: "38%",
          itemGap:15,
          textStyle: {
            color: "#f5f5f6",
            fontSize: 15,
            fontWeight: "bold",
          },
          subtextStyle: {

            color: "#f5f5f6",
            fontSize: 50,
            fontWeight: "bold",
          },
          textAlign:'center'
        },

        // backgroundColor: "#0F141B",
        tooltip: {
          show: true,
          backgroundColor: "rgba(0, 0, 0,.8)",
          textStyle: {
            color: "#fff",
          },
        },
        legend: legendData,
        grid: {
          top: 30,
          right: 20,
          bottom: 10,
          left: 10,
        },
        color: colorList,
        series: [
              {
                name: '',
                type: 'pie',
                roundCap: true,
                radius: ['66%', '70%'],
                center: ['50%', '45%'],
                label: {
                    show: false
                },
                labelLine: {
                    show: false
                },
                data: pieData1
            },
                 {
                type: 'pie',
                radius: ['66%', '60%'],
                center: ['50%', '45%'],
                gap: 1.71,
                label: {
                    show: false
                },
                labelLine: {
                    show: false
                },
                silent: true,
                data: pieData2
            },
            {
         type: 'gauge',
         zlevel: 2,
         splitNumber: 90,
         radius: '60%',
         center: ['50%', '45%'],
         startAngle: 90,
         endAngle: -269.9999,
         axisLine: {
            show: false,
         },
         axisTick: {
            show: false,
         },
         axisLabel: {
            show: false,
         },
         splitLine: {
            show: true,
            length: 7,
            lineStyle: {
               width: 4,
               color: 'rgb(33,85,130)',
            },
         },
         pointer: {
            show: 0,
         },
         detail: {
            show: 0,
         },
      },
    {
                type: 'pie',
                center: ['50%', '45%'],
                radius: [0, '45.6%'],
                label: {
                    show: false
                },
                labelLine: {
                    show: false
                },
                itemStyle: {
                    color: 'rgba(75, 126, 203,.1)'
                },
                silent: true,
                data: [
                    {
                        value: 100,
                        name: ''
                    }
                ]
            }
        ],
      };


var myChart = echarts.init(document.getElementById("ttt"));
myChart.setOption(option);
window.addEventListener("resize", function () {
    myChart.resize();
});

                }
     })
  }
setInterval(baifenbishuaxin,1000)