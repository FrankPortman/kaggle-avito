.mode csv
.headers on
.out ../data/1-testSearchStream.csv
select * from testSearchStream
where ObjectType = 3;
