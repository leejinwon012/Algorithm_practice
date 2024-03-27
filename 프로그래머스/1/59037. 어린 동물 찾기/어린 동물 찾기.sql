SELECT animal_id, name
from animal_ins
where INTAKE_CONDITION != "Aged"        # 문자열 비교이니 is not 이 아닌 != 또는 <>
order by animal_id