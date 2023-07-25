-- 데이베이스 : shop
--            table 4개 buytbl, usertbl, membertbl(GUI), producttbl(GUI)
--            열(필드), 행(레코드)

-- DML : 조회(80%), 추가, 수정, 삭제

-- 1. 데이터베이스 조회
SHOW DATABASES;
USE sys;
USE shop;

-- 2. 테이블 조회
SHOW TABLES;
-- 데이블 구조/ 열 조회
DESC buytbl; 
DESC usertbl;         


-- 3. SELECT
-- 형식) SELECT [필드명 또는 표현식] 
--      FROM [테이블명 또는 뷰명]
-- 3-1) 열(컬럼, 필드)
-- 회원테이블의 특정 열 가져오기 
SELECT userID FROM usertbl;
SELECT userID, name, addr, mobile1 FROM usertbl;
SELECT * FROM usertbl;

SELECT 
    userID, name, addr, mobile1
FROM
    usertbl;
    
-- 구매 테이블
SELECT userID, prodName FROM buytbl;
SELECT userID FROM buytbl;

-- 중복 없이 데이터 조회
SELECT DISTINCT userID FROM buytbl;

SELECT addr FROM usertbl;
SELECT DISTINCT addr FROM usertbl;

-- 산술연산
SELECT userID,
	   price,
       amount,
	   price*amount,
       price+amount,
       price-amount,
       price/amount
FROM buytbl;

SELECT userID AS 아이디,
	   price,
       amount,
	   price*amount AS mul,
       price+amount AS 덧셈,
       price-amount 뺄셈,
       price/amount "나눗셈 입니다" 
FROM buytbl;

-- 형식) SELECT [필드명 또는 표현식] 
--      FROM [테이블명 또는 뷰명]
--      WHERE [조건절] 
--      조건절 :  조건연산자, 관계연산자, BETWEEN ~ AND, IN, LIKE

-- 3-2) 행(레코드)
-- 조건연산자 : =, <, >, >=, <=, !=
SELECT * FROM usertbl WHERE name='김경호';
SELECT * FROM usertbl WHERE name !='김경호';

SELECT userID,
	   name,
       birthYear
FROM usertbl
WHERE birthYear >= 1970;

SELECT * FROM buytbl WHERE amount < 5;

-- 관계연산자 : AND, OR
SELECT * FROM usertbl
WHERE birthYear >=1970 AND height >=182;

SELECT name FROM usertbl
WHERE birthYear >=1970 AND height >=182;

SELECT name, addr FROM usertbl
WHERE addr="경남" OR addr="전남" OR addr="경북";

-- LIKE : 문자열의 내용 검색 (%, _)
SELECT name, height FROM usertbl
WHERE name LIKE '김%';                -- 시작 

SELECT name, height FROM usertbl
WHERE name LIKE '%호';               -- 끝

SELECT name, height FROM usertbl
WHERE name LIKE '%시%';              -- 어디간에

SELECT name, height FROM usertbl
WHERE name LIKE '_종신';             -- 첫번째 글자는 아무거나

-- BETWEEN ~ AND : 데이터 숫자로 구성되어 있으며 연속적이 값
-- 고객테이블에서 키가 180이상 183이하인 사람의 이름과 키 출력
SELECT name, height FROM usertbl
WHERE height >= 180 AND height <= 183;

-- 데이터 숫자로 구성되 있으면, 연속적이 값 / 동일한 필드
SELECT name, height FROM usertbl
WHERE height BETWEEN 180 AND 183;

SELECT name, height FROM usertbl
WHERE (height >= 180 AND height <= 183) AND name='이승기';

SELECT name, height FROM usertbl
WHERE (height BETWEEN 180 AND 183) AND name='이승기';

SELECT name, height FROM usertbl
WHERE height >=180 AND name LIKE '이%';

-- 고객테이블에서 경남, 전남, 경북에 거주하는 고객의 이름과 주소를 출력하세요.
SELECT name, addr FROM usertbl
WHERE addr='경남' OR addr='전남' OR addr='경북';

SELECT name, addr FROM usertbl
WHERE addr IN('경남', '전남', '경북') ;

SELECT name, addr FROM usertbl
WHERE (addr='경남' OR addr='전남' OR addr='경북') OR name='바비킴';

SELECT name, addr FROM usertbl
WHERE addr IN('경남', '전남', '경북') OR name='바비킴';

SELECT name, addr FROM usertbl
WHERE addr='경남'or name='바비킴';

-- SubQuery : 퀴리안에 또 다른 퀴리문이 들어 있는 것
-- 김경호보다 키가 큰 사람 출력
-- 김경호
SELECT height FROM usertbl
WHERE name='김경호';        -- 177

-- 김경호보다 키가 큰 사람
SELECT name, height FROM usertbl
WHERE height > 177;

SELECT name, height FROM usertbl
WHERE height > (SELECT height FROM usertbl WHERE name='김경호');

-- 바비킴이랑 같은 지역에 사는 사람
SELECT addr FROM usertbl WHERE name='바비킴';

SELECT name, addr FROM usertbl WHERE addr='서울';

SELECT name, addr FROM usertbl 
WHERE addr=(SELECT addr FROM usertbl WHERE name='바비킴')
AND name != '바비킴';

SELECT * FROM usertbl; 

-- 은지원보다 생일년도 이후 사람의 이름과 생일년도 출력
SELECT birthYear FROM usertbl WHERE name='은지원';   -- 1972
SELECT name, birthYear FROM usertbl WHERE birthYear >= 1972;

