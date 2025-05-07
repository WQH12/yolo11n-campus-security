//
// function xiaoxishuaxin() {
//     $.ajax({
//         url: '/xiaoxi',                     //从gettime这个视图函数获取数据，一会编写
//         type: 'get',                         //采用get方法
//         dataType: 'JSON',
//         success: function (d) {            //成功之后的结果，这里的t是从'/gettime'视图函数获得的返回值，如果返回值有多个，可以用json
//             //$('#timenow').load('当前时间为')//用“当前时间为：t”代替timenow也就是上面的“当前时间?"
//                if(!d['is_null'])
//                          $('#sum1').innerHTML=d[0];
//                          $('#ssxx').empty();
//
//
//                         for(let v=0 ;v < d[0]; v++) {
//                             var v1=$("<div class='media'> </div>");
//                             var v2=$("<div class=\"pull-left\"> </div>");
//                             var v3=$("<img width='40' src='static/img/"+d[1][v]['id']+".jpg' >");
//                             v2.append(v3)
//                             v1.append(v2)
//                             var v4=$("<div class=\"media-body\"></div>");
//                             var v5=$("<small class=\"text-muted\">"+d[1][v]['location']+ '-'+ d[1][v]['time']+"</small><br>")
//                             var v6=$("<a class=\"t-overflow\" href=\"\">"+d[1][v]['content']+"</a>")
//                             v4.append(v5)
//                             v4.append(v6)
//                             v1.append(v4)
//
//                             $('#ssxx').append(v1);
//
//                         }
//
//         }
//     })
// }
// setInterval(xiaoxishuaxin,4000)