select name, year from Album where year >= '20180101' and year < '20190101';

select name, time from Track order by time desc limit 1;

select name from Track where time >= 210;

select name from Collection where year >= '20180101' and year < '20210101';

select name from Band where name not like '%% %%';

select name from Track where name like '%%my%%' or name like '%%мой%%';