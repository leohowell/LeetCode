-- 1988. 找出每所学校的最低分数要求
-- https://leetcode-cn.com/problems/find-cutoff-score-for-each-school/submissions/

select Schools.school_id, ifnull(score, -1) as score
from Schools
         left join
     (select school_id, min(score) as score
      from Schools,
           Exam
      where Schools.capacity >= Exam.student_count
      group by Schools.school_id) r
     on Schools.school_id = r.school_id
