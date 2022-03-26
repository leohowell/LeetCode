-- 1045. 买下所有产品的客户
-- https://leetcode-cn.com/problems/customers-who-bought-all-products/

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(*) as cnt from Product)
