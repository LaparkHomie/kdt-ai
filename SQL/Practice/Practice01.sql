CREATE DATABASE sqldb;
USE sqldb;

CREATE TABLE usertbl -- 회원 테이블
( userID     CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  name       VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr        CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1   CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2   CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height       SMALLINT,  -- 키
  mDate       DATE  -- 회원 가입일
);

CREATE TABLE buytbl -- 회원 구매 테이블(Buy Table의 약자)
(  num       INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID     CHAR(8) NOT NULL, -- 아이디(FK)
   prodName    CHAR(6) NOT NULL, --  물품명
   groupName    CHAR(4)  , -- 분류
   price        INT  NOT NULL, -- 단가
   amount       SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (userID) REFERENCES usertbl(userID)
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

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);

SELECT * FROM buytbl;

SELECT * FROM usertbl WHERE Name = '김경호';
select * from usertbl;
SELECT userID, Name FROM usertbl WHERE birthYear >= 1970 AND height >= 182;
SELECT userID, Name, birtyYear, heihht FROM usertbl WHERE birthYear >= 1970 OR height >= 182;
SELECT name, height FROM usertbl WHERE height >= 180 AND height <= 183;
SELECT name, height FROM usertbl WHERE height BETWEEN 180 AND 183;

SELECT name, addr FROM usertbl WHERE addr='경남' OR addr='전남' OR addr='경북';
SELECT name, addr FROM usertbl WHERE addr IN ('경남', '전남', '경북');

SELECT name, height FROM usertbl WHERE name LIKE '김%';
SELECT name, height FROM usertbl WHERE name LIKE '윤__%';

USE sqldb;

SELECT name, height FROM usertbl WHERE height > 177;

SELECT name, height FROM usertbl
	WHERE height > (SELECT height FROM usertbl WHERE name = '김경호');

SELECT name, height FROM usertbl
	WHERE height = any (SELECT height FROM usertbl WHERE name = '경남');

-- 경남에 사는 사람보다 키가 크거나 같은 사람의 이름과 키를 조회
SELECT name, height FROM usertbl
	WHERE height >= (SELECT min(height) FROM usertbl WHERE addr = '경남');

SELECT name, height FROM usertbl
	WHERE height >= ANY (SELECT height FROM usertbl WHERE addr = '경남');

-- 경남에 사는 사람보다 키가 크거나 같은 사람의 이름과 키를 조회
SELECT name, height FROM usertbl
	WHERE height >= (SELECT max(height) FROM usertbl WHERE addr = '경남');

SELECT name, height FROM usertbl
	WHERE height >= ALL (SELECT height FROM usertbl WHERE addr = '경남');

SELECT * FROM usertbl;
SELECT * FROM buytbl;

SELECT userID, name, addr FROM usertbl
	WHERE userID in (SELECT userID FROM buytbl WHERE prodName = '운동화');

-- 정렬 : order by, 오름차순(asc), 내림차순(desc)
SELECT name, mDate FROM usertbl ORDER BY mDate, name ASC;
SELECT name, height FROM usertbl ORDER BY height DESC, name DESC;

SELECT addr, name FROM usertbl ORDER BY addr;
SELECT DISTINCT addr FROM usertbl ORDER BY addr;
SELECT DISTINCT addr, name FROM usertbl ORDER BY addr;

use employees;

SELECT emp_no, hire_date FROM employees
	ORDER BY hire_date ASC
    LIMIT 10, 5;

SELECT emp_no, hire_date FROM employees
	ORDER BY hire_date ASC
    LIMIT 5 OFFSET 10;

USE sqldb;

CREATE TABLE buytbl2 (SELECT * FROM buytbl);
DESC buytbl;
DESC buytbl2;

CREATE TABLE buytbl3 (SELECT userID, prodName FROM buytbl);
SELECT * FROM buytbl3;
desc buytbl3;

SELECT userID, amount FROM buytbl ORDER BY userID;
SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수' FROM buytbl GROUP BY userID;
SELECT userID AS '사용자 아이디', SUM(price * amount) AS '총 구매액'
	FROM buytbl GROUP BY userID;

SELECT AVG(amount) AS '평균 구매 개수' FROM buytbl;
SELECT userID, AVG(amount) AS '평균 구매 개수' FROM buytbl GROUP BY userID;
SELECT userID, AVG(amount) AS '평균 구매 개수' FROM buytbl; -- 집계함수의 기준이 없어 에러
SELECT userID, AVG(amount) AS '평균 구매 개수', price FROM buytbl GROUP BY userID; -- price는 그룹화를 안해야 쓸수있음
SELECT userID, AVG(amount) AS '평균 구매 개수' FROM buytbl; -- avg같은 집계 함수를 사용했을때, 그룹화를 안해서 에러 발생

SELECT name, height
	FROM usertbl
	WHERE height = (SELECT MAX(height) FROM usertbl)
		OR height = (SELECT MIN(height) FROM usertbl);

SELECT COUNT(*) FROM usertbl;
SELECT COUNT(mobile1) FROM usertbl;
SELECT * FROM usertbl;

