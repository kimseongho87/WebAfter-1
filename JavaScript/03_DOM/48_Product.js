function sub(){
  // alert("OK");

  let bigPic=document.querySelector("#cup");
  let smallPics=document.querySelectorAll(".small");

  for(let i=0;i<smallPics.length;i++){
      smallPics[i].addEventListener("click", function(){
            // alert(smallPics[i].src);
            bigPic.src=smallPics[i].src;
      });
  }

  let isOpen=false;
  let view=document.querySelector("#view");
  view.addEventListener("click", function(){

      let detail=document.querySelector("#detail");
      
      if(isOpen==false){            // 상세 정보가 감춰져 있다면
         detail.style.display="block";
         view.innerText="상세 설명 닫기";
         isOpen=true;
      }else{                               // 상세 정보가 표시되어 있다면
         detail.style.display="none";
         view.innerText="상세 설명 보기";
         isOpen=false;
      }
  });
}