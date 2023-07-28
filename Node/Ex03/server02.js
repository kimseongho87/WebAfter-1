const express=require('express');     // 서버 모듈
const app=express();                        // 객체
const port=3000;                              // 접속 포트

app.listen(port, function(){                
   console.log(`Server Start======> ${port}`);
});

// localhost:3000  URL
app.get("/", function(req, res){
       // req - 아이디, 비빌번호 ~~~~

       res.send(`
         <h1>Hello Main Page</h1>
         <h1>사과 </h1>
         <h1>바나나</h1>
         <h1>딸기</h1>
         <h1>메론</h1>
       `)
});

// localhost:3000/apple
app.get("/apple", function(req, res){
   console.log("apple OK");
});

// localhost:3000/abc/xyz/banana
app.get("/abc/xyz/banana", function(req, res){
   console.log("banana OK");
});

// 20분 시작입니다.


