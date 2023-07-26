-- DDL(Data Definition Language, 데이터 정의 언어) : 테이블 생성, 삭제, 변경
-- DML(Data Manipulation Language, 데이터 조작 언어) : 레코드 삽입, 삭제, 수정, 선택

-- 테이블 생성
CREATE TABLE person(
	bunho SMALLINT,
    name VARCHAR(20),
    ki DECIMAL(5, 1)
);
DESC person;
SELECT * FROM person;

-- 테이블 삭제
DROP TABLE person;

CREATE TABLE addr(
	irum VARCHAR(15),
	phone VARCHAR(20),    -- telphone
    address VARCHAR(200),
	email VARCHAR(100)
);
DESC addr;
SELECT * FROM addr;

-- 컬럼 추가 
ALTER TABLE addr ADD(tel VARCHAR(15));

-- 컬럼 삭제
ALTER TABLE addr DROP tel;

-- 수정 : 컬럼 속성 변경
ALTER TABLE addr MODIFY irum VARCHAR(30);

-- 수정 : 컬럼명 변경
ALTER TABLE addr CHANGE phone telphone VARCHAR(20);

-- 데이터 추가 
-- 첫번째 방법) INSERT INTO 테이블명 VALUES(값1, 값2....)
INSERT INTO addr VALUES('홍길동', '010-123-1234', '서울시 강남구 역삼1동', 'hong@naver.com');
INSERT INTO addr VALUES('박길동', '010-123-4567', '서울시 강남구 압구정동', 'park@hanmail.net');
INSERT INTO addr VALUES('박길동', '010-123-4567', '서울시 강남구 압구정동', 'park@hanmail.net');
INSERT INTO addr VALUES(null, null, '서울시 강남구 압구정동', 'park@hanmail.net');

-- 두번째 방법) INSERT INTO(컬럼명1, 컬럼명1) VALUES(값1, 값2)
INSERT INTO addr(irum, address) VALUES('이영자', '서울시 강남구');
INSERT INTO addr(email) VALUES('apple@naver.com');
SELECT * FROM addr;

-- 제약조건
-- 학생 테이블 
CREATE TABLE stdtbl(
	stdbunho DECIMAL(10) PRIMARY KEY,         -- 중복불가 /NULL불가
    stdname VARCHAR(20) NOT NULL,             -- 중복허용 /NULL불가
    email VARCHAR(100) UNIQUE                 -- 중복불가 /NULL허용
);
DESC stdtbl;
INSERT INTO stdtbl VALUES(1001, '홍길동', 'h@hanmail.net');
INSERT INTO stdtbl VALUES(1002, '박길동', 'p@hanmail.net');
INSERT INTO stdtbl VALUES(1003, '김길동', 'k@hanmail.net');

-- INSERT INTO stdtbl VALUES(1001, '이영자', 'l@naver.com'); 중복불가
-- INSERT INTO stdtbl VALUES(null, '이영자', 'l@naver.com'); NULL불가

INSERT INTO stdtbl VALUES(1004, '김길동', 'd@hanmail.net');    -- 중복허용
-- INSERT INTO stdtbl VALUES(1005, null, 'ki@hanmail.net');  NULL불가

INSERT INTO stdtbl VALUES(1005, '조인성', null); 
-- INSERT INTO stdtbl VALUES(1006, '박인성', 'k@hanmail.net');   중복불가
SELECT * FROM stdtbl;

-- 학생 동아리 테이블
CREATE TABLE clubtbl(
	clubname VARCHAR(10) PRIMARY KEY,    --  중복불가/NULL불가
    roomno CHAR(4) UNIQUE                --  중복불가/NULL허용
);
SELECT * FROM clubtbl;
DESC clubtbl;

INSERT INTO clubtbl VALUES('수영', '101호');
INSERT INTO clubtbl(clubname) VALUES('바둑');
-- INSERT INTO clubtbl VALUES('바둑', null);
INSERT INTO clubtbl VALUES('축구', '103호');
INSERT INTO clubtbl VALUES('봉사', '104호');

-- 동아리 테이블
CREATE TABLE stdclubtbl(
	num SMALLINT PRIMARY KEY,
    stdbunho DECIMAL(10) NOT NULL,
    clubname VARCHAR(10) NOT NULL,
    
	FOREIGN KEY(stdbunho) REFERENCES stdtbl(stdbunho),
    FOREIGN KEY(clubname) REFERENCES clubtbl(clubname)
);
DESC stdclubtbl;

SELECT * FROM stdtbl;    -- stdbunho(1001 ~ 1005)
SELECT * FROM clubtbl;   -- clubtbl(바둑, 수영, 축구, 봉사)

INSERT INTO stdclubtbl VALUES(1, 1001, '바둑');
INSERT INTO stdclubtbl VALUES(2, 1001, '수영');
INSERT INTO stdclubtbl VALUES(3, 1003, '봉사');

-- INSERT INTO stdclubtbl VALUES(4, 5000, '봉사');
-- INSERT INTO stdclubtbl VALUES(5, 1002, '음악감상');

INSERT INTO stdclubtbl VALUES(4, 1002, '축구');
INSERT INTO stdclubtbl VALUES(5, 1004, '바둑');

SELECT * FROM stdclubtbl;

-- 3개의 테이블 조인 / 학생을 기준으로 학생번호, 이름, 가입한 동아리, 동아리방







