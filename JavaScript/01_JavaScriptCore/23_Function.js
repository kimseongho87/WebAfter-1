function checkForm(obj){    // obj=this=form
   // alert("OK");
   // https://www.youtube.com/channel/UC-622LO2UxQR0OEZA9F90kQ

   if(obj.irum.value==""){       // abc길동
      alert("이름을 입력하세요");
      obj.irum.focus();
      return false;
   }

   if(obj.pwd.value.length < 3){      // 툭수문자대문소문
      alert("비밀번호 3자리 이상입니다");
      obj.pwd.focus();
      return false;
   }

   if(obj.pwd.value != obj.pwdCheck.value){
      alert("비밀번호 일치하지 않습니다");
      obj.pwdCheck.focus();
      return false;
   }

   if(obj.siteUrl.value==""){
      alert("이동할 사이트를 반드시 선택하세요");
      obj.siteUrl.focus();
      return false;
   }

   var test=false;

   for(let i=0;i<obj.fruit.length;i++){      // i < 4 0123
      if(obj.fruit[i].checked==true){
         // obj.fruit[i].valule;  DB 데이터 값 준다
         test=true;
      }
   }

   if(test==false){
      alert("좋아하는 과일 반드시 선택하세요");
      return false;
   }

   var count=0;
   var str="";

   for(let i=0;i<obj.interest.length;i++){

      if(obj.interest[i].checked==true){
         str += obj.interest[i].value + ",";    // 경제, 음악
         count++;     // 2
      }
   }

   // alert(str);

   if(count==0){
      alert("관심사를 반드시 하나이상 체크하세요");
      return false;
   }

   // 1시에 시작합니다.
}