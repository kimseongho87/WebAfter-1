-- 함수 Example 문제

-- 1. 사원들의 사원이름(first_name)을 소문자로 검색하세요.
SELECT LOWER(first_name) 사원이름
FROM employees;

-- 2. 사원들의 사원이름(first_name), 사원직군을 소문자로 검색하세요.
SELECT LOWER(first_name) 사원이름,
	   LOWER(job_id) 사원직군
FROM employees;

-- 3. 사원들의 사원이름(first_name)을 대문자로 검색하세요.
SELECT UPPER(first_name) 사원이름
FROM employees;

-- 4. 사원들의 사원이름(first_name), 사원직군을 대문자로 검색하세요.
SELECT UPPER(first_name) 사원이름,
	   UPPER(job_id) 사원직군
FROM employees;

-- 5. 사원들의 사원이름(first_name)을 첫문자만 대문자로 검색하세요.
SELECT INITCAP(first_name) 사원이름
FROM employees;

-- 6. 사원들의 사원이름(first_name), 사원직군을 첫문자만 대문자로 검색하세요.
SELECT INITCAP(first_name) 사원이름,
	   INITCAP(job_id) 사원직군
FROM employees;

-- 7. 사원들의 사원이름(first_name)과 사원직군를 연결하여 검색하세요. (CONCAT 함수)
SELECT CONCAT(first_name, job_id) 사원연결
FROM employees;

-- 8. 사원들의 사원이름(first_name)의 첫 두 글자를 검색하세요.
SELECT first_name, 
	   SUBSTR(first_name, 1, 2) 문자열추출
FROM employees;

-- 9. 사원들의 사원이름(first_name), 사원직군 그리고 사원직군의 네 번째 부터 두 글자를 검색하세요.
SELECT first_name, 
		job_id, 
		SUBSTR(job_id, 4, 2) 문자열추출
FROM employees;

-- 10. 사원들의 사원이름(first_name), 전화번호, 전화번호에서 지역번호만 검색하세요.
SELECT first_name, 
        phone_number,
	   	SUBSTR(phone_number, 1, 3) 지역번호
FROM employees;

-- 11. 사원들의 사원이름(last_name)의 끝자리가 N으로 끝나는 직원 검색하세요.
SELECT last_name 
FROM employees 
WHERE substr(last_name, -1, 1)='n';

-- 12. 사원들의  사원이름(first_name)의 길이를 검색하세요.
SELECT first_name,
	   LENGTH(first_name) 문자길이
FROM employees;

-- 13. 사원들의 사원이름(first_name)과 사원직군의 길이를 검색하세요.
SELECT first_name,
		job_id,
		LENGTH(job_id) 문자길이
FROM employees;

-- 14. 사원들의 사원이름(first_name)에 'a'가 몇 번째 위치에 있는지를 검색하세요.
SELECT first_name,
	 INSTR(first_name, 'a') "a의 위치"
FROM employees;

-- 15. 사원직군에 'A'가 몇 번째 위치에 있는지 검색하세요.
SELECT job_id,
	 INSTR(job_id, 'A') "A의 위치"
FROM employees;

-- 16. 사원이름(first_name)을 15자리로 하고, 뒤에 '&'를 채워 검색하세요.
SELECT rpad(first_name, 15, '&') 패턴
FROM employees;

-- 17. 사원직군을 20자리고 하고, 앞에 '%'를 채워 검색하세요.
SELECT lpad(job_id, 20, '%') 패턴
FROM employees;

-- 18. 실수형 3456.789를 두 번째 자리에서 반올림하여 출력하세요.
SELECT round(3456.789, 2) 반올림
FROM dual;

-- 19. 실수형 3456.789를 소수 이전 까지만 출력
SELECT TRUNC(3456.789) 버림
FROM dual;

-- 20. 사원번호와 연봉을 1000으로 나눈 나머지를 검색하세요.
SELECT employee_id, 
		salary, 
		MOD(salary, 1000) 나머지
FROM employees;

-- 21. 사원번호, 사원이름, 입사일, 입사 후 100일의 날짜를 검색하세요.
SELECT employee_id, 
		first_name, 
		hire_date, 
		hire_date+100 "100 후"
FROM employees;

-- 22. 사원번호, 사원이름, 입사일, 근무 일자를 계산하여 검색하세요.
SELECT employee_id, 
		first_name, 
		hire_date, 
		TRUNC(sysdate-hire_date) 근무일자
FROM employees;

--  23. 사원들의 입사일에서 3달째 되는 날짜를 검색하세요.
SELECT hire_date, 
		ADD_MONTHS(hire_date, 3) 삼개월후날짜
FROM employees;

