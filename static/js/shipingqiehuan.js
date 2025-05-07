function qiehuan1()
{
    // var d=event.target.getAttribute("id")
    // $('#shiping').empty();
    // var sp1=$("<img  src='/img/school_dection'  style='display: block; width: 100%; height: 100%'>");
    // $('#shiping').append(sp1)

    var d = event.target.getAttribute("id");
    // 定义按钮 id 到图片路径的映射
    var imageMap= window.imageMap;
    // 根据按钮 id 获取对应的图片路径
    var imagePath=imageMap[d];
    if (imagePath) {
        // 清空 #shiping 元素的内容
        $('#shiping').empty();
        // 创建新的 img 元素
        var sp1 = $("<img  src='" + imagePath + "'  style='display: block; width: 100%; height: 100%'>");
        // 将 img 元素添加到 #shiping 元素中
        $('#shiping').append(sp1);
    } else {
        console.log("未找到对应的图片路径");
    }
}


