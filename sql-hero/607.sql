-- 607. 销售员
-- https://leetcode-cn.com/problems/sales-person/

select name
from SalesPerson
where sales_id not in (
    select distinct sales_id
    from (
          (select sales_id, com_id
           from Orders) o

             inner join

         (select com_id
          from Company
          where name = "RED"
         ) c
         on o.com_id = c.com_id
             )
)