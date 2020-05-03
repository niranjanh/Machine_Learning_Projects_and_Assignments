-- Consider a table consisting the marks of students in a mathematics test along with their unique student_id. Write a query to determine which -- students got the marks that is divisible by 10 and which students did not. 
-- Make sure that the output is ordered by student_id.﻿

use upgrad;

# Write your code below

alter table marks
add div_by_ten varchar(10)
default "no";

update marks
set div_by_ten = "yes"
where MOD(marks, 10) = 0;

select *
from marks
order by student_id;
