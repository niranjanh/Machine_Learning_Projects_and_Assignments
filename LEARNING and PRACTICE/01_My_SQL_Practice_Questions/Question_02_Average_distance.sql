-- Average distance
-- Description
-- Consider a table employee storing the details of the employee. 

-- ssn : social security number of the employee
-- address : storing the address of the employee

-- Looking at the address field in the employee table, you would notice that all the employees reside in "Fondren, Houston, TX". Consider the integer in the address field as house number. Consider the distance between the two houses as the difference in the house numbers, so the distance between house number 2 and 38 is 36 units. Write a query to determine the average distance between the house of the employee with ssn '123456789' and the other employees' houses. Print the answer to two decimal places. Make sure that the answer is formatted with a comma like x,xxx.xx . 

use upgrad;

select FORMAT(sum(abs(oth - emp)) / count(oth), 2) as average
from (
      select cast(address as SIGNED) as oth
      from employee
      where ssn != '123456789'
     ) e1
cross join (
      select cast(address as SIGNED) as emp
      from employee
      where ssn = '123456789'
     ) e2
     




