-- 626. 换座位
-- https://leetcode-cn.com/problems/exchange-seats/

-- 如果起始为偶数，则偶数+1，奇数-1
-- 如果起始为奇数，则奇数+1, 偶数-1

select
case
-- 起始奇数, 当前奇数，总数奇数，当前为最大 => id不变
when start_flag = 1 and id % 2 = 1 and total_flag = 1 and id = max_id then id
-- 起始奇数, 当前奇数，总数奇数，当前非最大 => id+1
when start_flag = 1 and id % 2 = 1 and total_flag = 1 and id <> max_id then id + 1
-- 起始奇数, 当前奇数，总数偶数 => id+1
when start_flag = 1 and id % 2 = 1 and total_flag = 0 then id + 1
-- 起始奇数, 当前偶数，总数奇数 => id - 1
when start_flag = 1 and id % 2 = 0 then id - 1

-- 起始偶数，当前奇数，总数奇数，当前为最大 => id不变
when start_flag = 0 and id % 2 = 1 and total_flag = 1 and id = max_id then id
-- 起始偶数，当前奇数，总数奇数，当前非最大 => id -1
when start_flag = 0 and id % 2 = 1 and total_flag = 1 and id <> max_id then id - 1
-- 起始偶数，当前奇数，总数偶数 => id+1
when start_flag = 0 and id % 2 = 1 and total_flag = 0 then id - 1
-- 起始偶数，当前偶数 => id+1
when start_flag = 0 and id % 2 = 0 then id + 1
else id
end
as id,
student

from
seat,
(select
       count(*) % 2 as total_flag,
       min(id) % 2 as start_flag,
       max(id) as max_id
from seat) a
order by id
