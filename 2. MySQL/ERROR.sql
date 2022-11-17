-- local에서 쓰는 프로시저에서 definer를 root로 정의했더니 root를 인식하지 못 함
    -- 기존
    CREATE DEFINER=`root`@`%` PROCEDURE db명.프로시저명 (파라미터)

    -- 변경
    `root`@`%` -> `root`@`localhost`
    CREATE DEFINER=`root`@`localhost` PROCEDURE db명.프로시저명 (파라미터)


-- 