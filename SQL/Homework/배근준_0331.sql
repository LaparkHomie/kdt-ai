/* ---- 조인 ---- */
USE 한빛무역;
-- 1. ‘이소미’ 사원의 사원번호, 직위, 부서번호, 부서명을 보이시오.
SELECT stf.사원번호, stf.직위, stf.부서번호, stf.부서번호, dpt.부서명
	FROM 사원 stf
		INNER JOIN 부서 dpt
			ON stf.부서번호 = dpt.부서번호
		WHERE stf.이름 = '이소미';

SELECT * FROM 사원;
SELECT * FROM 부서;

-- 2. 고객 회사들이 주문한 주문건수를 주문건수가 많은 순서대로 보이시오. 이때 고객 회사의 정보로는 고객번호, 담당자명, 고객회사명을 보이시오.
SELECT COUNT(ord.고객번호) 주문건수, cus.고객번호, cus.담당자명, cus.고객회사명
	FROM 고객 cus
		INNER JOIN 주문 ord
			ON cus.고객번호 = ord.고객번호
		GROUP BY ord.고객번호
		ORDER BY 주문건수 DESC;

SELECT * FROM 고객;
SELECT * FROM 주문;

-- 3. 고객별(고객번호, 담당자명, 고객회사명)로 주문금액 합을 보이되, 주문금액 합이 많은 순서대로 보이시오.
SELECT cus.고객번호, cus.담당자명, cus.고객회사명, ROUND(SUM(det.단가 * det.주문수량 * (1 - det.할인율))) 주문금액합
	FROM 고객 cus
		INNER JOIN 주문 ord
			ON cus.고객번호 = ord.고객번호
		INNER JOIN 주문세부 det
			ON ord.주문번호 = det.주문번호
		GROUP BY cus.고객번호
		ORDER BY 주문금액합 DESC;

SELECT * FROM 고객;
SELECT * FROM 주문;
SELECT * FROM 주문세부;

-- 4. 고객 테이블에서 담당자가 ‘이은광’인 경우의 고객번호, 고객회사명, 담당자명, 마일리지와 마일리지등급을 보이시오.
SELECT cus.고객번호, cus.고객회사명, cus.담당자명, cus.마일리지, grd.등급명
	FROM 고객 cus
		INNER JOIN 마일리지등급 grd
			ON cus.마일리지 BETWEEN grd.하한마일리지 AND grd.상한마일리지
		WHERE 담당자명 = '이은광';

SELECT * FROM 고객;
SELECT * FROM 마일리지등급;
