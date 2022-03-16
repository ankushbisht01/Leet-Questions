# Write your MySQL query statement below
select * 
from cinema
where id % 2 != 0 and description != "boring"
Order by rating Desc