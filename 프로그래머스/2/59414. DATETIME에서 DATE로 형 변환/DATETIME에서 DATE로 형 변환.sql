SELECT ANIMAL_ID,
       NAME,
       DATE_FORMAT(DATETIME, '%Y-%m-%d') as 날짜
from animal_ins