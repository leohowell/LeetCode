-- https://leetcode-cn.com/problems/orders-with-maximum-quantity-above-average/
-- 1867. 最大数量高于平均水平的订单

select order_id
from OrdersDetails
group by order_id
having max(quantity) > all (
    select avg(quantity)
    from OrdersDetails
    group by order_id
)
