-- 세현님 코드 인용
CREATE DATABASE projectdb;
USE projectdb;

SELECT * FROM pop_2021;
SELECT * FROM pop_2022;
SELECT * FROM pop_2023;
SELECT * FROM pop_2024;

DROP TABLE IF EXISTS poptbl;
CREATE TABLE poptbl AS
	SELECT * FROM pop_2021 UNION ALL
	SELECT * FROM pop_2022 UNION ALL
	SELECT * FROM pop_2023 UNION ALL
	SELECT * FROM pop_2024;

SELECT * FROM poptbl;

-- 파이썬 코드 실행 후, 2021년부터 2042년까지 담겨있는지 확인
SELECT * FROM poptbl;


-- 연령별 입대 확률
CREATE TABLE agetbl (
	age INT PRIMARY KEY,
	rate FLOAT
);

INSERT INTO agetbl (age, rate) VALUES
(19, 0.043081), (20, 0.627356), (21, 0.194951), (22, 0.059142), (23, 0.028271), (24, 0.016587),
(25, 0.005102), (26, 0.005102), (27, 0.005102), (28, 0.005102), (29, 0.005102), (30, 0.005102);

-- 군별 복무기간 및 할당 비율 테이블 (df_soldier.T 데이터 기반)
CREATE TABLE inputtbl (
	name VARCHAR(10) PRIMARY KEY,
	month INT,
	rate FLOAT
);

-- df_soldier.T 예시 입력값
INSERT INTO inputtbl (name, month, rate) VALUES
('육군', 18, 0.70),
('해군', 20, 0.10),
('공군', 22, 0.10),
('해병대', 18, 0.10);

-- 연도별/연령별 복무 현황 시뮬레이션 테이블
CREATE TABLE militarytbl (
	year INT,
	age INT,
	total_pop INT,          -- ① 해당 연도/나이의 총 남성 인구 (poptbl에서 옴)
	new_enlist INT,         -- ② 당해 신규 입대자 (total_pop * enlist_rate_tbl.rate)
	serving_army INT,       -- ③ 복무중 (육군)
	serving_navy INT,       -- ③ 복무중 (해군)
	serving_air INT,        -- ③ 복무중 (공군)
	serving_marine INT,     -- ③ 복무중 (해병대)
	total_serving INT,      -- ④ 총 복무중 인원 (위 4개 합)
	discharged INT,         -- ⑤ 군필 (전역자 누적)
	unlisted INT,           -- ⑥ 미필 (total_pop - total_serving - discharged)

	PRIMARY KEY (year, age)
);

SELECT * FROM militarytbl;
