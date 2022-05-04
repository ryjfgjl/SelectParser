with tmp_table1 as( 
select 
a.id as id, 
b.name as name, -- from 
c.city,
' from 
aa',
--select * from comment_table1 a join comment_table2 b on a.id = b.id where 1=1
66/*select * from comment_table3 a join comment_table4 b on a.id = b.id
where 1=1
--test
*/
,
(select a.name from country a where a.id = c.countryid) as country,
'---',
(select nvl(c.country,' ') from dual as a) as country1,
a.amount,
decode(d.email,'xxx',' select ',nvl(e.name,' from ')),
'a
aa' name1,
' where ' as  test
from order as a 
left join user1. customer b on (a.custid = b.id)  and b.sex in ('0','1','2')
join address c on c.id = b.addressid
left join (select custid, max(email) email from contact a where email is not null group by custid) d on d.custid =b.id,
company e
where e.id = b.companyid
union all
select 
*
from (select * from order as b) as a ,(select * from customer as b) b --,comment_table3
, address c 
,(select custid, max(email) email from contact a where email is not null group by custid) d 
where a.id = (select 1 from dual)
and b.custid = subsrr(b.id,1,8)
and b.addressid = c.id
and d.custid = b.id
),
tmp_table2 AS
(
select * from (select * from user1 . order a join user2.customer b on a.custid = b.id)
)
select a.custid, sum(amount) from tmp_table1 a, tmp_table2 b 
where a.id = b.id
and a.id exists(select * from order c where c.amout >= 10000 )
and b.date >= add_months((select sysdate from dual),-12)
group by a.custid