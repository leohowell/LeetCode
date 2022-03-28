-- 1141. 查询近30天活跃用户数
-- https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-i/

select activity_date as day, count(distinct user_id) as active_users
from Activity
where activity_date <= "2019-07-27"
  and activity_date >= "2019-06-28"
group by activity_date
