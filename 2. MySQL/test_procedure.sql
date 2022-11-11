-- 테스트 프로시저 작성
    CREATE DEFINER=`db계정명`@`%` PROCEDURE `db명`.`프로시저명`()
    begin
        INSERT INTO  infocar_internal_data.test(
            var,
            val 
        )
        values (
            now(),
            (select CAST(rand()*100 as signed integer))
            -- int형 1~100 랜덤값
        );
    END

-- 테스트 스케줄러 작성
    CREATE EVENT infocar_internal_data.스케줄러명
    ON SCHEDULE EVERY 10 second
    STARTS '2022-11-09 10:18:00'
    COMMENT '테스트중'
    DO call infocar_internal_data.test_proc();

-- 존재하는 스케줄러 확인
    show variables like 'event%';
    SELECT * FROM information_schema.events;