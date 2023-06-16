class Yonsan{
   constructor(su, buho, num){
      this.su=su;
      this.buho=buho;
      this.num=num;
      this.result=0;
     // alert(this.su + "," + this.buho + "," + this.num + "," + this.result);
   }

   calculate(){
       if(this.buho=="+"){
         this.result=this.su+this.num;
         // alert(this.result);
         }else if(this.buho=="-"){
            this.result=this.su-this.num;
         }else if(this.buho=="*"){
            this.result=this.su*this.num;
         }else if(this.buho=="/"){
            if(this.num==0){
               this.num=1;
            }
            this.result=this.su/this.num;
         }else{
            this.result="부호 다시입력!!!!!";
         }

         // alert(this.result);
   }

   disp(){
      let h3=document.getElementById("disp");
      h3.innerHTML=this.result;
   }
}