-- 내장함수 :문자, 숫자, 날짜 https://dev.mysql.com/doc/refman/8.0/en/functions.html

-- 문자열 함수 : 문자열 조작
SELECT ASCII('A') AS '숫자값변환',
	   CHAR(65) AS '아스키코드';
       
-- BIT_LENGTH(문자열), CHAR_LENGTH(문자열), LENGTH(문자열)
SELECT BIT_LENGTH('abc') AS 'bit크기',              -- 3*8(bit)=24bit
	   CHAR_LENGTH('ABC') AS '문자개수반환',		   -- 3개	
       LENGTH('abc') AS 'BYTES크기';				   -- 3byte

SELECT BIT_LENGTH('가나다') AS 'bit크기',             	-- 3*(8*3)=72bit
	   CHAR_LENGTH('가나다') AS '문자개수반환',		   	-- 3개	
       LENGTH('가나다') AS 'BYTES크기';				-- 3*3=9byte / 한글은 UTF-8로 한글 문장당 3바이트
       
-- CONCAT(문자열1, 문자열2) 
SELECT CONCAT('Hello', '입니다') AS '문자열연결';   

SELECT * FROM buytbl; 
SELECT CONCAT(userID, prodName) AS '문자열'
FROM buytbl;

SELECT prodName, 
	   CHAR_LENGTH(prodName) AS '문자열길이'
FROM buytbl;

-- CONCAT_WS(구분자, 문자열1, 문자열2,..)
SELECT CONCAT_WS('/', '2025', '01', '01') AS '구분자연결';
       
-- INSTR(문자열, 검색어)
SELECT INSTR('하나둘셋', '둘') AS '문자열 검색';
SELECT INSTR('Hello', 'e') AS '문자열 검색';

-- 1시에 시작합니다.
       
       