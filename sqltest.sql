# select

select * from table; 

select column from tables;

select column from tables where a= 'b' and not c = "b" order by column asc or desc;

select column from tables where order by column asc or desc limit 1

중복없이
select distinct column from tables;

몇 종류인지
select count(distinct column) from tables;

NULL 처리
select * from tables where column is null


from -> where -> group by -> having -> select -> order by
# insert

순서에 맞게
insert into tables  (column1,column2,column3) values (value1,value2,value3);

문자열이면 따옴표 사용하기
insert into tables values (value1,value2,value3)


# update df

update tables set column  = value where a is null;

update tables set column = valuel, column2 = value;

# delete

delete from table where column = "a"

# MIN MAX

select min(column) from tables;

select max(column) from tables;

# count avg sum

select count(column) from table where ~

select avg(column) from table where ~

select sum(column) from table where ~

# like

select * from tables where column like 'a%' // a로 시작하는

select * from tables where column like "%e" // e로 끝나느

# operator

select * from columns where column1 in ('germany', 'france', 'uk')

select * from products where price between 10 and 20;

# group by
select co1, count(co1) as cnt from table group by co1

select co1, count(co1) as cnt from table group by co1 having cnt>=2

# join

select a.id, a.name from a left outer join b on a.id = b.id where b.id is null

select a.id, a.name, a.kname from a innter join b on a.id = b.id
# case

case column
when 조건1 then 값1
when 조건2 then 값2
else 값3
end