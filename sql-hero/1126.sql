-- 1126. 查询活跃业务
-- https://leetcode-cn.com/problems/active-businesses/

-- 我的解法(大致同官方题解)
select business_id
from Events e,
     (select event_type, avg(occurences) as event_avg
      from Events
      group by event_type) a
where e.event_type = a.event_type
  and e.occurences > a.event_avg
group by business_id
having count(e.event_type) >= 2
