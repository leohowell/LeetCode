-- 196. 删除重复的电子邮箱
-- https://leetcode-cn.com/problems/delete-duplicate-emails/


-- 选择所有重复的邮箱，保留id最小的
select p1.id as id, p2.email as email
from Person p1, Person p2
where p1.email = p2.email and p1.id > p2.id


-- 删除所有重复的邮箱，保留id最小的
delete p1
from Person p1, Person p2
where p1.id > p2.id and p1.email = p2.email
