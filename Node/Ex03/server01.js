/**
 *   2-2) 외부모듈 : 설치 필요
 *          1) 패키지 관리자 설치 D:>> npm init >> pagckage.json 파일 생성
 *   
 *           2) 서버 express 모듈 D:>npm i(install) express
 */

const express=require('express');   // 서버 사용을 위한 모듈
const app=express();                    //  서버관련된 함수및 객체들

app.listen(3000, function(){           // 서버구동, 포트 열어놓는다. (0~65536)
   console.log("Server Strat=======>");
});      

// 사용자 요청
app.get('/', function (req, res) {
   res.send('<h3> 서버구동 성공 </h3>')
 })


// http://localhost:3000   





