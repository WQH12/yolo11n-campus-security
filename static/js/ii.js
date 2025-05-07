function baojingtuxian(){

var btn = document.getElementById("ditu");
var i = document.createElement("img");
i.src = "static img/bj.png";
i.className="bj"
btn.appendChild(i);
setInterval(function(){
    i.style.opacity = 0;  //图片隐藏
},250)
//再次调用setInterval()函数,每隔0.5秒显示 时间差就可以形成图片闪烁功能;
setInterval(function(){
    i.style.opacity = 1;  //图片显示
},500)

}

