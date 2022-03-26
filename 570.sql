-- 570. 至少有5名直接下属的经理
-- https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports/

select name
from (select managerId
      from Employee
      where managerId is not null
      group by managerId
      having count(id) >= 5) m
         inner join
     Employee
     on m.managerId = Employee.id
