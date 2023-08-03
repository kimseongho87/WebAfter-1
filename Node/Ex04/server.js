const express=require('express');
const app=express();
const port=3000;

app.listen(port, function(){      
   console.log(`Server Start ====> ${port}`);
});

// 시작 page
app.get('/', function(req, res){
   res.sendFile(__dirname + "/msg.html");
});

// 환경설정
app.use(express.urlencoded({ extended: true }));      // URL 웹브라우저 요청시 인코딩 방식을 해석할수 있다. 

// GET
app.get("/msg", function(req, res){
   const msg=req.query.message;
   console.log("GET 방식 전달:", msg);
});

// POST
app.post('/msg', function(req, res){
   const msg=req.body.message;
   console.log("POST 방식 전달", msg);    
});
