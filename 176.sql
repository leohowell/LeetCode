-- 176. 第二高的薪水
-- https://leetcode-cn.com/problems/second-highest-salary/


-- 我的解答
select ifnull(
               (select salary
                from (select salary, rank() over (order by salary desc) salary_rank
                      from Employee) a
                where (salary_rank = 2) limit 1)
, null
           ) as SecondHighestSalary

-- 官方题解
select (select distinct salary
        from Employee
        order by salary desc
           limit 1 offset 1) as SecondHighestSalary
