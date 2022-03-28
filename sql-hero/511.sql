-- 511. 游戏玩法分析 I
-- https://leetcode-cn.com/problems/game-play-analysis-i/

select player_id, min(event_date) as first_login
from Activity
group by player_id
order by player_id
