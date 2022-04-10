# Write your MySQL query statement below
select name as Employee 
from Employee as em
where salary > (select salary 
               from employee as mg
               where em.managerId = mg.id)