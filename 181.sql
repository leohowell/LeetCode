-- 181. 超过经理收入的员工
-- https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/

-- 员工比起对应的经理收入高
select e.name as Employee
from (
      (select name, salary, managerId
       from Employee
       where managerId is not null) e

         left join

     (select id, salary
      from Employee) m
     on e.managerId = m.id
)
where e.salary > m.salary
