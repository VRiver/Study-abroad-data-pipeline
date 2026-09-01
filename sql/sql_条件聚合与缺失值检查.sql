select s.school,
    count(p.program) as program_count
from schools as s
left join programs as p
on s.school_id = p.school_id
group by s.school
HAVING count(p.program) > 0;

select p.program,
       p.tuition_usd,
    CASE
    when p.tuition_usd is null then 'Unknown'
    when p.tuition_usd < 40000 then 'Budget'
    else 'Expensive'
end as tuition_level
from programs as p

select program,
       tuition_usd
from programs
where tuition_usd is null

select p.program,
    r.ielts_min
from programs as p
left join requirements as r
on r.program_id = p.program_id
where r.ielts_min is null
group by p.program,r.ielts_min;