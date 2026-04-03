SELECT * FROM tabledb.usertbl;

desc usertbl;

CREATE TABLE usertbl(					-- 회원 테이블
	userID		CHAR(8) PRIMARY KEY,	-- 사용자 아이디
	name		VARCHAR(10),			-- 이름
	birthYear	INT,					-- 출생년도
    addr		CHAR(2),				-- 지역(경기, 서울, 경남 등오르 글자만 입력)
    mobile1		CHAR(3),				-- 휴대폰의국번(001, 016, 017, 018, 019, 010 등)
    mobile2		CHAR(8),				-- 휴대폰의 나머지 전화번호(하이픈 제외)
    height		SMALLINT,				-- 키
    mDate		DATE					-- 회원 가입일	
);

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

SELECT * FROM usertbl;

CREATE TABLE buytbl(
	num			INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userid		CHAR(8) NOT NULL,
    prodName	CHAR(6) NOT NULL,
    groupName	CHAR(4),
    price		INT NOT NULL,
    amount		SMALLINT NOT NULL,
    FOREIGN KEY(userid) REFERENCES usertbl(userID)
);

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL, 30, 2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200, 1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);

select * from usertbl;
select * from buytbl;

DROP TABLE IF EXISTS prodTbl;
CREATE TABLE prodTbl(
	prodCode	CHAR(3) NOT NULL,
    prodId		CHAR(4) NOT NULL,
    prodDate	DATETIME NOT NULL,
    prodCur		CHAR(10) NULL -- ,
    -- CONSTRAINT	PK_prodTbl_proCode_prodID PRIMARY KEY (prodCode, prodID)
);

desc prodTbl;

ALTER TABLE prodTbl
	ADD CONSTRAINT PK_prodTbl_proCode_prodID PRIMARY KEY (prodCode, prodID);
ALTER TABLE prodTbl
	DROP primary key;
SHOW INDEX FROM prodTbl;

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'tabledb' AND table_name="usertbl";

DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl(
	userID		CHAR(8)		PRIMARY KEY,
	name		VARCHAR(10),
	birthYear	INT CHECK	(birthYear >= 1900 AND birtyYear <= 2023),
	mobile1		CHAR(3) NULL,
	CONSTRAINT	CK_name CHECK ( name IS NOT NULL)
);

ALTER TABLE usertbl drop CONSTRAINT CK_name;

DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL (
	userID		CHAR(8) NOT NULL PRIMARY KEY,
    name		VARCHAR(10) NOT NULL,
    birthYear	INT NOT NULL DEFAULT -1,
    addr		CHAR(2) NOT NULL DEFAULT '서울',
    mobile1		CHAR(3) NULL,
    mobile2		CHAR(8) NULL,
    height		SMALLINT NULL DEFAULT 170,
    mDate		DATE NULL
);

DESC usertbl;

ALTER TABLE usertbl
	ALTER COLUMN mobile1 SET DEFAULT '010';

ALTER TABLE usertbl
	CHANGE height he INT;
   
ALTER TABLE usertbl
	MODIFY he SMALLINT;

USE tabledb;
ALTER TABLE usertbl
	ADD homepage VARCHAR(30)				-- 열추가
		DEFAULT 'http://www.hanbit.co.kr'	-- 디폴트값
        NULL;								-- Null 허용함

ALTER TABLE usertbl
	ADD homepage2 VARCHAR(30)
		DEFAULT 'http://www.hanbit.co.kr' AFTER he;

ALTER TABLE usertbl
	CHANGE COLUMN name uName VARCHAR(20) NULL;

ALTER TABLE usertbl
	DROP COLUMN homepage;

DESC usertbl;

DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl 
( userID  CHAR(8), 
  name    VARCHAR(10),
  birthYear   INT,  
  addr     CHAR(2), 
  mobile1   CHAR(3), 
  mobile2   CHAR(8), 
  height    SMALLINT, 
  mDate    DATE 
);

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', NULL, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1871, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');

DROP TABLE IF EXISTS buytbl;
CREATE TABLE buytbl 
(  num int AUTO_INCREMENT PRIMARY KEY,
   userid  CHAR(8),
   prodName CHAR(6),
   groupName CHAR(4),
   price     INT ,
   amount   SMALLINT
);

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL,'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL,'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL,'BBK', '모니터', '전자', 200,  5);
DELETE FROM buytbl WHERE userid = 'BBK';

SELECT * FROM buytbl;

ALTER TABLE usertbl
	ADD CONSTRAINT PK_usertbl_userID PRIMARY KEY (userID);

ALTER TABLE buytbl
	ADD CONSTRAINT FK_usertbl_buytbl FOREIGN KEY (userid) REFERENCES usertbl(userID);


SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'tabledb' AND table_name="usertbl";

CREATE VIEW v_usertbl
AS
SELECT userid, name, addr FROM usertbl;

SELECT table_schema, table_name, table_type
FROM information_schema.TABLES
WHERE table_type LIKE 'VIEW' AND table_schema = 'tabledb';

SELECT * FROM v_usertbl;
SELECT userid, name FROM v_usertbl;

CREATE VIEW v_userbuytbl
AS
SELECT U.userid, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	INNER JOIN buytbl B
		ON U.userid = B.userid;

SHOW FULL TABLES IN tabledb
WHERE table_type like 'VIEW';

SELECT * FROM v_userbuytbl;
SELECT userid, name, prodName FROM v_userbuytbl;

SHOW CREATE VIEW v_userbuytbl;
