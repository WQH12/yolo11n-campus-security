// 要开启报警的时候 这一段别忘了加上去
function baojingshuaxin() {
    $.ajax({
        url: '/baojing',                     //从gettime这个视图函数获取数据，一会编写
        type: 'get',                         //采用get方法
        dataType: 'JSON',
        success: function (c) {            //成功之后的结果，这里的t是从'/gettime'视图函数获得的返回值，如果返回值有多个，可以用json
            //$('#timenow').load('当前时间为')//用“当前时间为：t”代替timenow也就是上面的“当前时间?"
            if(c['flag']==1)
            {
                var btn = document.getElementById("ditu");
                var i = document.createElement("img");
                i.src = "static/img/bj.png";
                i.className="bj"
                btn.appendChild(i);
                for(l=0;l<4;l++)
                {  setInterval(function(){
                i.style.opacity = 0;  //图片隐藏
                },250)
                //再次调用setInterval()函数,每隔0.5秒显示 时间差就可以形成图片闪烁功能;
                setInterval(function(){
                i.style.opacity = 1;  //图片显示
                },500)

                }


            }
            else
            {
                var btn = document.getElementById("ditu");
                var i = document.createElement("img");
                i.src = "static/img/bj.png";
                i.className="bj"
                i.style.opacity=0;
                btn.appendChild(i);
                btn.removeChild(i);

            }


        }
    })
}
setInterval(baojingshuaxin,5000)