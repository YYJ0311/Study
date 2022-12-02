-- user_id와 login_dt로 이루어진 테이블이 있음(전체 로그인 로그 테이블)
-- 해당 로그에서 특정 유저의 최근 로그인 일자를 확인하고 싶을 경우

-- 1. Self Join
SELECT 
    a.user_id
    , a.login_dt -- 최근 로그인 시간
    , MAX(b.login_dt) lag_dt -- 최근에서 바로 전 로그인 시간
FROM t a
LEFT OUTER JOIN t b
    ON a.user_id  = b.user_id
    AND a.login_dt > b.login_dt 
   -- 여기에서 a테이블에만 있는 로그인 시간(최근 로그인 시간)을 가져올 수 있게 됨
GROUP BY a.user_id, a.login_dt

-- 2. @변수 사용
SELECT 
    user_id
    , login_dt
    , lag_dt
FROM 
    (SELECT
        user_id
        , login_dt
        , CASE WHEN @id = user_id THEN @dt END lag_dt
        -- , IF(@id = user_id, @dt, null) lag_dt
        , @dt := login_dt
        , @id := user_id
    FROM t
    ORDER BY user_id, login_dt
    ) a

-- 3. 스칼라 서브쿼리
SELECT 
    user_id
    , login_dt
    , (SELECT login_dt
        FROM t b
        WHERE b.user_id  = a.user_id
        AND b.login_dt < a.login_dt
        ORDER BY login_dt DESC 
        LIMIT 1 -- 가장 최근 직전의 로그인 날짜가 선택됨
    ) lag_dt
FROM t a
ORDER BY user_id, login_dt