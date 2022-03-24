-- 580. 统计各专业学生人数
-- https://leetcode-cn.com/problems/count-student-number-in-departments/

select Department.dept_name      as dept_name,
       ifnull(student_number, 0) as student_number
from (Department
    left join
    (select dept_id, count(distinct (student_id)) as student_number
     from Student
     group by dept_id) s
    on Department.dept_id = s.dept_id
     )
order by student_number desc, dept_name