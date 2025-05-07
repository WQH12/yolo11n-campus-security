function a1() {
    var d=event.target.getAttribute("id"); //d就可以当前触发函数的那个id
    t1=document.getElementById(d)

    table=document.getElementById("hh")
    let tr = document.createElement("tr");
    tr.setAttribute("id","gh")
    for (let i = 0; i < 5; i++) { //i的循环次数 决定了最后一共添加了多少行就是了
        let td = document.createElement("td");
        td.innerHTML = '';
        tr.appendChild(td);
    }

    let tdl = document.createElement("td");
    let del = document.createElement("button");
    del.className="btn btn-sm btn-alt"
    del.innerHTML = "删除"
    i=1;
    del.setAttribute("id",i)
    del.setAttribute("onclick","myFun1();")
    tdl.appendChild(del);
  

    let update = document.createElement("button")
    update.className="btn btn-sm btn-alt"
    update.innerHTML = "修改"
    update.setAttribute("id","u8")
    update.setAttribute("onclick","myFun2();")
    tdl.appendChild(update);

    tr.appendChild(tdl);
    table.appendChild(tr);
    console.log(del.getAttribute("id"))
    xuhao();

}

//删除函数
function myFun1() {
    var d=event.target.getAttribute("id"); //d就可以当前触发函数的那个id
    t1=document.getElementById(d);
    var c=t1.parentNode.parentNode.getAttribute("id");
    dd=document.getElementById(c)
    dd.remove();
    xuhao();
}

//修改函数
function myFun2() {
    var d=event.target.getAttribute("id"); //d就可以当前触发函数的那个id
    t1=document.getElementById(d)
    var c=t1.parentNode.parentNode.getAttribute("id"); //c就是包含按钮的tr的id了
    dd=document.getElementById(c)
    table=document.getElementById("hh")
    console.log(table.children[0].children[0].innerHTML)
    let arr1 = dd.children; //arr1返回的是子节点的一个集合
    if (t1.innerHTML == "修改") {
        t1.innerHTML = "保存";
        for (let i = 0; i < arr1.length - 1; i++) {
            let a1 = document.createElement("input");
       
            a1.className="xiugailan"
            a1.value = arr1[i].innerHTML;
            arr1[i].innerHTML = "";
            arr1[i].appendChild(a1);
            //console.log(tr.children[i]);
        }
    } else {
        t1.innerHTML = "修改";
        for (let i = 0; i < arr1.length - 1; i++) {
            arr1[i].innerHTML = arr1[i].children[0].value; //本质上arr1[i]的children也就只有一个
        }
    }


}

function xuhao()
{
    table=document.getElementById("hh")
    var trs=table.children //trs就是tr的一个集合了对吧
    for (let i = 0; i < trs.length ; i++) //遍历每一个tr
    {
        trs[i].children[0].innerHTML=i+1;
    }


}

