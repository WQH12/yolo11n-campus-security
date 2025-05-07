option = {
                      backgroundColor: 'white',
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
  tooltip: {
    confine: true,
    trigger: 'axis',
    axisPointer: {
      type: 'shadow',
    },
    backgroundColor: 'rgba(3, 16, 42, 0.85)',
    borderColor: 'rgba(114, 190, 253, 0.6)',
    borderWidth: 1,
    padding: 12,
  },
  grid: {
    left: '5%',
    top: '20%',
    bottom: '15%',
    right: '5%',
  },
  xAxis: {
    axisTick: {
      show: false,
    },
    axisLine: {
      lineStyle: {
        color: 'rgba(94,194,181,0.45)',
        width: 1, // 这里是为了突出显示加上的
      },
    },
    axisLabel: {
      color: '#6A93B9',
      fontSize: 12,
    },
    data: ['校门', '操场', '寝室园区', '十字路口'],
  },
  yAxis: {
    type: 'value',
    name: '报警次数',
    min: 0,
    minInterval: 1,
    nameTextStyle: {
      align: 'center',
    },
    splitLine: {
      lineStyle: {
        color: 'rgba(255, 255, 255, 0.15)',
        // type: 'dashed', // dotted 虚线
      },
    },
    splitArea: { show: false },
    axisLine: {
      show: false,
    },
    axisTick: {
      show: false,
    },
    axisLabel: {
      fontSize: 12,
      color: '#6A93B9',
      fontFamily: 'Bebas',
    },
  },
  series: [{
    name: 'hill',
    type: 'pictorialBar',
    barCategoryGap: '-20px',
    symbol: 'path://M12.000,-0.000 C12.000,-0.000 16.074,60.121 22.731,60.121 C26.173,60.121 -3.234,60.121 0.511,60.121 C7.072,60.121 12.000,-0.000 12.000,-0.000 Z',
    label: {
      show: true,
      position: 'top',
      distance: 5,
      color: '#fff',
      // fontWeight: 'bolder',
      fontSize: 12,
      fontFamily: 'Bebas',
    },
    itemStyle: {
      normal: {
        color(params) {
          let colorList = ['#6bdebd', '#6b91e1', '#6bdebd', '#6b91e1']
          return colorList[params.dataIndex]
        },
      },
      emphasis: {
        opacity: 1,
      },
    },
    data: [3, 2,5, 4],
    z: 10,
  }],
};


                    var myChart = echarts.init(document.getElementById("diduan"));
                    myChart.setOption(option);
                    window.addEventListener("resize", function () {
                        myChart.resize();
                    });




