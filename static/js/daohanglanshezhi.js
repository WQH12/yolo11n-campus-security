// 这一块诗是写的是车辆管理的那个菜单
var daohang1=document.getElementById("cheliangguanli1");
var jiankongdinweizicaidan1=document.getElementById("cheliangguanlizicaidan1");
var jiankongdinweizicaidan2=document.getElementById("cheliangguanlizicaidan2");
var jiankongdinweizicaidan3=document.getElementById("cheliangguanlizicaidan3");
var jiankongdinweizicaidan4=document.getElementById("cheliangguanlizicaidan4");
var jiankongdinweizicaidan5=document.getElementById("cheliangguanlizicaidan5");
var i=1;


daohang1.onclick=function(){
    //显示出子按钮
    i=i+1;
    if(i%2==0) {
        jiankongdinweizicaidan1.style.display = 'block';
        jiankongdinweizicaidan2.style.display = 'block';
        jiankongdinweizicaidan3.style.display = 'block';
        jiankongdinweizicaidan4.style.display = 'block';
        jiankongdinweizicaidan5.style.display = 'block';
    }
    else {
        jiankongdinweizicaidan1.style.display = 'none';
        jiankongdinweizicaidan2.style.display = 'none';
        jiankongdinweizicaidan3.style.display = 'none';
        jiankongdinweizicaidan4.style.display = 'none';
        jiankongdinweizicaidan5.style.display = 'none';
    }
}
//这一块写的是通行记录的子菜单
var tongxing1=document.getElementById("tongxinjilu1");
var tongxingjiluzicaidan1=document.getElementById("tongxinjiluzicaidan1");
var tongxingjiluzicaidan2=document.getElementById("tongxinjiluzicaidan2");
var tongxingjiluzicaidan11=document.getElementById("tongxinjiluzicaidan11");
var tongxingjiluzicaidan12=document.getElementById("tongxinjiluzicaidan12");
var tongxingjiluzicaidan21=document.getElementById("tongxinjiluzicaidan21");
var tongxingjiluzicaidan22=document.getElementById("tongxinjiluzicaidan22");
var i1=1;
tongxing1.onclick=function(){
    //显示出子按钮
    i1=i1+1;
    if(i1%2==0) {
        tongxingjiluzicaidan1.style.display = 'block';
        tongxingjiluzicaidan2.style.display = 'block';
    }
    else {
        tongxingjiluzicaidan1.style.display = 'none';
        tongxingjiluzicaidan2.style.display = 'none';

    }
}
var i2=1;
tongxingjiluzicaidan1.onclick=function(){
    //显示出二级子按钮
    i2=i2+1;
    if(i2%2==0) {
        tongxingjiluzicaidan11.style.display = 'block';
        tongxingjiluzicaidan12.style.display = 'block';
    }
    else {
        tongxingjiluzicaidan11.style.display = 'none';
        tongxingjiluzicaidan12.style.display = 'none';

    }
}
var i3=1;
tongxingjiluzicaidan2.onclick=function(){
    //显示出二级子按钮
    i3=i3+1;
    if(i3%2==0) {
        tongxingjiluzicaidan21.style.display = 'block';
        tongxingjiluzicaidan22.style.display = 'block';
    }
    else {
        tongxingjiluzicaidan21.style.display = 'none';
        tongxingjiluzicaidan22.style.display = 'none';

    }
}

//这一块写人员信息

//这边写访客管理

//这一块写的是规则配置的子菜单

