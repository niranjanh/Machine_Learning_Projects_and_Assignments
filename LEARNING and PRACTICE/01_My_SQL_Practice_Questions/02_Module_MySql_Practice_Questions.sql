-- 1.
-- Given the following table salary from a university database, write a query to find the student_id of with salary greater than 59,999. 

-- | Student_id | Salary |

-- Order your results in the order of student_id.

select Student_id
from salary
where Salary > 59999
order by Student_id;




-- 2.
-- Consider the following table marks part of a school database containing the following columns
-- Student_id : Storing the id of the student
-- Course         : Storing the name of the course 
-- Marks           : Storing the marks obtained by the student in the particular course

-- Write a query to determine the average marks obtained by students. Order the results in the descending order of average marks. In case the --average marks are same for two students, student with a lower student_id should appear first.

-- The output should be of the form
-- |Student_id|avg(marks)|

select student_id, avg(Marks)
from marks
group by student_id
order by avg(Marks) desc, student_id asc;





-- 3.

-- Consider a table named 'home' storing Arsenal football club's performance in the league at home in 2003-04 season, while the table 'away' stores Arsenal's performance away in the same season.﻿

-- home
-- opponent goals_scored goals_conceded

-- away
-- opponent goals_scored goals_conceded

-- ﻿Note that a team is awarded three points for a win, one for a draw and zero for a loss. Write a query to determine the number of teams against whom Arsenal won all the available six points.

-- Arsenal plays each team once at home and once away.



use upgrad;

# Write your code below
drop function if exists didArsenalWon;

DELIMITER $$

create function didArsenalWon (goals_scored int, goals_conceded int)
    returns int
deterministic
begin
    declare points_scored int;
    set points_scored = 0;
    if goals_scored > goals_conceded then
        set points_scored = 1;
    else
        set points_scored = 0;
    end if;
    
    return points_scored;
end
$$

select count(*) 
from home h
where didArsenalWon(h.goals_scored, h.goals_conceded) = 1 
    and 
    didArsenalWon(h.goals_scored, h.goals_conceded) = 
    (
        select didArsenalWon(a.goals_scored, a.goals_conceded)
        from away a
        where a.opponent = h.opponent
    );



