-- 1077. 项目员工 III
-- https://leetcode-cn.com/problems/project-employees-iii/

select project_id,
       employee_id
from (select project_id,
             p.employee_id,
             rank() over (partition by project_id order by experience_years desc) myrank
      from Project p
               left join
           Employee e
           on p.employee_id = e.employee_id) a
where myrank = 1
