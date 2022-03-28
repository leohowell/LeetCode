-- 197. 上升的温度
-- https://leetcode-cn.com/problems/rising-temperature/

select b.id as id
from (
      (select recordDate, temperature
       from Weather) a
         inner join
     (select id, recordDate, temperature
      from Weather) b
     on a.temperature < b.temperature and datediff(a.recordDate, b.recordDate) = -1
         )