-- 24. 사원들의 입사일 다음 토요일의 날짜를 검색하세요.
SELECT hire_date, 
		NEXT_DAY(hire_date, '토') 토요일날짜
FROM employees;

-- 25. 사원들의 입사월의 마지막 날짜를 검색하세요.
SELECT hire_date, 
		LAST_DAY(hire_date) 마지막날짜
FROM employees;

-- 26. 사원들의 입사일을 년을 기준으로 반올림하여 검색하세요.
SELECT hire_date, 
		ROUND(hire_date, 'YYYY') 반올림
FROM employees;

-- 27. 사원들의 입사일을 년을 기준으로 절삭하여 검색하세요.
SELECT hire_date, 
		TRUNC(hire_date, 'YYYY') 버림
FROM employees;

-- 28. 관리자번호가 없는 사원의 경우 'CEO'로 바꾸어 검색하세요.
SELECT employee_id,
        first_name,
        NVL(to_char(manager_id), 'CEO')  관리자번호
FROM employees;

-- 28. 커미션을 포함한 연봉을 계산하여 출력하세요. (연봉계산은 연봉+커미션*12)
SELECT employee_id, 
		first_name,
		salary,
		commission_pct,
		ROUND((salary+nvl(commission_pct, 0))*12) 연봉계산
FROM employees;

-- 29. 1993년 01월01일 이전에 입사한 직원들의 사번, 성, 이름, 입사일, 급여, 커미션을 검색하세요.
--      처리조건) 입사일은 2005-01-01로 표기, 커미션이 없는 경우 0으로 출력, 급여가 많은 순으로 정렬
SELECT employee_id, 
	   	last_name,
        first_name,
	  	TO_CHAR(HIRE_DATE, 'YYYY-MM-DD') 입사년월일,
		TO_CHAR(HIRE_DATE, 'YYYY "년"') 년도,
	   	TO_CHAR(salary, '$99,999') 월급,
	   	NVL(commission_pct, 0) 수수료
FROM employees WHERE hire_date < TO_DATE('2005-01-01', 'YYYY-MM-DD') 
ORDER BY salary DESC;

-- 30. 사원들의 사원이름(first_name) 중 MAX와 MIN 값을 검색하세요.
SELECT MAX(first_name) 최대값,
            MIN(first_name) 최소값
FROM employees;

-- 31. 사원들의 입사일 중 MAX와 MIN 값을 검색하세요.
SELECT MAX(hire_date) 최대값,
            MIN(hire_date) 최소값
FROM employees;

-- 32. 관리자번호 열의 개수를 검색하세요.
SELECT COUNT(manager_id) count
FROM employees;

-- 33. 사원이름의 개수를 검색하세요.
SELECT COUNT(first_name) count
FROM employees;

-- 34. 사원테이블의 튜플(레코드) 수를 검색하세요.
SELECT COUNT(*) count
FROM employees;

-- 35. 커미션의 개수를 검색 하세요.
SELECT COUNT(commission_pct) count
FROM employees;

-- 36. 부서별 사원들의 인원수를 검색하세요.
SELECT department_id, 
            COUNT(department_id) 부서인원수
FROM employees
GROUP BY department_id
ORDER by department_id;

-- 37. 관리자번호별 사원들의 인원수를 검색하세요.
SELECT manager_id,
        COUNT(manager_id)  관리인원수
FROM employees
GROUP BY manager_id
ORDER by manager_id;

-- 38. 부서별 사원들의 평균 연봉를 검색하세요.
SELECT department_id, 
		ROUND(AVG(salary)) 부서평균연봉
FROM employees
GROUP BY department_id
ORDER by department_id;

-- 39. 부서별 사원들의 연봉 합을 검색하세요.
SELECT department_id, 
	   SUM(salary) 부서연봉합
FROM employees
GROUP BY department_id
ORDER by department_id;

-- 40. 직군별 사원들의 평균 연봉을 검색하세요.
SELECT job_id, 
	   ROUND(AVG(salary)) 직군평균연봉
FROM employees
GROUP BY job_id
ORDER by job_id;

-- 41. 부서별, 직군별 사원들의 입사일의 MAX와 MIN 값을 검색하세요.
SELECT department_id,
		job_id, 
	   max(hire_date) max,
	   min(hire_date) min
FROM employees
GROUP BY department_id, job_id 
ORDER by department_id, job_id;

-- 42. 부서별 연봉 평균 구하고, 연봉 평균이 5000이상 7000이하인 부서만 검색하세요.
SELECT department_id,
	   ROUND(AVG(salary)) 연봉
FROM employees 
GROUP BY department_id 
HAVING AVG(salary) >=5000  AND  7000 >=AVG(salary)
ORDER by department_id;







