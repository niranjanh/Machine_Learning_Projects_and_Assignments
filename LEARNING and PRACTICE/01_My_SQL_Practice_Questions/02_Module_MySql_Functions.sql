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
