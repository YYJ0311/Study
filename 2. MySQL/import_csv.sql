-- csv 파일을 import 하기 전에 인코딩을 utf8로 변환해야 한다.
    -- csv파일을 메모장으로 열고, 다른이름 저장 - 인코딩을 utf-8로 변경하여 저장
    -- * 인코딩 형식을 바꾼 뒤 파일 내용을 수정한 경우 다시 인코딩 변환과정을 거쳐야 함

-- 1. 테이블 구조와 csv 파일 구조가 동일할 경우
load data infile 'C:/test/ko2_utf8.csv'
into table tb_csvinserttest
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

-- 2. 테이블과 csv파일의 컬럼명이 다른 경우
    -- 테이블의 컬럼명 = id/var/val/more
    -- csv파일의 컬럼명 = num/category/value1/value2
load data infile 'C:/test/ko2_utf8mod.csv'
into table tb_csvinserttest
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows
(@num, @category, @value1, @value2)
set id = @num,
	var = @category,
	val = @value1,
	more = @value2

-- 3. db server 내에 있는 파일이 아니라, 클라이언트에 있는 csv 파일을 가져올 경우
    -- load data infile 대신 load data local infile로 사용
    -- 이 경우 클라이언트에 있는 파일에 대한 읽기 권한이 있어야 함
    -- 실행속도 느림
load data local infile 'C:/test/ko2_utf8.csv'
into table tb_csvinserttest
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

-- 주의점
    -- fields terminated로 지정하는 문자로 컬럼을 구분한다. 
    -- 여기선 "," 로 구분했는데 만약 컬럼의 내용에 ,가 있으면 오류가 발생하기 때문에 다른 문자로 구분해야 한다.