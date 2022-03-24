-- 184. 部门工资最高的员工
-- https://leetcode-cn.com/problems/department-highest-salary/

select Department.name as Department, e.name as Employee, e.salary as Salary
from (select name, salary, departmentId
      from Employee
      where (salary, departmentId) in
            (select max(salary) as salary, departmentId
             from Employee
             group by departmentId)) e

         left join Department
                   on e.departmentId = Department.id
