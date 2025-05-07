function clearcontent(elementID) {
    document.getElementById(elementID).innerHTML = "";
} //直接把原来的div都清空就可以了


function fun2(elementID){
    var btn = document.getElementById("12345");
    clearcontent(elementID);
    var div1=document.createElement("div")
    var button1 = document.createElement("button");
    button1.innerHTML="2.1";
    button1.className="custom-btn btn-1"
    div1.className="frame_1"
    div1.appendChild(button1);

    var div2=document.createElement("div")
    var button2 = document.createElement("button");
    button2.innerHTML="2.2";
    button2.className="custom-btn btn-1"
    div2.className="frame_5"
    div2.appendChild(button2);

    var div3=document.createElement("div")
    var button3 = document.createElement("button");
    button3.innerHTML="2.3";
    button3.className="custom-btn btn-1"
    div3.className="frame_9"
    div3.appendChild(button3);

    var div4=document.createElement("div")
    var button4 = document.createElement("button");
    button4.innerHTML="2.4";
    button4.className="custom-btn btn-1"
    div4.className="frame_13"
    div4.appendChild(button4);

    var div5=document.createElement("div")
    var button5 = document.createElement("button");
    button5.innerHTML="2.5";
    button5.className="custom-btn btn-1"
    div5.className="frame_17"
    div5.appendChild(button5);

    btn.appendChild(div1)
    btn.appendChild(div2)
    btn.appendChild(div3)
    btn.appendChild(div4)
    btn.appendChild(div5)

}

function fanhui(elementID){

    var btn = document.getElementById("12345");
    clearcontent(elementID);

    var div1=document.createElement("div")
    var button1 = document.createElement("button");
    button1.innerHTML="1";
    button1.className="custom-btn btn-1"
    div1.className="frame_1"
    div1.appendChild(button1);

    var div2=document.createElement("div")
    var button2 = document.createElement("button");
    button2.innerHTML="2";
    button2.className="custom-btn btn-1"
    button2.setAttribute("onclick","fun2(12345)");  //这个来设计按钮的点击效果
    div2.className="frame_2"
    div2.appendChild(button2);

    var div3=document.createElement("div")
    var button3 = document.createElement("button");
    button3.innerHTML="3";
    button3.className="custom-btn btn-1"
    div3.className="frame_3"
    div3.appendChild(button3);

    var div4=document.createElement("div")
    var button4 = document.createElement("button");
    button4.innerHTML="4";
    button4.className="custom-btn btn-1"
    div4.className="frame_4"
    div4.appendChild(button4);

    var div5=document.createElement("div")
    var button5 = document.createElement("button");
    button5.innerHTML="5";
    button5.className="custom-btn btn-1"
    div5.className="frame_5"
    div5.appendChild(button5);

    
    var div6=document.createElement("div")
    var button6= document.createElement("button");
    button6.innerHTML="6";
    button6.className="custom-btn btn-1"
    div6.className="frame_6"
    div6.appendChild(button6);
    
    var div7=document.createElement("div")
    var button7= document.createElement("button");
    button7.innerHTML="7";
    button7.className="custom-btn btn-1"
    div7.className="frame_7"
    div7.appendChild(button7);
    
    var div8=document.createElement("div")
    var button8 = document.createElement("button");
    button8.innerHTML="8";
    button8.className="custom-btn btn-1"
    div8.className="frame_8"
    div8.appendChild(button8);
    
    var div9=document.createElement("div")
    var button9 = document.createElement("button");
    button9.innerHTML="9";
    button9.className="custom-btn btn-1"
    div9.className="frame_9"
    div9.appendChild(button9);
    
    var div10=document.createElement("div")
    var button10= document.createElement("button");
    button10.innerHTML="10";
    button10.className="custom-btn btn-1"
    div10.className="frame_10"
    div10.appendChild(button10);
    
    var div11=document.createElement("div")
    var button11 = document.createElement("button");
    button11.innerHTML="11";
    button11.className="custom-btn btn-1"
    div11.className="frame_11"
    div11.appendChild(button11);
    
    var div12=document.createElement("div")
    var button12 = document.createElement("button");
    button12.innerHTML="12";
    button12.className="custom-btn btn-1"
    div12.className="frame_12"
    div12.appendChild(button12);
    
    var div13=document.createElement("div")
    var button13= document.createElement("button");
    button13.innerHTML="13";
    button13.className="custom-btn btn-1"
    div13.className="frame_13"
    div13.appendChild(button13);
    
    var div14=document.createElement("div")
    var button14 = document.createElement("button");
    button14.innerHTML="14";
    button14.className="custom-btn btn-1"
    div14.className="frame_14"
    div14.appendChild(button14);
    
    var div15=document.createElement("div")
    var button15 = document.createElement("button");
    button15.innerHTML="15";
    button15.className="custom-btn btn-1"
    div15.className="frame_15"
    div15.appendChild(button15);
    
    var div16=document.createElement("div")
    var button16= document.createElement("button");
    button16.innerHTML="16";
    button16.className="custom-btn btn-1"
    div16.className="frame_16"
    div16.appendChild(button16);
    
    var div17=document.createElement("div")
    var button17 = document.createElement("button");
    button17.innerHTML="17";
    button17.className="custom-btn btn-1"
    div17.className="frame_17"
    div17.appendChild(button17);
    
    var div18=document.createElement("div")
    var button18 = document.createElement("button");
    button18.innerHTML="5";
    button18.className="custom-btn btn-1"
    div18.className="frame_18"
    div18.appendChild(button18);
    
    var div19=document.createElement("div")
    var button19 = document.createElement("button");
    button19.innerHTML="19";
    button19.className="custom-btn btn-1"
    div19.className="frame_19"
    div19.appendChild(button19);
    
    var div20=document.createElement("div")
    var button20 = document.createElement("button");
    button20.innerHTML="20";
    button20.className="custom-btn btn-1"
    div20.className="frame_20"
    div20.appendChild(button20);
    btn.appendChild(div1)
    btn.appendChild(div2)
    btn.appendChild(div3)
    btn.appendChild(div4)
    btn.appendChild(div5)
    btn.appendChild(div6)
    btn.appendChild(div7)
    btn.appendChild(div8)
    btn.appendChild(div9)
    btn.appendChild(div10)
    btn.appendChild(div11)
    btn.appendChild(div12)
    btn.appendChild(div13)
    btn.appendChild(div14)
    btn.appendChild(div15)
    btn.appendChild(div16)
    btn.appendChild(div17)
    btn.appendChild(div18)
    btn.appendChild(div19)
    btn.appendChild(div20)
}


function textchange1(elementID){
   var tt=document.createElement("div");
   var tt1=document.createElement("div");
   console.log(document.getElementById('wuyu1'))
   tt.className="media ui-sortable-handle"
   tt1.className="checkbox m-0"
   var tt2=document.createElement("label");
   tt2.className="t-overflow"
   tt2.setAttribute("style","text-decoration: line-through;")
   var tt3=document.createElement("input");
   var tt4=document.createElement("a");
   var yiwai1=document.createElement("div");
   var yiwai2=document.createElement("ins");
   yiwai1.className="icheckbox_minimal checked"
   yiwai1.setAttribute("aria-checked","false")
   yiwai1.setAttribute("aria-disabled","false")
   yiwai1.setAttribute("style","position: relative;")
   tt4.innerText="事件1";

   tt3.setAttribute("checked","checked")
   tt3.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
   tt3.setAttribute("type","checkbox")

   yiwai2.className="iCheck-helper";
   yiwai2.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")

   yiwai1.appendChild(tt3);
   yiwai1.appendChild(yiwai2)

   tt2.appendChild(yiwai1)
   tt2.appendChild(tt4)
   tt1.appendChild(tt2);
   tt.appendChild(tt1);
   
   var imp=document.getElementById('ycl')
   imp.appendChild(tt)


    document.getElementById(elementID).innerHTML = "";
}
function textchange2(elementID){
    var tt=document.createElement("div");
    var tt1=document.createElement("div");
    console.log(document.getElementById('wuyu1'))
    tt.className="media ui-sortable-handle"
    tt1.className="checkbox m-0"
    var tt2=document.createElement("label");
    tt2.className="t-overflow"
    tt2.setAttribute("style","text-decoration: line-through;")
    var tt3=document.createElement("input");
    var tt4=document.createElement("a");
    var yiwai1=document.createElement("div");
    var yiwai2=document.createElement("ins");
    yiwai1.className="icheckbox_minimal checked"
    yiwai1.setAttribute("aria-checked","false")
    yiwai1.setAttribute("aria-disabled","false")
    yiwai1.setAttribute("style","position: relative;")
    tt4.innerText="事件2";
 
    tt3.setAttribute("checked","checked")
    tt3.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
    tt3.setAttribute("type","checkbox")
 
    yiwai2.className="iCheck-helper";
    yiwai2.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
 
    yiwai1.appendChild(tt3);
    yiwai1.appendChild(yiwai2)
 
    tt2.appendChild(yiwai1)
    tt2.appendChild(tt4)
    tt1.appendChild(tt2);
    tt.appendChild(tt1);
    
    var imp=document.getElementById('ycl')
    imp.appendChild(tt)
 
 
     document.getElementById(elementID).innerHTML = "";
 }
 function textchange3(elementID){
    var tt=document.createElement("div");
    var tt1=document.createElement("div");
    console.log(document.getElementById('wuyu1'))
    tt.className="media ui-sortable-handle"
    tt1.className="checkbox m-0"
    var tt2=document.createElement("label");
    tt2.className="t-overflow"
    tt2.setAttribute("style","text-decoration: line-through;")
    var tt3=document.createElement("input");
    var tt4=document.createElement("a");
    var yiwai1=document.createElement("div");
    var yiwai2=document.createElement("ins");
    yiwai1.className="icheckbox_minimal checked"
    yiwai1.setAttribute("aria-checked","false")
    yiwai1.setAttribute("aria-disabled","false")
    yiwai1.setAttribute("style","position: relative;")
    tt4.innerText="事件3";
 
    tt3.setAttribute("checked","checked")
    tt3.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
    tt3.setAttribute("type","checkbox")
 
    yiwai2.className="iCheck-helper";
    yiwai2.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
 
    yiwai1.appendChild(tt3);
    yiwai1.appendChild(yiwai2)
 
    tt2.appendChild(yiwai1)
    tt2.appendChild(tt4)
    tt1.appendChild(tt2);
    tt.appendChild(tt1);
    
    var imp=document.getElementById('ycl')
    imp.appendChild(tt)
 
 
     document.getElementById(elementID).innerHTML = "";
 }
 function textchange4(elementID){
    var tt=document.createElement("div");
    var tt1=document.createElement("div");
    console.log(document.getElementById('wuyu1'))
    tt.className="media ui-sortable-handle"
    tt1.className="checkbox m-0"
    var tt2=document.createElement("label");
    tt2.className="t-overflow"
    tt2.setAttribute("style","text-decoration: line-through;")
    var tt3=document.createElement("input");
    var tt4=document.createElement("a");
    var yiwai1=document.createElement("div");
    var yiwai2=document.createElement("ins");
    yiwai1.className="icheckbox_minimal checked"
    yiwai1.setAttribute("aria-checked","false")
    yiwai1.setAttribute("aria-disabled","false")
    yiwai1.setAttribute("style","position: relative;")
    tt4.innerText="事件4";
 
    tt3.setAttribute("checked","checked")
    tt3.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
    tt3.setAttribute("type","checkbox")
 
    yiwai2.className="iCheck-helper";
    yiwai2.setAttribute("style","position: absolute; top: -20%; left: -20%; display: block; width: 140%; height: 140%; margin: 0px; padding: 0px; background: rgb(255, 255, 255); border: 0px; opacity: 0;")
 
    yiwai1.appendChild(tt3);
    yiwai1.appendChild(yiwai2)
 
    tt2.appendChild(yiwai1)
    tt2.appendChild(tt4)
    tt1.appendChild(tt2);
    tt.appendChild(tt1);
    
    var imp=document.getElementById('ycl')
    imp.appendChild(tt)
 
 
     document.getElementById(elementID).innerHTML = "";
 }