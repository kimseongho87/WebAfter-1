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

-- 12. 사원들의 6개월 커미션의 합을 검색하세요.
SELECT first_name, 
            nvl(commission_pct*7, 0) AS 커미션의합
FROM employees;

-- 13. 사원이름을 Name으로, 사원의 급여를 Salary로 열의 이름을 부여하여 검색하세요.
SELECT first_name AS "Name", 
            salary AS "Salary"
FROM employees;

-- 14. 사원의 사원번호, 사원이름, 입사일, 부서번호를 한글로 바꾸어 검색하세요.
SELECT employee_id AS 사원번호, 
            first_name AS 사원이름, 
            hire_date AS 입사일, 
            department_id AS 부서번호
FROM employees;

-- 15. 부서번호, 부서이름, 지역번호를 한글로 바꾸어 검색하세요.
SELECT department_id AS 부서번호,
            department_name AS 부서이름,
            location_id AS 지역번호
FROM departments;

-- 16. 사원의 사원직무번호와 사원이름을 합쳐서 검색하세요.
SELECT job_id || first_Name
FROM employees;

-- 17. 입사일 '사원이름을 80-12-27에 입사한 SMITH입니다.' 식으로 검색하세요.
-- *** 안배웠음
SELECT CONCAT('입사일 \'사원이름을 ', DATE_FORMAT(hire_date, '%y-%m-%d'), '에 입사한 ', first_name, '입니다.') AS "사원정보"
FROM employees;

-- 18. ‘Steven의 급여는 24000입니다.’와 같은 형식으로 검색하세요. 
SELECT CONCAT(first_name, '의 급여는 ', salary, '입니다.') AS "사원의 급여"
FROM employees
WHERE first_name = 'Steven';

-- Select ~ Where Example 문제
-- ** 사원(employees), 부서(departments), 직군(jobs) 테이블 사용하여 아래의 내용을 검색(select ~ where) 하세요.
SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM jobs;

-- 19. 10번 부서에 근무 사원이름을 검색하세요.
SELECT department_id,
        first_name
FROM employees
WHERE department_id=10;

-- 20. 연봉이 2000 이상인 사원들의 사원번호, 사원이름을 검색하세요.
SELECT employee_id,
            first_name, 
            salary
FROM employees
WHERE salary >=2000;

-- 21. 사원직무가 'AD_VP' 인 사원들의 사원번호, 사원이름을 검색하세요.
SELECT employee_id, 
            first_name, 
            job_id
FROM employees
WHERE job_id='AD_VP';

-- 22. 2004년 02월 17일에 입사한 사원의 이름을 검색하세요.
SELECT first_name, 
            hire_date
FROM employees
WHERE hire_date='2004-02-17';

-- 23. 부서번호 30 이외의 부서이름과 지역번호을 검색하세요.
SELECT department_id, 
          department_name,
          location_id
FROM departments
WHERE department_id != 30;

-- 24. 직군 'IT_PROG'의 상위급여와 하위급여를 검색하세요.
SELECT job_id, 
            min_salary, 
            max_salary
FROM jobs
WHERE job_id='IT_PROG';

-- 25. 'Steven' 사원의 모든 정보를 검색하세요.
SELECT * FROM employees
WHERE first_name='Steven';

-- 26. 90 부서에 근무하는 'AD_VP'의 사원이름을 검색하세요.
SELECT department_id, 
            job_id, 
            first_name
FROM employees
WHERE department_id=90 AND job_id='AD_VP';

-- 27. 연봉이 2000 이상이며, 30번 부서에 근무하는 사원들의 사원번호와 사원이름을 검색하세요.
SELECT employee_id, 
            first_name, 
            department_id, 
            salary
FROM employees
WHERE salary >=2000 AND department_id=30;

-- 28. 사원의 직군이 'ST_MAN' 이며, 2004년 이후에 입사한 사원들의 사원번호, 사원이름을 검색하세요.
SELECT employee_id, 
            first_name, job_id,
            hire_date
FROM employees
WHERE job_id='ST_MAN' AND hire_date > '2004-12-31';

-- 29. 1700 이외 지역에서 있는 부서이름을 검색하세요.
SELECT department_name, 
            location_id
FROM departments
WHERE location_id <> 1700;

