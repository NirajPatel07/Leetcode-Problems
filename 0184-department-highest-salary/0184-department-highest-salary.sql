# Write your MySQL query statement below

SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary FROM Department, Employee WHERE Department.id = Employee.departmentId
AND (Employee.departmentId, Employee.salary) IN (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId)