-- Topper
-- Description
-- Consider a table storing the marks obtained by student in five course, physics, chemistry, mathematics, history and philosophy in comma separated form. ﻿
-- student_id  marks
--  1          20,30,40,50,60

-- Write a query to determine the id of the student who has the highest average in Physics, Chemistry and Mathematics. Assume that the marks are all stored as two digit numbers. 



use upgrad

alter table marks
add physics int
default 0;

update marks
set physics = SUBSTRING_INDEX(SUBSTRING_INDEX(marks,',',1),",",-1);

alter table marks
add chemistry int
default 0;

update marks
set chemistry = SUBSTRING_INDEX(SUBSTRING_INDEX(marks,',',2),",",-1);

alter table marks
add mathematics int
default 0;

update marks
set mathematics = SUBSTRING_INDEX(SUBSTRING_INDEX(marks,',',3),",",-1);

-- (physics + chemistry + mathematics)/3  as avg_marks 
select student_id
from marks
group by student_id
order by (physics + chemistry + mathematics)/3 desc
limit 1;
