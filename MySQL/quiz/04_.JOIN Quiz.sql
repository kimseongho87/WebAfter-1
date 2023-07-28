-- 1. 사원번호, 사원이름, 부서이름 검색하세요. 
SELECT employee_id,
          first_name,
          department_name
FROM employees e 
INNER JOIN departments d
ON e.department_id=d.department_id;

-- 2. 사원번호, 사원이름, 직군번호, 직군명을 검색하세요.
-- ** 테이블 근무지역 존재하지 않음

-- 3. 부서코드가 80~100인 사원번호, 부서코드, 부서명를 부서코드순으로 검색하세요.
SELECT employee_id,
          e.department_id,
          department_name
FROM employees e  
INNER JOIN departments d
ON e.department_id=d.department_id
WHERE  e.department_id >70 AND e.department_id < 100
ORDER BY 2;

-- 4. 근무지역이 Oxford인 사원을 검색하세요. 
SELECT * FROM locations;
SELECT * FROM employees;
SELECT * FROM departments;

SELECT employee_id, 
          first_name,
          city
FROM employees e
INNER JOIN departments d
ON  e.department_id=d.department_id
INNER JOIN locations loc
ON d.location_id=loc.location_id
AND city='Oxford';

-- 5. Neena 사원이 근무 중인 부서이름과 근무지역을 검색하세요.
SELECT first_name,
          department_name,
          city
FROM employees e
INNER JOIN departments d
ON e.department_id=d.department_id
INNER JOIN locations loc
ON d.location_id=loc.location_id
AND first_name='Neena';

-- 6. 사원번호, 이름, 직군명, 부서명, 근무지역 검색하세요.
-- ** 테이블 근무지역 존재하지 않음

-- 7. 사원직군 Accountant이면서 Seattle 지역에 근무하는 사원명을 검색하세요.
-- ** 테이블 근무지역 존재하지 않음

-- 8. 부서(부서명)별 평균연봉 구하세요 (equi join).
SELECT department_name,
        ROUND(AVG(salary)) 평균연봉
FROM employees e
INNER JOIN departments d
ON e.department_id=d.department_id
GROUP BY department_name;

-- 9.직군(직군명)별 인원수 검색 후, 인원수가 5명 이상인 직군(직군명)을 직군(직군명)순으로 검색하세요.
-- 해당 테이블 존재하지 않음

-- 10. Adam과 같은 직무인 사원의 이름과 직군을 검색하세요 (Sele Join).
SELECT e.first_name, 
        j.job_id
FROM employees e
INNER JOIN employees j
ON e.job_id=j.job_id
AND j.first_name='Adam'
AND e.first_name != j.first_name;

-- 11. David와 같은 연봉을 받는 사원의 이름과 연봉을 검색하여 이름순으로 출력하세요 (Sele Join).
-- 4800, 6800, 9500
SELECT e.first_name, 
        j.salary
FROM employees e
INNER JOIN employees j
ON e.salary=j.salary
AND j.first_name='David'
AND e.first_name <> j.first_name
ORDER BY 2;

SELECT * FROM employees;










