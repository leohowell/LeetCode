-- 1107. 每日新用户统计
-- https://leetcode-cn.com/problems/new-users-daily-count/

select activity_date as login_date, count(user_id) as user_count
from (
         select user_id,
                min(activity_date) as activity_date,
         from Traffic
         where activity = "login"
         group by user_id
     ) a
where activity_date >= "2019-04-01"
  and activity_date <= "2019-09-30"
group by activity_date
order by activity_date
