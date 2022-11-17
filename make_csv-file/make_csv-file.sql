-- 데이터를 선택해서 넣는 경우 프로시저를 호출할 때 필요한 파라미터를 같이 넘김
CREATE DEFINER=`db아이디`@`db주소` PROCEDURE `db명`.`프로시저명`(파라미터)
BEGIN

-- fullOutputPath : csv파일이 생길 경로. 경로(폴더)는 컨트롤러에서 미리 생성해야함.
SET @fullOutputPath := CONCAT('"C:\/temp\/폴더명\/파일명.csv"');
        -- outfileCarDate : csv 파일에 넣을 데이터를 조회하는 쿼리
		set @outfileCarDate := concat("
                select 쿼리문 ~
		        INTO OUTFILE ", @fullOutputPath,
				" FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '\"' ");

		prepare s1 from @outfileCarDate;
		execute s1;
		deallocate prepare s1;
        
END