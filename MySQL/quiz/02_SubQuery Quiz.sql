-- 1. Harrison 사원보다 많은 연봉을 받는 사원 정보를 검색하세요.
SELECT employee_id, 
            first_name, 
            salary
FROM employees
WHERE salary > (SELECT salary 
                     FROM employees 
                     WHERE first_name='Harrison');  -- 해리슨 10000
                     
-- 2. Ki 사원보다 적은 연봉을 받는 사원 정보를 검색하세요. 
SELECT employee_id, 
            first_name, 
            salary
FROM employees
WHERE salary < (SELECT salary 
                     FROM employees 
                     WHERE first_name='Ki');  -- 2400
                     
-- 3. Sales 부서의 모든 사원의 사원이름, 연봉, 부서번호 검색하세요.
SELECT first_name, 
            salary, 
            department_id 
FROM employees 
WHERE department_id=(SELECT department_id 
                            FROM departments
                            WHERE department_name='Sales');                           

-- 4. 사원이름이 B로 시작하는 사원들과 같은 부서에서 근무하고 있는 사원 정보를 검색
SELECT first_name,
        department_id
FROM employees
WHERE department_id IN (SELECT department_id 
						FROM employees 
                        WHERE first_name LIKE 'B%');                      -- 60, 50       

-- 5. 관리자 King(last_name) 사원이  관리하는 사원 정보를 검색
SELECT first_name, 
        manager_id
FROM employees
WHERE manager_id IN (SELECT employee_id 
					 FROM employees 
					 WHERE last_name='King');   --  100, 156(관리하는 사원 없음)

-- 6. 전체 사원의 평균 연봉보다 연봉이 많은 사원 정보를 검색하세요.
SELECT first_name, 
        salary
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);    -- 6461

-- 7. 연봉이 모든 부서들의 평균 연봉보다 많은 사원 정보를 검색하세요.
SELECT first_name, 
        salary
FROM employees 
WHERE salary > ALL (SELECT ROUND(AVG(salary))
					FROM employees 
					GROUP BY department_id);    -- 19333
                            
-- 8. 60번 부서번호의 최대 급여보다 최대 급여가 큰 부서의 번호와 최대 급여를 검색하세요.
SELECT MAX(salary) maxsalary,
          department_id
FROM employees 
WHERE salary > (SELECT MAX(salary)
				FROM employees 
				WHERE department_id=60)    -- 9000
GROUP BY department_id;                             

-- 9. Toronto 지역에 위치하는 부서에 근무하는 사원 정보를 검색하세요 (Join / .SubQuery ~ WHERE)
SELECT employee_id,
        first_name, 
        department_id
FROM employees 
WHERE department_id=(SELECT department_id 
					 FROM departments
					 WHERE location_id=(SELECT location_id
										FROM locations)); 
                                                                                                                                           	                                                      
-- 10. 부서별로 가장 최근에 입사한 사원을 검색하세요.   
-- 1) SubQuery ~ Where
SELECT department_id, 
          first_name,
          hire_date
FROM employees 
WHERE (department_id, hire_date) IN (SELECT department_id, MAX(hire_date) 
									 FROM employees
									 GROUP BY department_id)
ORDER BY 1;












