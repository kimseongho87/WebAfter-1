var xhr=null;
var arr=new Array();

function startRequest(){
   xhr=new XMLHttpRequest();
   xhr.open("get", "responseXML.xml", true);
   xhr.send();
   xhr.onreadystatechange=resultProcess;
}

function resultProcess(){
   if(xhr.readyState==4 && xhr.status==200){
      arr.push(xhr.responseXML);

      let xmlDoc=xhr.responseXML;
      let studentList=xmlDoc.querySelectorAll("student");
      arr.push(studentList.length);

      for(let i=0;i<studentList.length;i++){
         let student=studentList[i].childNodes;
         arr.push(student.length);

         let div=document.createElement("div");
         for(let j=0;j<student.length;j++){
               if(student[j].nodeType==1){
                  arr.push(student[j].childNodes[0].nodeValue);

                  let span=document.createElement("span");
                  span.innerHTML=student[j].childNodes[0].nodeValue + "&nbsp;";

                  div.appendChild(span);
               }
         }

         document.querySelector("#disp").appendChild(div);
      }

      // alert(arr.join("\n"));     
   }
}