-- 578. 查询回答率最高的问题
-- https://leetcode-cn.com/problems/get-highest-answer-rate-question/

select question_id as survey_log
from (
         select s.question_id,
                ifnull(cnt_answer, 0) / cast(cnt_show as float) as answer_rate
         from (
               (select question_id, count(*) as cnt_show
                from SurveyLog
                where `action` = "show"
                group by question_id) s

                  left join

              (select question_id, count(*) as cnt_answer
               from SurveyLog
               where `action` = "answer"
               group by question_id) a
              on s.question_id = a.question_id
                  )
     ) a
order by answer_rate desc, question_id limit 1
