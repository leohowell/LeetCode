-- 627. 变更性别
-- https://leetcode-cn.com/problems/swap-salary/

update Salary
Set sex = case sex when "m" then "f" else "m" end;
