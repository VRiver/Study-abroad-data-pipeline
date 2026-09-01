select p.program,
        s.school
from programs as p
left join schools as s
on s.school_id = p.school_id
group by p.program,s.school;

select p.program,
        s.country
from programs as p
left join schools as s
on s.school_id = p.school_id
group by p.program,s.country;

select p.program,
    p.degree,
    r.ielts_min
from programs as p
left join requirements as r
on r.program_id = p.program_id
group by p.program,p.degree,r.ielts_min;

select s.school,
    count(p.program) as program_count
from schools as s
left join programs as p
on s.school_id = p.school_id
group by s.school;