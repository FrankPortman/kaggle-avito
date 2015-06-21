.mode csv
.headers on
.out ../data/1-trainSearchStream.csv
select * from trainSearchStream
where ObjectType = 3;
