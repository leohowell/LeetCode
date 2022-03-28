-- 175. 组合两个表
-- https://leetcode-cn.com/problems/combine-two-tables/

select FirstName, LastName, City, State
from (select PersonId,
             FirstName,
             LastName
      from Person) p
         left join
     (select PersonId, City, State
      from Address) a
     on p.PersonId = a.PersonId
