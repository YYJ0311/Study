-- while - update(일정 범위동안 반복하는 update) 프로시저
    -- 아래 프로시저에선 두 쿼리(하루의 데이터 + 전날 데이터)의 결과값을 합산하기 위해 alias를 주고 union all 을 이용해서 더해줬다.

    CREATE DEFINER=`DB아이디명`@`%` PROCEDURE `DB명`.`프로시저명`()
    begin
        declare 초기선언변수 timestamp(타입) default "2020-03-02 00:00:00"(초기값설정); 
            -- 20.03.02 값 부터 update

        while (초기선언변수 < "2022-11-07 00:00:00") DO 
            -- 2022-11-07까지 반복함
            update DB명.테이블명
            set DB명.테이블명.수정하는컬럼명 = (
                select sum(dtSum) from(
                    (SELECT sum(time_to_sec(참고DB명.참고테이블명.RECDRV_DRVTIME)) as dtSum
                    FROM 참고DB명.참고테이블명
                    where
                        RECDRV_UPLOAD_TIME >= 초기선언변수
                        and
                        RECDRV_UPLOAD_TIME < DATE_ADD(초기선언변수, interval 1 day)
                        and
                        RECDRV_DRVDIS > 0
                        and
                        RECDRV_DRVDIS <= 1000
                        and
                        RECDRV_IS_HIDDEN = 0)
                    union all
                    (select cumulativeDrivingTime as dtSum
                    from DB명.테이블명
                    where stats_datetime = DATE_SUB(초기선언변수, interval 1 day))
                ) as a
            )
            where stats_datetime = 초기선언변수;
            set 초기선언변수 = DATE_ADD(초기선언변수, interval 1 day); 
            -- 초기선언변수가 날짜여서 하루 더해줌으로써 while문이 돌아가게 만듦
        end while;
    END