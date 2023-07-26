-- 5. JOIN : 두개 이상의 테이블 서로 묶어서 하나의 결과 집합으로 만듬
-- 5-1) INNER JOIN(내부조인) : 가장 많이 사용, 일반적으로 join은 내부조인
-- SELECT <열 목록>
-- FROM <첫번째 테이블>
-- INNER JOIN <두번째 테이블>
-- ON <조인될조건>
-- [WHERE 검색조건]

SELECT * FROM buytbl;
SELECT * FROM usertbl;

-- 회원테이블, 구매테이블 
SELECT * FROM buytbl
INNER JOIN usertbl
ON buytbl.userID=usertbl.userID;

-- 회원테이블, 구매테이블에서 원하는 필드만 출력
SELECT num, 
	   name, 
       prodName, 
       addr, 
       buytbl.userID 
FROM buytbl
INNER JOIN usertbl
ON buytbl.userID=usertbl.userID;

-- 테이블 결합시 ALIAS 사용
SELECT U.userID,
	   U.name,
       B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl AS U
INNER JOIN buytbl AS B
ON U.userID=B.userID
ORDER BY U.userID;  

-- 두개의 테이블에서 JYP 정보만 출력
SELECT U.userID,
	   U.name, 
	   B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buytbl B
INNER JOIN usertbl U
ON U.userID=B.userID
WHERE B.userID='JYP';     --  U.userID='JYP'

-- 쇼핑몰에서 한번이상 구매한 회원에게 감사 안내문 발송 : 중복값제거
SELECT DISTINCT U.userID,
	   U.name,
       U.addr
FROM usertbl U
INNER JOIN buytbl B
ON U.userID=B.userID
ORDER BY U.userID;

-- 구매한적이 없는 회원까지 모두 출력
SELECT U.userID,
	   U.name, 
	   B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
LEFT OUTER JOIN buytbl B     -- usertabl 모두것이 출력
ON U.userID=B.userID
ORDER BY U.userID;

SELECT U.userID,
	   U.name, 
	   B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buytbl B
RIGHT OUTER JOIN usertbl U     -- usertabl 모두것이 출력
ON U.userID=B.userID
ORDER BY U.userID;

-- 구매기록이 없는 유령회원만 출력 
SELECT U.userID,
	   U.name,
       B.prodName,
       U.addr,
	   CONCAT(U.mobile1, U.mobile2) '연락처'
FROM usertbl U
LEFT OUTER JOIN buytbl B
ON U.userID=B.userID
WHERE B.prodName IS NULL
ORDER BY U.userID;

-- CORSS JOIN 상호조인 : 샘플데이터 만들때 사용
SELECT count(*) FROM buytbl;   -- 12
SELECT count(*) FROM usertbl;  -- 10  = 10*12=120

SELECT * FROM buytbl
CROSS JOIN usertbl;

-- SELF JOIN 자체 조인 
SELECT * FROM employees;

-- 각 사원의 관리자 출력
SELECT e.EMPLOYEE_ID,
	   e.FIRST_NAME,
       e.MANAGER_ID,
       m.FIRST_NAME
FROM employees e                  -- 사원
INNER JOIN employees m			  -- 관리자	
ON e.MANAGER_ID=m.EMPLOYEE_ID;

-- Steven의 팀원들 출력
SELECT e.EMPLOYEE_ID,
	   e.FIRST_NAME,
       e.MANAGER_ID,
       m.FIRST_NAME
FROM employees e
INNER JOIN employees m
ON e.MANAGER_ID=m.EMPLOYEE_ID
WHERE m.FIRST_NAME='Steven';











