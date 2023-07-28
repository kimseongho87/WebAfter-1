-- Select Example 문제

-- 1. 사원(employees) 테이블의 구조를 검색하세요.
DESCRIBE employees;

-- 2. 부서(departments) 테이블의 구조를 검색하세요.
DESCRIBE departments;

-- 3. 지역(locations) 테이블의 구조를 검색하세요.
DESCRIBE locations;

-- ** 사원(employees) 테이블과 부서(departments) 테이블 사용하여 아래의 내용을 검색(select) 하세요.
SELECT * FROM employees;
SELECT * FROM departments;

-- 4. 사원들의 사원번호, 사원이름, 사원직무를 검색하세요.
SELECT employee_id, 
		first_name, job_id
FROM employees;

-- 5. 부서의 부서번호와 부서이름을 검색하세요.
SELECT department_id, department_name 
FROM departments;

-- 6. 부서의 부서이름과 지역번호를 검색하세요.
SELECT department_name, 
		location_id
FROM departments;

-- 7. 사원들의 급여와 커미션을 검색하세요
SELECT salary, 
		commission_pct
FROM employees;

-- 8. 사원들의 입사일 중복을 제거하고 검색하세요.
SELECT DISTINCT hire_date
FROM employees;

-- 9. 사원들의 관리자번호 중복을 제거하고 검색하세요.
SELECT DISTINCT manager_id
FROM employees;

-- 10. 사원들의 부서번호 중복을 제거하고 검색하세요.
SELECT DISTINCT department_id
FROM departments;

-- 11. 사원들의 6개월 급여의 합을 검색하세요.
SELECT first_name, salary*6 as 급여의합
FROM employees;

-- 12. 사원이름을 Name으로, 사원의 급여를 Salary로 열의 이름을 부여하여 검색하세요.
SELECT first_name AS "Name", 
		salary AS "Salary"
FROM employees;

-- 13. 사원의 사원번호, 사원이름, 입사일, 부서번호를 한글로 바꾸어 검색하세요.
SELECT employee_id AS 사원번호, 
		first_name AS 사원이름, 
		hire_date AS 입사일, 
		department_id AS 부서번호
FROM employees;

-- 14. 부서번호, 부서이름, 지역번호를 한글로 바꾸어 검색하세요.
SELECT department_id AS 부서번호,
            department_name AS 부서이름,
            location_id AS 지역번호
FROM departments;

-- 15. 사원의 사원직무번호와 사원이름을 합쳐서 검색하세요.
SELECT CONCAT(job_id, '||', first_Name)
FROM employees;

-- 16. 입사일 '사원이름을 80-12-27에 입사한 SMITH입니다.' 식으로 검색하세요.
SELECT CONCAT(hire_date, '에 입사한 ', first_name, '입니다.') 
FROM employees;

-- 17. ‘Steven의 급여는 24000입니다.’와 같은 형식으로 검색하세요. 
SELECT CONCAT(first_name, '의 급여는 ', salary, '입니다.') 
FROM employees;
