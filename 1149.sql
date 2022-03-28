-- 1149. 文章浏览 II
-- https://leetcode-cn.com/problems/article-views-ii/

-- 我的解答(同官方题解)
select distinct viewer_id as id
from Views
group by view_date, viewer_id
having count(distinct article_id) >= 2
order by viewer_id
