-- 1699. 两人之间的通话次数
-- https://leetcode-cn.com/problems/number-of-calls-between-two-persons/

select person1,
       person2,
       count(*)      as call_count,
       sum(duration) as total_duration
from (select case when from_id > to_id then to_id else from_id end as person1,
             case when from_id > to_id then from_id else to_id end as person2,
             duration
      from Calls) a
group by person1, person2