-- 30. 'IT_PROG'이며 연봉이 5000 이상인 사원이름을 검색하세요.
SELECT first_name, 
            salary,
            job_id
FROM employees
WHERE job_id='IT_PROG' AND salary >=5000;

-- 31. 사원번호 13X인 사원의 사원번호, 사원이름, 부서번호를 검색하세요. 
SELECT employee_id, 
            first_name, 
            department_id
FROM employees
WHERE employee_id LIKE '13%';

-- 32. 관리자사원번호가 20으로 시작하는 사원들의 사원이름을 검색하세요.
SELECT first_name, 
            manager_id
FROM employees
WHERE manager_id LIKE '20%';

-- 33. 사원이름 중간에 'a'가 들어있는 사원의 사원번호와 사원이름을 검색하세요.
SELECT employee_id, 
            first_name
FROM employees
WHERE first_name LIKE '_%a%';

-- 34. 연봉이 1000이상이며, 2500 이하인 사원의 사원번호, 사원이름, 연봉을 검색하세요. (BETWEEN ~ AND 연산자)
SELECT employee_id, 
            first_name, 
            salary
FROM employees
WHERE salary BETWEEN 1000 AND 2500;

-- 35. 2005년 10월에 입사한 사원의 사원번호, 사원이름, 부서번호를 검색하세요. (BETWEEN ~ AND 연산자)
SELECT employee_id, 
            first_name, 
            department_id,
            hire_date
FROM employees
where hire_date BETWEEN '2005-10-01' AND '2005-10-30';

-- 36. 사원이름(first_name)을 조회하여 첫 글자가 H~J를 포함한 사원이름을 검색하세요. (BETWEEN ~ AND 연산자, %연산자)
SELECT first_name 
FROM employees 
WHERE first_name BETWEEN 'H%' AND 'J%'; 

-- 37. 부서번호가 10 또는 30에 근무하는 사원들의 사원이름, 연봉을 검색하세요. (IN 연산자)
SELECT first_name, 
            salary,
            department_id
FROM employees
WHERE department_id in (10, 30);

-- 38. 사원번호가 166 또는 129인 사원이름을 검색하세요.  (IN 연산자)
SELECT employee_id, 
            first_name
FROM employees
WHERE employee_id in (166, 129);

-- 39.  관리자번호가  100 또는 103 사원의 사원번호와 사원이름을 검색하세요.(IN 연산자)
SELECT employee_id, 
            first_name,
            manager_id
FROM employees
WHERE manager_id in (100, 103);

-- 40.  사원의 직군이 'SA_MAN'또는 'SA_REP' 인 사원의 사원번호, 사원이름을 검색하세요.(IN 연산자)
SELECT employee_id, 
            first_name,
            job_id
FROM employees
WHERE job_id in ('SA_MAN', 'SA_REP');

-- 41. 관리자번호가 NULL 인 사원의 사원번호, 사원이름을 검색하세요.
SELECT employee_id, 
          manager_id
FROM employees
WHERE manager_id IS NULL;

-- 42. 관리자번호가 NULL 아닌 사원의 사원번호, 사원이름을 검색하세요.
SELECT employee_id, 
            first_name,
          manager_id
FROM employees
WHERE manager_id IS NOT NULL;

-- 43. 사원들의 사원번호와 사원이름을 사원번호 순으로 검색하세요.
SELECT employee_id, 
          first_name
FROM employees
ORDER BY employee_id ASC;

-- 44. 사원들의 사원번호와 사원이름을 부서번호별 이름순으로 검색하세요.
SELECT employee_id, 
          first_name,
          department_id
FROM employees
ORDER BY department_id ASC, employee_id ASC;

-- 45. 사원들의 정보를 부서별 급여가 많은 순으로 검색하세요.
SELECT employee_id, 
          first_name,
          department_id,
          salary
FROM employees
ORDER BY department_id ASC, salary DESC;

-- 46. 사원들의 정보를 사원직무별 급여 순으로 검색하세요.
SELECT employee_id, 
          first_name,
          job_id,
          salary
FROM employees
ORDER BY job_id ASC, salary DESC;

-- 47. 사원들의 정보를 부서번호별, 사원직무별, 연봉 순으로 검색하세요.
SELECT employee_id, 
          first_name,
          department_id,
          job_id,
          salary
FROM employees
ORDER BY department_id, job_id, salary DESC;
