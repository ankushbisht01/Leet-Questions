# Write your MySQL query statement below
select firstName , lastName , city , state
from Person  
Left join Address 
on Person.personId = Address.personId