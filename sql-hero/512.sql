-- 512. 游戏玩法分析 II
-- https://leetcode-cn.com/problems/game-play-analysis-ii/

select player_id, device_id
from Activity
where (player_id, event_date) in
      (select player_id, min(event_date) as event_date
       from Activity
       group by player_id)
