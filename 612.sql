-- 612. 平面上的最近距离
-- https://leetcode-cn.com/problems/shortest-distance-in-a-plane/

select round(
               min(
                       sqrt(
                                   power((p1.x - p2.x), 2) + power((p1.y - p2.y)
                                   , 2)
                           )
                   )
           , 2)
           as shortest
from Point2D p1
         cross join
     Point2D p2
where p1.x <> p2.x
   or p1.y <> p2.y
