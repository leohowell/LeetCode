-- 1532. 最近的三笔订单
-- https://leetcode-cn.com/problems/the-most-recent-three-orders/

select name as customer_name, o.customer_id, order_id, order_date
from (select customer_id,
             order_id,
             order_date
      from (
               select customer_id,
                      order_id,
                      order_date,
                      rank() over (partition by customer_id order by order_date desc) as myrank
               from Orders
           ) a
      where myrank <= 3) o

         left join
     Customers
     on Customers.customer_id = o.customer_id
order by Customers.name, customer_id, order_date desc