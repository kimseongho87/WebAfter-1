USE example;
-- 학생 테이블 
-- ctrl + / : 키보드 영문 - 블럭전체주석
CREATE TABLE student(
	stu_no CHAR(15), 				 	  -- 학번
    stu_name VARCHAR(12) NOT NULL,   	  -- 이름
	stu_dept VARCHAR(20) NOT NULL,   	  -- 학과
    stu_grade CHAR(2) NOT NULL,       	  -- 학년
    stu_class CHAR(2) NOT NULL,           -- 반
    stu_gender CHAR(2) CHECK(stu_gender IN('M', 'F')),   -- 성별
    stu_height DECIMAL(5, 2),               -- 신장
    stu_weight DECIMAL(5, 2), 			    -- 체중
    
    CONSTRAINT PK_stu_stu_no PRIMARY KEY(stu_no)
);
DESC student;

INSERT INTO student VALUES(20153075, '옥한빛', '기계', 1, 'C', 'M', 177.8, 80);
INSERT INTO student VALUES(20153088, '이태연', '기계', 1, 'C', 'F', 162.2, 50);
INSERT INTO student VALUES(20143054, '유가인', '기계', 2, 'C', 'F', 154.3, 47);

INSERT INTO student VALUES(20152088, '조민우', '전기전자', 1, 'C', 'M', 188.7, 90);
INSERT INTO student VALUES(20142021, '심수정', '전기전자', 2, 'A', 'F', 168, 45);
INSERT INTO student VALUES(20132003, '박희철', '전기전자', 3, 'B', 'M', null, 63);
INSERT INTO student VALUES(20151062, '김인중', '컴퓨터정보', 1, 'B', 'M', 166, 67);
INSERT INTO student VALUES(20141007, '진현무', '컴퓨터정보', 2, 'A', 'M', 174, 64);
INSERT INTO student VALUES(20131001, '김종헌', '컴퓨터정보', 3, 'C', 'M', null, 72);
INSERT INTO student VALUES(20131025, '옥성우', '컴퓨터정보', 3, 'A', 'F', 177, 63);
SELECT * FROM student ORDER BY stu_name;

-- 과목 테이블
CREATE TABLE subject(
	sub_no CHAR(3),                     -- 과목번호
    sub_name VARCHAR(30),               -- 과목이름 
    sub_prof VARCHAR(12),               -- 교수명
    sub_grade CHAR(2),                	-- 학년
    sub_dept VARCHAR(20),               -- 학과
    
    CONSTRAINT PK_sub_sub_no PRIMARY KEY(sub_no)
);
DESC subject;

INSERT INTO subject VALUES('111', '데이터베이스', '이재영', 2, '컴퓨터정보');
INSERT INTO subject VALUES('110', '자동제어', '정순정', 2, '전기전자');
INSERT INTO subject VALUES('109', '자동화설계', '박민영', 3, '기계');

INSERT INTO subject VALUES('101', '컴퓨터개론', '강종영', 3, '컴퓨터정보');
INSERT INTO subject VALUES('102', '기계공작법', '김태영', 1, '기계');
INSERT INTO subject VALUES('103', '기초전자실험', '김유석', 1, '전기전자');
INSERT INTO subject VALUES('104', '시스템분석설계', '강석현', 3, '컴퓨터정보');
INSERT INTO subject VALUES('105', '기계설계', '김명성', 1, '기계');
INSERT INTO subject VALUES('106', '전자회로실험', '최영민', 3, '전기전자');
INSERT INTO subject VALUES('107', 'CAD응용실습', '구봉규', 2, '기계');
INSERT INTO subject VALUES('108', '소프트웨어공학', '권민성', 1, '컴퓨터정보');

SELECT * FROM subject ORDER BY sub_no;

-- 수강 테이블
CREATE TABLE enrol(
	sub_no CHAR(3),       -- 과목번호 / subject 필드 참조
    stu_no CHAR(15),      -- 학번  / student 필드 참조
    enr_grade SMALLINT,    -- 수강번호
    
	CONSTRAINT FK_enrol_sub_no FOREIGN KEY(sub_no) REFERENCES subject(sub_no),
    CONSTRAINT FK_enrol_stu_no FOREIGN KEY(stu_no) REFERENCES student(stu_no)
);
DESC enrol;

INSERT INTO enrol VALUES('104', '20131001', 56);
INSERT INTO enrol VALUES('106', '20132003', 72);
INSERT INTO enrol VALUES('103', '20152088', 45);

