const express=require('express');
const app=express();
const port=3000;

// 서버 준비중
app.listen(port, function(){      
   console.log(`Server Start =====> ${port}`);
});

// ROOT
app.get('/', function(req, res){
   res.sendFile(__dirname + "/pages/login.html");
});

// 환경설정
app.use(express.urlencoded({ extended: true }));         // 데이터 전송

// GET
app.get('/login/check', function(req, res){
   const id=req.query.id;
   const pwd=req.query.pwd;
   console.log("GET 방식>>>>" + id + "\t" + pwd);

   if (id == "abc123" && pwd=="abc123"){
      res.sendFile(__dirname + "/pages/success.html");
  }else{
      res.sendFile(__dirname + "/pages/fail.html");
  }
});

// POST
app.post('/login/check', function(req, res){
   const id=req.body.id;  
   const pwd=req.body.pwd;
   console.log("POST 방식>>>>" + id + "\t" + pwd);

   if (id == "abc123" && pwd=="abc123"){
      res.sendFile(__dirname + "/pages/success.html");
  }else{
      res.sendFile(__dirname + "/pages/fail.html");
  }
});