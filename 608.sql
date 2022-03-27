-- 608. 树节点
-- https://leetcode-cn.com/problems/tree-node/

select id,
       case
           when p_id is null then "Root"
           when id in (select p_id from tree) then "Inner"
           else "Leaf" end as type
from tree
