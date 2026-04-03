USE 한빛무역;

-- 1번
SELECT * FROM 고객;

-- 2번
SELECT 고객번호, 담당자명, 고객회사명 FROM 고객;

-- 3번
SELECT 고객번호, 담당자명, 마일리지 FROM 고객 WHERE 마일리지 >= 100000;

-- 4번
SELECT * FROM 고객 WHERE 담당자명 LIKE '김%' AND 담당자직위 = '영업 사원';

-- 5번
SELECT 고객번호, 고객회사명, 담당자명 FROM 고객 WHERE 도시 IN ('서울특별시', '인천광역시', '대구광역시');