SELECT userID AS '사용자', SUM(price * amount) AS '총구매액'
	FROM buytbl
	GROUP BY userID
    -- WHERE SUM(price * amount) > 1000
    HAVING SUM(price * amount) > 1000
    ORDER BY '총구매액';

SELECT num, groupName, SUM(price * amount) AS '비용'
	FROM buytbl
    GROUP BY groupName, num
    WITH ROLLUP;

CREATE TABLE testTbl1 (
	id int,
    userName char(3),
    age int
);

INSERT INTO testTbl1 (id, userName, age) VALUES (1, '홍길동', 30);
SELECT * FROM testTbl1;
INSERT INTO testTbl1 VALUES (2, '이기자', 27);
INSERT INTO testTbl1(id, userName) VALUES (3, '김기자');

CREATE TABLE testTbl2 (
	id int AUTO_INCREMENT PRIMARY KEY,
    userName char(3),
    age int
);

INSERT INTO testTbl2 VALUES (NULL, '지민', 25);
INSERT INTO testTbl2 VALUES (NULL, '유나', 22);
INSERT INTO testTbl2 VALUES (NULL, '유경', 21);
SELECT * FROM testTbl2;

SELECT LAST_INSERT_ID();

CREATE TABLE testTbl3 (
	id int AUTO_INCREMENT PRIMARY KEY,
    userName char(3),
    age int
);
ALTER TABLE testTbl3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;
INSERT INTO testTbl3 VALUES (NULL, '나연', 20);
INSERT INTO testTbl3 VALUES (NULL, '정연', 18);
INSERT INTO testTbl3 VALUES (NULL, '모모', 19);
SELECT * FROM testTbl3;

CREATE TABLE testTbl4 (
	id int,
    Fname varchar(50),
    Lname varchar(50)
);

INSERT INTO testTbl4
	SELECT emp_no, first_name, last_name
		FROM employees.employees;

SELECT * FROM testTbl4;

UPDATE testTbl4
	SET Lname = '없음'
    WHERE Fname = 'Georgi';

select * from testTbl4;

UPDATE testTbl4
	SET Lname = '없음', Fname = 'Georgi'
    WHERE id = 10002;

select * from testTbl4;

DELETE FROM testTbl4 WHERE id = 10001;
drop table tableTblr;

SELECT * from testTBl4;

SELECT CAST('2020%12%12' AS DATE);
SELECT CAST('2020@12@12' AS DATE);

SELECT num, CONCAT(CAST(price AS CHAR(10)), 'x',
	CAST(amount AS CHAR(4)), '=') AS '단가X수량',
    price*amount AS '구매액'
    FROM buytbl;

SELECT IF (100>200, '참이다', '거짓이다');
SELECT IFNULL (NULL, '널이군요'), IFNULL(100, '널이군요');
SELECT NULLIF(100,100), IFNULL(200,100);

SELECT CASE 10
	WHEN 1 THEN '일'
    WHEN 5 THEN '오'
    WHEN 10 THEN '십'
    ELSE '모름'
    END AS 'CASE연습';

SELECT ASCII('A'), CHAR(65);

SELECT BIT_LENGTH('abc'), CHAR_LENGTH('abc'), LENGTH('abc');
SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다');

SELECT CONCAT_WS('/', '2025', '01', '01');

SELECT ELT(2, '하나', '둘', '셋'), FIELD('둘', '하나', '둘', '셋'),
	FIND_IN_SET('둘', '하나,둘,셋'), INSTR('하나둘셋', '둘'), LOCATE('둘', '하나둘셋');

SELECT LEFT('abcdefghi', 3), RIGHT('abcdefghi', 3);
SELECT LOWER('abcdEFGH'), UPPER('abcdEFGH');
SELECT LPAD('이것이', 5, '%%'), RPAD('이것이', 5, '##');
SELECT LTRIM('    이것이'), RTRIM('이것이    ');
SELECT TRIM('    이것이    '), TRIM(BOTH 'ㅋ' FROM 'ㅋㅋㅋㅋ재밌어요.ㅋㅋㅋ');

SELECT SUBSTRING('대한민국만세', 3, 3);
SELECT SUBSTRING_INDEX('cafe.naver.com', '.', 1),
	SUBSTRING_INDEX('cafe.naver.com', '.', -1);

SELECT CEILING(4.7), FLOOR(4.7), ROUND(4.7);
SELECT CEILING(-4.7), FLOOR(-4.7), ROUND(-4.7);

SELECT ADDDATE('2025-01-01', INTERVAL 31 DAY), ADDDATE('2025-01-01', INTERVAL 1 MONTH);
SELECT SUBDATE('2025-01-01', INTERVAL 31 DAY), SUBDATE('2025-01-01', INTERVAL 1 MONTH);
SELECT ADDTIME('2025-01-01 23:59:59', '1:1:1'), ADDTIME('15:00:00', '2:10:10');
SELECT SUBTIME('2025-01-01 23:59:59', '1:1:1'), SUBTIME('15:00:00', '2:10:10');
SELECT YEAR(CURDATE()), MONTH(CURDATE()), DAYOFMONTH(CURDATE());
SELECT HOUR(CURTIME()), MINUTE(CURRENT_TIME()), SECOND(CURRENT_TIME), MICROSECOND(CURRENT_TIME);

