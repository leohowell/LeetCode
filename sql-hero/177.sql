-- 177. 第N高的薪水
-- https://leetcode-cn.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET
N = N-1;
RETURN (
    # Write your MySQL query statement below.
      select (select distinct salary
        from Employee
        order by salary desc
           limit 1 offset N) as getNthHighestSalary
    );
END
