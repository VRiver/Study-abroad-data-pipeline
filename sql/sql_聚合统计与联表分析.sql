select
    country,
    count(*) as school_count
from
    schools
group by country;

select
    avg(tuition_usd) as avg_tuition
from
    programs;

select degree,
       count(program) as  program_count
from programs
group by degree;

select s.country ,
       avg(p.tuition_usd) as avg_tuition
from schools as s
left join programs as p
on s.school_id = p.school_id
group by country;