SELECT NOW(), DATE(NOW()), TIME(NOW());

SELECT *
	FROM buytbl
		INNER JOIN usertbl
			ON buytbl.userID = usertbl.userID
		WHERE buytbl.userID = 'JYP';

SELECT *
	FROM buytbl
		INNER JOIN usertbl
			ON buytbl.userID = usertbl.userID
		ORDER BY num;

SELECT buytbl.userID, name, prodName, addr, mobile1 + mobile2 AS '연락처'
	FROM buytbl
		INNER JOIN usertbl
			ON buytbl.userID = usertbl.userID
		ORDER BY num;

SELECT B.userID, U.name, B.prodName, U.addr, U.mobile1 + U.mobile2 AS '연락처'
	FROM buytbl B
		INNER JOIN usertbl U
			ON B.userID = U.userID
		ORDER BY B.num;


CREATE TABLE stdtbl 
( stdName    VARCHAR(10) NOT NULL PRIMARY KEY,
  addr     CHAR(4) NOT NULL
);
CREATE TABLE clubtbl 
( clubName    VARCHAR(10) NOT NULL PRIMARY KEY,
  roomNo    CHAR(4) NOT NULL
);
CREATE TABLE stdclubtbl
(  num int AUTO_INCREMENT NOT NULL PRIMARY KEY, 
   stdName    VARCHAR(10) NOT NULL,
   clubName    VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdtbl(stdName),
FOREIGN KEY(clubName) REFERENCES clubtbl(clubName)
);
INSERT INTO stdtbl VALUES ('김범수','경남'), ('성시경','서울'), ('조용필','경기'), ('은지원','경북'),('바비킴','서울');
INSERT INTO clubtbl VALUES ('수영','101호'), ('바둑','102호'), ('축구','103호'), ('봉사','104호');
INSERT INTO stdclubtbl VALUES (NULL, '김범수','바둑'), (NULL,'김범수','축구'), (NULL,'조용필','축구'), (NULL,'은지원','축구'), (NULL,'은지원','봉사'), (NULL,'바비킴','봉사');

SELECT * FROM stdtbl;
SELECT * FROM clubtbl;
SELECT * FROM stdclubtbl;

SELECT S.stdName, S.addr, SC.clubName, C.roomNo
	FROM stdtbl S
		INNER JOIN stdclubtbl SC
			ON S.stdName = Sc.stdName
		INNER JOIN clubtbl C
			ON SC.clubName = C.clubName
	ORDER BY S.stdName;

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
	FROM usertbl U
		LEFT OUTER JOIN buytbl B
			ON U.userId = B.userID
		ORDER BY U.userID;

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
	FROM usertbl U
		RIGHT OUTER JOIN buytbl B
			ON U.userId = B.userID
		ORDER BY U.userID;

SELECT COUNT(*) FROM usertbl;
SELECT COUNT(*) FROM buytbl;


CREATE TABLE empTbl (emp CHAR(3), manager CHAR(3), empTel VARCHAR(8));

INSERT INTO empTbl VALUES('나사장',NULL,'0000');
INSERT INTO empTbl VALUES('김재무','나사장','2222');
INSERT INTO empTbl VALUES('김부장','김재무','2222-1');
INSERT INTO empTbl VALUES('이부장','김재무','2222-2');
INSERT INTO empTbl VALUES('우대리','이부장','2222-2-1');
INSERT INTO empTbl VALUES('지사원','이부장','2222-2-2');
INSERT INTO empTbl VALUES('이영업','나사장','1111');
INSERT INTO empTbl VALUES('한과장','이영업','1111-1');
INSERT INTO empTbl VALUES('최정보','나사장','3333');
INSERT INTO empTbl VALUES('윤차장','최정보','3333-1');
INSERT INTO empTbl VALUES('이주임','윤차장','3333-1-1');

SELECT * FROM empTbl;

-- 우대리의 직속 상관의 이름과 연락처를 조회하시오.
SELECT A.emp AS '부하직원', B.emp AS '직속상관', B.empTel AS '직속상관연락처'
	FROM empTbl A
		INNER JOIN empTbl B
			ON A.manager = B.emp
		WHERE A.emp = '우대리';

SELECT emp AS '부하직원', manager AS '직속상관', empTel AS '직속상관연락처'
	FROM empTbl
		WHERE empTbl.emp = '우대리';

SELECT stdName, addr FROM stdtbl
	UNION ALL
SELECT clubName, roomNo FROM clubtbl;

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM usertbl
	WHERE name NOT IN (SELECT name FROM usertbl WHERE mobile1 IS NULL);
SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM usertbl
	WHERE name IN (SELECT name FROM usertbl WHERE mobile1 IS NULL);