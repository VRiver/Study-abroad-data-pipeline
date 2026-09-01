select program,
       tuition_usd
from programs
where tuition_usd >(
    select avg(tuition_usd)
    from programs
    )

select program,
       tuition_usd
from programs
where tuition_usd = (
    select max(tuition_usd)
    from programs
    )

select program,
       tuition_usd,
rank() over(order by tuition_usd desc)
from programs

select *
from(
select s.country,
       p.program,
       p.tuition_usd,
       rank() over (
    partition by s.country
    order by p.tuition_usd desc)
        as country_rank
from schools as s
left join programs as p
on s.school_id = p.school_id)
as ranked_programs
where ranked_programs.country_rank = 1