INSERT INTO enrol VALUES('101', '20131025', 65);
INSERT INTO enrol VALUES('104', '20131025', 65);
INSERT INTO enrol VALUES('102', '20153075', 66);
INSERT INTO enrol VALUES('105', '20153075', 56);
INSERT INTO enrol VALUES('102', '20153088', 61);
INSERT INTO enrol VALUES('105', '20153088', 78);
INSERT INTO enrol VALUES('107', '20143054', 41);
-- INSERT INTO enrol VALUES('108', '20151062', 81);

SELECT * FROM enrol ORDER BY enr_grade;
 
-- 조인 연습
SELECT enr.enr_grade '수강번호',
	   stu.stu_no '학번',
       stu.stu_name '이름',
       stu.stu_dept '학과',
       
       sub.sub_prof '교수',
       sub.sub_name '과목명'
FROM enrol AS enr
INNER JOIN student AS stu
ON stu.stu_no = enr.stu_no
INNER JOIN subject AS sub
ON sub.sub_no = enr.sub_no;

-- 제약조건 삭제
SELECT * FROM subject;
DELETE FROM subject WHERE sub_no='108';    -- ERROR

SET foreign_key_checks = 0;                -- 제약조건 활성
 
DELETE FROM subject WHERE sub_no='108';    -- 삭제
SELECT * FROM subject;

SET foreign_key_checks = 1;                -- 제약조건 비활성
DELETE FROM subject WHERE sub_no='107';    -- 확인 

ALTER TABLE enrol DROP CONSTRAINT FK_enrol_sub_no;   -- 참조키를 삭제

-- 참조키를 다시 만든 후 참조키 수정,삭제 용이
ALTER TABLE enrol 
ADD CONSTRAINT FK_enrol_sub_no FOREIGN KEY(sub_no) REFERENCES subject(sub_no)
ON DELETE CASCADE ON UPDATE CASCADE;
desc enrol;

SELECT * FROM subject;
SELECT * FROM enrol;

DELETE FROM subject WHERE sub_no='102';
UPDATE subject SET sub_no='999' WHERE sub_no='105';

-- 사용자 테이블
CREATE TABLE users (
  user_id VARCHAR(10),              -- 사용자 아이디
  username VARCHAR(50) NOT NULL,    -- 사용자 이름
  email VARCHAR(100) UNIQUE,        -- 이메일
  
  CONSTRAINT PK_user_id PRIMARY KEY(user_id)
);
DESC users;

INSERT INTO users VALUES(1, 'John Doe', 'john@example.com');
INSERT INTO users VALUES(2, 'Jane Smith', 'jane@example.com');
INSERT INTO users VALUES(3, 'Michael Johnson', 'michael@example.com');
SELECT * FROM users;

-- 주문 테이블
CREATE TABLE orders (
  order_id VARCHAR(10),    -- 주문번호
  user_id VARCHAR(10),     -- 사용자아이디
  product_name VARCHAR(100),  -- 상품명
  order_date DATE,           -- 날짜
  
  CONSTRAINT PK_order_id PRIMARY KEY(order_id),
  CONSTRAINT FK_user_id FOREIGN KEY(user_id) REFERENCES users(user_id) 
  ON UPDATE CASCADE ON DELETE CASCADE
);
DESC orders;

INSERT INTO orders VALUES(101, 1, 'Product A', '2023-07-24');
INSERT INTO orders VALUES(102, 1, 'Product B', '2023-07-25');
INSERT INTO orders VALUES(103, 2, 'Product C', '2023-07-23');
INSERT INTO orders VALUES(104, 3, 'Product D', '2023-07-22');

SELECT * FROM users;
SELECT * FROM orders;

-- 두테이블 영향을 받아서 테이블 레코드가 다 수정된다.
DELETE FROM users WHERE user_id='1';	

-- 두테이블 영향을 받아서 테이블의 레코드가 다 수정된다.
UPDATE users SET user_id='20' WHERE user_id='2';

USE example;
CREATE TABLE datetest(
	a DATE, 		-- 날짜
    b TIME,			-- 시분초
    c DATETIME      -- 날짜시간
);
DESC datetest;

INSERT INTO datetest VALUES('2023-07-28', '12:00:27', '2023-07-27 12:00:10');
SELECT * FROM datetest;
INSERT INTO datetest VALUES(CURDATE(), CURTIME(), SYSDATE());



















