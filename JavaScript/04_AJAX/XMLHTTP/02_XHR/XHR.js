var xhr=null;
var arr=new Array();

function startRequest(){
   arr.push("OK");

   xhr=new XMLHttpRequest();
   xhr.open("get", "JSON.txt", true);
   xhr.send();
   xhr.onreadystatechange=resultProcess;
}

function resultProcess(){
   arr.push(xhr.readyState + "," + xhr.status);
   alert(arr.join("\n"));

   // 11시 7분
}