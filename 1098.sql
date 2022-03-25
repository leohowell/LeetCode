-- 1098. 小众书籍
-- https://leetcode-cn.com/problems/unpopular-books/

select b.book_id, name
from (
      (select book_id, name
       from Books
       where available_from < "2019-05-23") b

         left join

     (select book_id, sum(quantity) as sum_quantity
      from Orders
      where dispatch_date <= "2019-06-23"
        and dispatch_date >= "2018-06-23"
      group by book_id) o
     on b.book_id = o.book_id
         )
where sum_quantity is null
   or sum_quantity < 10
