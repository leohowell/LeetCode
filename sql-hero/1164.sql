-- 1164. 指定日期的产品价格
-- https://leetcode-cn.com/problems/product-price-at-a-given-date/

-- 我的解法(同官方题解)
select d.product_id, ifnull(price, 10) as price
from (select distinct product_id
      from Products) d

         left join

     (select e.product_id,
             new_price as price
      from Products e

               inner join

           (select product_id,
                   max(change_date) as change_date
            from Products
            where change_date <= "2019-08-16"
            group by product_id) c
           on e.product_id = c.product_id and e.change_date = c.change_date) s
     on d.product_id = s.product_id