SELECT name, birthYear FROM usertbl 
WHERE birthYear >= (SELECT birthYear FROM usertbl WHERE name='은지원');

-- 조용필의 mobile1 같은 사람 이름과 전화번호 출력
SELECT mobile1 FROM usertbl WHERE name='조용필';          -- 011
SELECT name, mobile1 FROM usertbl WHERE mobile1='011'; 

SELECT name, mobile1 FROM usertbl 
WHERE mobile1=(SELECT mobile1 FROM usertbl WHERE name='조용필');   -- mobile1=011

-- ANY / SOME, ALL
-- 검색 : 지역이 경남 사람의 키보다 키가 크거라 같은 사람 출력
SELECT height FROM usertbl WHERE addr='경남';     -- 173, 170

-- ANY / SOME : 서브쿼리의 여러개의 결과 중 한가지만 만족해도 가능 
SELECT height, addr FROM usertbl
WHERE height >= ANY (SELECT height FROM usertbl WHERE addr='경남');    -- 173보다 크거나 같다, 170 크거나 같다

SELECT height, addr FROM usertbl
WHERE height >= SOME (SELECT height FROM usertbl WHERE addr='경남');  

-- ALL : 서브쿼리의 결과 중 여러 개의 결과를 모든 만족해야 함
SELECT height, addr FROM usertbl
WHERE height >= ALL (SELECT height FROM usertbl WHERE addr='경남');    -- 173보다 크면

-- 형식) SELECT [필드명 또는 표현식] 
--      FROM [테이블명 또는 뷰명]
--      WHERE [조건절] 
--      ~~~~
--      ORDER BY [컬럼명]

SELECT name, mDate FROM usertbl
ORDER BY mDate;          -- 오름차순

SELECT name, mDate FROM usertbl
ORDER BY mDate DESC;     -- 내림차순

SELECT name, mDate FROM usertbl
ORDER BY name, mDate;     -- 이름순 오름차순 정렬하되 동명이름인 경우 생일로 오름차순

SELECT name, height FROM usertbl 
ORDER BY height DESC, name ASC;   -- 키가 큰순서로 정렬하되 만약 키가 같을 경우 이름순 정렬

-- 형식) SELECT [필드명 또는 표현식] 
--      FROM [테이블명 또는 뷰명]
--      WHERE [조건절] / 서브쿼리 ANY, ALL
--      ~~~~
--      ORDER BY [컬럼명]
--      LIMIT [조회갯수]

SELECT * FROM usertbl;

SELECT * FROM usertbl
LIMIT 5;        -- 0, 5

SELECT name, height FROM usertbl
ORDER BY height DESC, name ASC
LIMIT 0, 5;	     -- 출력 결과에서 0번째부터 5개 


SELECT name, height FROM usertbl
ORDER BY height DESC, name ASC
LIMIT 2, 5;      -- 출력 결과에서 2번째부터 5개

-- 형식) SELECT [필드명 또는 표현식] 
--      FROM [테이블명 또는 뷰명]
--      WHERE [조건절] / 서브쿼리 ANY, ALL
--      GROUP BY [컬럼명]
--      ORDER BY [컬럼명]
--      LIMIT [조회갯수]

-- 집계함수 : sum, avg, min, max, count
SELECT * FROM buytbl;

SELECT AVG(amount) AS '구매평균',
	   SUM(amount) AS '구매합계',
	   MIN(amount) AS '작은구매수',
	   MAX(amount) AS '큰구매수'
FROM buytbl;

SELECT AVG(price) AS '판매가격평균',
	   SUM(price) AS '판매가격합계',
       MIN(price) AS '작은구매수',
	   MAX(price) AS '큰구매수'
FROM buytbl;

SELECT COUNT(num) FROM buytbl;
SELECT COUNT(*) FROM buytbl;

-- 각 사용자별 구매수와 평균
SELECT userID,
	   sum(amount)
FROM buytbl
GROUP BY userID;

SELECT userID,
	   avg(price),
       sum(price)
FROM buytbl
GROUP BY userID
ORDER BY avg(price) DESC;

SELECT * FROM usertbl;

-- 지역분포 서울 4, 경북 1
SELECT addr, 
	   COUNT(addr) AS '지역분포'
FROM usertbl
GROUP BY addr;

-- 전화번호분포 010:4~~
SELECT mobile1, 
	   COUNT(mobile1) AS '전화번호분포'
FROM usertbl
GROUP BY mobile1;

-- 형식) SELECT [필드명 또는 표현식] 
--      FROM [테이블명 또는 뷰명]
--      WHERE [조건절] / 서브쿼리 ANY, ALL
--      GROUP BY [컬럼명]  / sum, avg, min, max, count
--      HAVING [그룹 조건식]
--      ORDER BY [컬럼명]  / DESC, ASC(생략가능)
--      LIMIT [조회갯수]

SELECT addr, 
	   COUNT(addr) AS '지역분포'
FROM usertbl
GROUP BY addr
HAVING COUNT(addr) >= 2;

SELECT userID,
	   SUM(price * amount) AS '총구매액'
FROM buytbl
GROUP BY userID
HAVING SUM(price * amount) > 1000;

-- ROLLUP : 총합 또는 중간합계 
SELECT num,
	   groupName,
       SUM(price * amount) AS '총구매액'
FROM buytbl
GROUP by groupName, num
WITH ROLLUP;











