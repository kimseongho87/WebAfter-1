/*
   1. module 종류
      1-1) 사용자 정의 모듈
      1-2) node js 기본 모듈
      1-3) 외부 모듈

    2. 사용자의 정의 모듈
       2-1) 변수(variable), 객체(object), 함수(function), 폴더(folder)를 module로 만듬
       2-2) 외부로 공개  module.exports == exports
       2-3) require를 사용하여 module을 사용 (python import pands as pd)
*/

// 2-1) 사용자 모듈 정의후 require
const sum=require("./sum");
const sum_result=sum(1, 2);
console.log(sum_result);

const mul=require("./mul");
const mul_result=mul(5, 6);
console.log(mul_result);

// 2-2) node js 기본 모듈
const http=require("http");
