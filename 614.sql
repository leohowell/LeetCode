-- 614. 二级关注者
-- https://leetcode-cn.com/problems/second-degree-follower/

select followee as follower, count(distinct follower) as num
from follow
where followee in
      (select distinct follower
       from follow)
group by followee
