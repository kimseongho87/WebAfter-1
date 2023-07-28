-- VIEW : 보안상, 반복적인 긴 퀴리문 작성
USE shop;

-- 일반 선택문 내가 원하는 필드 출력
SELECT * FROM usertbl;
SELECT userid, name, addr FROM usertbl;

-- VIEW로 내가 필요한 가상의 테이블 만듬
CREATE VIEW v_usertbl 
AS 
SELECT userid, name, addr FROM usertbl;

SELECT * FROM v_usertbl;
SELECT * FROM v_usertbl WHERE name='바비킴';
SELECT userid, addr FROM v_usertbl WHERE addr='서울';

-- 긴쿼리문 작성
SELECT U.userid,
	   U.name,
       B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
INNER JOIN buytbl B
ON U.userid=B.userid
ORDER BY U.userid;

-- VIEW 만듬
CREATE VIEW v_join_inner 
AS 
SELECT U.userid,
	   U.name,
       B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
INNER JOIN buytbl B
ON U.userid=B.userid
ORDER BY U.userid;

SELECT * FROM v_join_inner;
SELECT * FROM v_join_inner WHERE name='바비킴';

DESC v_join_inner;
SELECT userid, prodName FROM v_join_inner;

-- 유령회원 
SELECT U.userID,
	   U.name,
       B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS 'phone'
FROM usertbl U      
LEFT OUTER JOIN buytbl B    
ON U.userID=B.userID
WHERE B.prodName IS NULL
ORDER BY U.userID;

CREATE VIEW v_join_outer
AS
SELECT U.userID,
	   U.name,
       B.prodName,
       U.addr,
       CONCAT(U.mobile1, U.mobile2) AS 'phone'
FROM usertbl U      
LEFT OUTER JOIN buytbl B    
ON U.userID=B.userID
WHERE B.prodName IS NULL
ORDER BY U.userID;

SELECT * FROM v_join_outer;

-- 뷰삭제
DROP VIEW v_join_inner;
DROP VIEW v_join_outer;

-- index 
USE example;
CREATE TABLE person(
	num SMALLINT,
	name VARCHAR(20),
	ki DECIMAL(5, 1)
); 
DESC person;
INSERT INTO person VALUES(1, '홍길동', 177.7);
INSERT INTO person VALUES(2, '박길동', 167.7);
INSERT INTO person VALUES(3, '조길동', 187.7);
INSERT INTO person VALUES(4, '이길동', 197.7);
INSERT INTO person VALUES(5, '홍길동', 167.7);
INSERT INTO person VALUES(6, '전길동', 167.7);
INSERT INTO person VALUES(7, '민길동', 187.7);
INSERT INTO person VALUES(8, '최길동', 177.7);

SELECT * FROM person;
SELECT * FROM person WHERE num=5;

-- primary key 추가해서 index 확인해보기
ALTER TABLE person ADD CONSTRAINT PK_person_num PRIMARY KEY(num);
DESC person;
SELECT * FROM person WHERE num=5;

-- 트랜잭션 : 하나의 작업 흐름 (select, insert, update, delete)
SELECT * FROM person;

START TRANSACTION;    -- 시작
DELETE FROM person WHERE num=8;
ROLLBACK;     		  -- 되돌리기

START TRANSACTION;
DELETE FROM person WHERE num=1;
COMMIT;     		  -- 실행





