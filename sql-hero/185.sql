-- 185. 部门工资前三高的所有员工
-- https://leetcode-cn.com/problems/department-top-three-salaries/

-- 我的解答
select d.name as Department, r.name as Employee, salary
from (select departmentId,
             name,
             salary,
             dense_rank() over (partition by departmentId order by salary desc) as myrank
      from Employee) r

         left join
     Department d
     on r.departmentId = d.id

where myrank <= 3


-- 官方题解的解答
-- 学习到的知识点，在子查询中可以使用父查询中的字段

select d.name as Department, m.name as employee, salary
from (select e1.name, e1.salary, e1.departmentId
      from employee e1
      where (select count(distinct e2.salary) as cnt
             from employee e2
             where e2.salary > e1.salary
               and e1.departmentId = e2.departmentId
            ) < 3) m
         left join
     Department d
     on m.departmentId = d.id
