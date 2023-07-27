-- 테이블 : 숫자(정수, 실수), 문자(특수문자)
create table test(
	-- 숫자
	a DECIMAL(3), 		-- 숫자 자리수 
    b DECIMAL(6, 1),    -- 전체 자리수 / 정수 5, 실수 1
    c SMALLINT,         -- 2byte 32,768 ~ -32,767
    
    -- 문자
    x VARCHAR(10),      -- 1~65535 / 영문자 10글자, 한글 3글자 / 김(3개 차지)
    y CHAR(5)           -- 1~255
);

-- 숫자(정수, 실수): 1, 2.5
-- 문자(특수문자) : apple, 010-123-125, apple-1
-- 설계(상황따라서) : 202301235 학번, 1001 사원번호 / 123-123-789 = -제거후 123123789 숫자

-- 제약키 : PRIMARY KEY(학번, 군번, 주민번호), UNIQUE KEY(동아리방번호), NOT NULL(이름....), 
--        CHECK(나이:1~150, 남자:M, F....), DEFULAT(회원등급, 총점), FOREING KEY(A table, B table 참조)

-- SELECT : SELECT ~~ FROM ~~ WEHRE ~~~ GROUP BY ~~ HAVING ~~ ORDER BY ~~ LIMIT
--          SELECT ~~ FROM ~~ WEHER(SubQuery / ANY, ALL) ~~ GROUP BY(집계함수 avg(), min()....)
-- JOIN : INNER JOIN, QUTER JOIN, SELF JOIN

-- DML(레코드) : SELECT, INSERT
-- INSERT INTO table명 VALUES(값1, 값2...)
-- INSERT INTO table명(컬럼명1, 컬럼명2,.....) VALUES(값1, 값2....) : NULL 허용시 원하는 필드에 값만 삽입할때

-- DDL(테이블) : 테이블 추가, 삭제, 필드명 추가/삭제/수정
-- CREATE ~~, DROP ~~~, ALTER TABLE [ADD, DROP, MODIFI, CHANGE]