var guizepeizhi1=document.getElementById("guizepeizhi");
var guizepeizhizicaidan1=document.getElementById("guizepeizhizicaidan1");
var guizepeizhizicaidan11=document.getElementById("guizepeizhizicaidan11");
var guizepeizhizicaidan12=document.getElementById("guizepeizhizicaidan12");
var guizepeizhizicaidan13=document.getElementById("guizepeizhizicaidan13");
var guizepeizhizicaidan2=document.getElementById("guizepeizhizicaidan2");
var guizepeizhizicaidan21=document.getElementById("guizepeizhizicaidan21");
var guizepeizhizicaidan22=document.getElementById("guizepeizhizicaidan22");
var guizepeizhizicaidan3=document.getElementById("guizepeizhizicaidan3");
var guizepeizhizicaidan31=document.getElementById("guizepeizhizicaidan31");
var guizepeizhizicaidan32=document.getElementById("guizepeizhizicaidan32");
var i6=1;
guizepeizhi1.onclick=function(){
    //显示出子按钮
    i6=i6+1;
    if(i6%2==0) {
        guizepeizhizicaidan1.style.display = 'block';
        guizepeizhizicaidan2.style.display = 'block';
        guizepeizhizicaidan3.style.display = 'block';

    }
    else {
        guizepeizhizicaidan1.style.display = 'none';
        guizepeizhizicaidan2.style.display = 'none';
        guizepeizhizicaidan3.style.display = 'none';

    }
}
var i7=1;
guizepeizhizicaidan2.onclick=function(){
    //显示出二级子按钮
    i7=i7+1;
    if(i7%2==0) {
        guizepeizhizicaidan21.style.display = 'block';
        guizepeizhizicaidan22.style.display = 'block';
    }
    else {
        guizepeizhizicaidan21.style.display = 'none';
        guizepeizhizicaidan22.style.display = 'none';

    }
}
var i10=1;
guizepeizhizicaidan1.onclick=function(){
    //显示出二级子按钮
    i10=i10+1;
    if(i10%2==0) {
        guizepeizhizicaidan11.style.display = 'block';
        guizepeizhizicaidan12.style.display = 'block';
        guizepeizhizicaidan13.style.display = 'block';
    }
    else {
        guizepeizhizicaidan11.style.display = 'none';
        guizepeizhizicaidan12.style.display = 'none';
        guizepeizhizicaidan13.style.display = 'none';

    }
}
var i11=1;
guizepeizhizicaidan3.onclick=function(){
    //显示出二级子按钮
    i11=i11+1;
    if(i11%2==0) {
        guizepeizhizicaidan31.style.display = 'block';
        guizepeizhizicaidan32.style.display = 'block';
    }
    else {
        guizepeizhizicaidan31.style.display = 'none';
        guizepeizhizicaidan32.style.display = 'none';

    }
}

//这边写事件报警
var shijianbaojin1=document.getElementById("shijianbaojin");
var shijianbaojinzicaidan1=document.getElementById("shijianbaojinzicaidan1");
var shijianbaojinzicaidan2=document.getElementById("shijianbaojinzicaidan2");

var i8=1;
shijianbaojin1.onclick=function(){
    //显示出子按钮
    i8=i8+1;
    if(i8%2==0) {
        shijianbaojinzicaidan1.style.display = 'block';
        shijianbaojinzicaidan2.style.display = 'block';
    }
    else {
        shijianbaojinzicaidan1.style.display = 'none';
        shijianbaojinzicaidan2.style.display = 'none';

    }
}
//这边设置系统设置的子菜单
var xitongshezhi=document.getElementById("xitongshezhi");
var xitongshezhizicaidan1=document.getElementById("xitongshezhizicaidan1");
var xitongshezhizicaidan2=document.getElementById("xitongshezhizicaidan2");
var xitongshezhizicaidan3=document.getElementById("xitongshezhizicaidan3");
var i9=1;
xitongshezhi.onclick=function(){
    //显示出子按钮
    i9=i9+1;
    if(i9%2==0) {
        xitongshezhizicaidan1.style.display = 'block';
        xitongshezhizicaidan2.style.display = 'block';
        xitongshezhizicaidan3.style.display = 'block';
    }
    else {
        xitongshezhizicaidan1.style.display = 'none';
        xitongshezhizicaidan2.style.display = 'none';
        xitongshezhizicaidan3.style.display = 'none';

    }
}

