const express=require('express');
const app=express();
const port=2000;

app.listen(port, function(){
   console.log(`Server Strat =======> ${port}`);
});

// http://localhost:2000
app.get("/", function(req, res){
   res.sendFile(__dirname + "/pages/index.html");
});

// http://localhost:2000/about
app.get("/about", function(req, res){
   res.sendFile(__dirname + "/pages/about.html");
});