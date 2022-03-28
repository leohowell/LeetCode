-- 577. 员工奖金
-- https://leetcode-cn.com/problems/employee-bonus/

select name, bonus
from (
      (select empId, name
       from Employee) e
         left join
     (select empId, bonus
      from bonus) b
     on e.empId = b.empId
         )
where b.bonus < 1000
   or b.bonus is null
