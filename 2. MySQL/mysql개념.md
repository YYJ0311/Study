# 헷갈리는 문법
    # primary key 추가
        alter table infocar_internal_data.data_daily_stats ADD PRIMARY key (컬럼명);
        alter table DB명.테이블명 ADD PRIMARY key (컬럼명1, 컬럼명2);

# 중복데이터 관리 방법
    1. INSERT IGNORE
        중복된 데이터 값이 있다면 삽입을 무시한다
        한 테이블에 id와 name, address 컬럼이 있고 name 컬럼에 unique인덱스가 걸려있는 경우,
            INSERT INTO person VALUES ('Andrew', 'Seoul');
            -- 아래 2개의 쿼리는 중복된 데이터로 인해 동작하지 않고 에러가 난다
            INSERT INTO person VALUES ('Andrew', 'Incheon');
            INSERT INTO person VALUES ('Andrew', 'Busan');

            INSERT IGNORE INTO person VALUES ('Andrew', 'Seoul');
            -- 아래 2개의 쿼리는 0 row affected로 반환한다. (에러는 아님)
            INSERT IGNORE INTO person VALUES ('Andrew', 'Incheon');
            INSERT IGNORE INTO person VALUES ('Andrew', 'Busan');

            person 테이블을 조회하면
                (1  Andrew  Seoul)
                처음에 insert한 값과 id만 나온다.

        테이블의 다른 컬럼에 AUTO_INCREMENT가 있어도 IGNORE로 인해 추가등록되지 않은 항목들에는 AUTO_INCREMENT가 적용되지 않는다.
    
    2. INSERT INTO … ON DUPLICATE KEY UPDATE
        중복데이터가 발생했을때, 업데이트할 항목을 지정할 수 있다.
        테이블에 똑같이 name과 address 컬럼이 있고, name에 unique가 걸려있다. 그리고 inserted_cnt 컬럼을 추가해서 중복 데이터의 갯수를 체크할 수 있다.
            INSERT INTO person VALUES ('Andrew', 'Seoul', 1) 
                ON DUPLICATE KEY UPDATE inserted_cnt = inserted_cnt + 1;

            INSERT INTO person VALUES ('Andrew', 'Incheon', 1) 
                ON DUPLICATE KEY UPDATE inserted_cnt = inserted_cnt + 1;

            INSERT INTO person VALUES ('Andrew', 'Busan', 1) 
                ON DUPLICATE KEY UPDATE inserted_cnt = inserted_cnt + 1;
            
            ON DUPLICATE KEY UPDATE키워드는 각각 처음 삽입된 쿼리를 제외하고, 2 row affected를 리턴한다.
            person 테이블을 조회하면 
                (1  Andrew  Busan  3)
                주소는 마지막에 입력한 값이 들어가 있고
                inserted_cnt 는 같은 name을 가지는 데이터의 총 개수를 보여준다.

    3. REPLACE INTO
        기존의 중복데이터가 있으면 삭제하고, 새로 INSERT한다. 
        새로 삽입하기 때문에 AUTO_INCREMENT값이 증가한다.(단점)

            REPLACE INTO person VALUES ('Andrew', 'Seoul');

            REPLACE INTO person VALUES ('Andrew', 'Incheon');
            REPLACE INTO person VALUES ('Andrew', 'Busan');

            첫번째 삽입되는 항목을 제외하고, 나머지 2개의 쿼리는 2 row affected를 반환한다.
            person 테이블을 조회하면
                (3  Andrew  Busan)
                증가된 AUTO_INCREMENT 컬럼값과(ex. id) 마지막에 입력한 주소값이 나온다.

# 프로시저(procedure)
    여러 SQL 문을 하나의 SQL 문처럼 정리하여 실행할 수 있게 만든 것 
    1. 프로시저 생성
        DELIMITER $$
        CREATE PROCEDURE GetCustomers()
        BEGIN
            SELECT customerName, city, state, postalCode, country 
            FROM customers 
            ORDER BY customerName; 
        END $$ 
        DELIMITER ;

        1-1 DELIMITER 사용 이유
            - 구문 문자로, 문법의 끝을 나타내는 역할을 함
            - C나 JAVA의 ';'(세미콜론)이라고 생각하면 됨
            - 저장 프로시저 내부에 사용하는 SQL문은 일반 SQL문이기때문에 세미콜론(;)으로 문장을 끝맺어야 한다. 즉 문장을 구분하기 위해 사용한다.

    2. 프로시저 호출
        CALL GetCustomers();
        - 저장 프로시저를 활용하면 쿼리문을 일일히 작성하지 않아도 함수처럼 사용하여 손쉽게 쿼리문과 동일한 결과를 조회 할 수 있다.

    3. 사용
        기본 형태
            CREATE DEFINER=`DB아이디`@`%` PROCEDURE `프로시저명`
            BEGIN
                SELECT * 
                FROM 테이블명
            END

        인자값, 변수 할당, 조건문
            CREATE DEFINER=`DB아이디`@`%` PROCEDURE `프로시저명`(
                IN 변수명 자료형,
                OUT 변수명 자료형
            )
            BEGIN
                SET @v_code = '123'; // 변수. 서브쿼리 사용 가능
                IF @v_code!='' THEN
                    SELECT *
                    FROM 테이블명
                    WHERE 컬럼 = 변수명 AND
                        컬럼 = @v_code
                END IF;
            END

        IF 절
            IF 조건문(조건문 THEN)
                실행문구
            ELSE IF(조건문 THEN)
                실행문구
            END IF;

            [NULL 체크 & 비교]
            IS NOT NULL / IS NULL 을 쓸 수 있다.

            !=, <> 사용가능

# Mysql CHARACTER SET / COLLATE
    Mysql에서 DB를 생성할 때 Character Set과 Collation을 지정할 때가 있다.
    collation을 통해 문자 데이터 타입에 대해 어떻게 다룰 것인가를 명시한다.

    Character Set
        문자와 encodign의 집합
        ex) utf8, euckr
    
    Collation
        Character Set 안에서 character들을 비교하기 위한 rule들의 집합
        ex) binary collation (encoding된 byte 스트림 값으로 문자를 비교하는 것), 
            case-insensitive collation (다음의 규칙으로 문자를 비교하는 것 : 1. 소문자와 대문자를 같은 문자로 다룸 2. 이후 encoding으로 비교)

    character Set과 collation 예
        character set utf8은 utf8_bin, utf8_czech_ci, utf8_danish_ci 등의 collation을 가짐

        character set euckr은 euckr_bin, euckr_korean_ci 와 같은 2가지의 collation을 가짐

    설정 단계
        character set은 각 단계별로 설정이 가능하다
        1. server
        2. database(schema)
        3. table

        각 단계에서 charater set/collation 설정을 하면 그 하위 단계에서는 설정하면 안 된다. (server에서 설정을 하면 database에선 charater set/collation을 사용한다는 구문이 없어야만 한다.)

    문제점
        1. 데이터가 저장된 table의 collation에 따라 데이터 비교가 제대로 되지 않을 수 있음
            => collation이 xxx_general_ci로 되어있다면 xxx_bin으로 수정하면 됨
        2. 서버에서 설정한 값이 테이블에 적용되지 않을 수 있음
            => 서버의 설정값과 db의 설정값이 다른 경우 db의 설정값을 변경 후 테이블 생성
            테이블 생성시 추가 설정을 한 경우 서버의 설정값을 그대로 받기 위해 테이블에서 설정을 하지 않도록 함

# LEAD / LAG
    LEAD
        문법
            LEAD(<expression>[,offset[, default_value]]) OVER (
                PARTITION BY (expr)
                ORDER BY (expr)
            )

        PARTITION BY 절
            LEAD() 함수가 적용되는 행을 나눈다.
            partition by로 나눠진 컬럼 안에서 정렬된다.
        
        ORDER BY 절
            파티션의 행 순서를 결정한다.
        
        예문
            SELECT 
                customerName,
                orderDate,
                LEAD(orderDate,1) OVER (
                    PARTITION BY customerNumber
                    ORDER BY orderDate ) nextOrderDate
            FROM 
                orders
            INNER JOIN customers USING (customerNumber);

        https://www.mysqltutorial.org/mysql-window-functions/mysql-lead-function/

    LAG
        문법
            LAG(<expression>[,offset[, default_value]]) OVER (
                PARTITION BY expr,...
                ORDER BY expr [ASC|DESC],...
            )
        사용
            select 
                totaldownloadNumber,
                LAG(totaldownloadNumber) over (order by stats_datetime_start) as previousTotalNumber
            from mureung.data_monthly_stats
            => 이렇게 쓰면 각 행의 totaldownloadNumber와 그 윗 행의 값이 previousTotalNumber 컬럼으로 조회됨
        
        https://www.mysqltutorial.org/mysql-window-functions/mysql-lag-function/

# LIMIT 사용의 단점과 방안
    limit의 사용은 모든 쿼리가 실행되어 select됨과 동시에 limit으로 select되는 갯수를 제한할 수 있어서 쿼리 전체 실행 시간을 줄여줄 수 있다. (마지막 레코드까지 가져오지 않아도 되기 때문)

    하지만 전체 레코드를 조회해야만 하는 ORDER BY나 GROUP BY와 limit이 같이 사용될 경우에는 limit을 사용해도 모든 레코드를 거쳐야 하기 때문에 성능 향상에 도움이 되지 않으며 응답속도가 느려질 수밖에 없다.
        => 인덱스를 사용한 정렬 방식과 limit을 같이 사용한다면 제한된 건수만큼 읽으면서 바로 클라이언트로 결과를 전송해줄 수 있기 때문에 빠른 응답속도를 기대할 수 있다.
    
    MySQL에서 페이징 처리를 위하여 LIMIT 키워드를 제공하여 쉽게 페이징할 수 있는데, 이 때 offset의 사용으로 문제가 발생할 수 있다.
        LIMIT 5, 20(= LIMIT 20 OFFSET 5) : 5번째 행부터 20개로 제한함
    위와 같이 OFFSET을 사용하여 페이징 할 경우 5번째 행부터 조회하는 것이 아니라 처음부터 25번째 만큼을 읽은 다음 앞의 5번째 까지의 레코드를 버리는 방식으로 작동한다. 따라서 OFFSET 값이 큰 수일 경우 읽어오는 레코드의 갯수도 많아지므로 이 때의 LIMIT은 최적화 대상이 된다.
        => 인덱스를 설정하고 where절에 조건을 줌으로써 해결됨
        1 페이지를 가져오는 쿼리
            SELECT * FROM salaries ORDER BY id LIMIT 0, 10
        2 페이지를 가져오는 쿼리
            -- 1 페이지에서 가져온 10번째 레코드의 id = 15
            SELECT * FROM salaries 
            WHERE id > 15
            ORDER BY id LIMIT 0, 10
        3 페이지를 가져오는 쿼리
            -- 2 페이지에서 가져온 20번째 레코드의 id = 26
            SELECT * FROM salaries
            WHERE id > 26
            ORDER BY id LIMIT 0, 10;
        WHERE을 거치면서 필요한 10개만큼 스캔한다.
        하지만 이렇게 적용하려면 1부터 500(혹은 그 이상) 페이지까지의 인덱스 컬럼의 값(where로 제한을 거는 부분?)을 알고 있어야 적용할 수 있기 때문에 어려움이 있다.
            => 이를 해결하기 위해 커버링 인덱스를 사용한다
            커버링 인덱스 : 전체 레코드에 접근할 필요 없이 인덱스의 컬럼만으로 select 결과를 만들 수 있는 경우
                SELECT id, emp_id, emp_name, salary
                FROM salaries
                where from_date >= '2000-01-01'
                LIMIT 5000000, 10
            위와 같은 쿼리는 (id, emp_id, emp_name, salary, from_date)로 구성된 인덱스가 생성되어 있어 굳이 레코드를 읽지 않아도 처리가 가능하다.
            이렇게 사용하면 모든 값이 메모리에 있으므로 500만 인덱스 레코드를 스캔하는데 걸리는 속도의 향상을 기대할 수 있다.

    대기업 예시
        바로 큰 수의 페이지(500만 번째 페이지)로 넘어갈 때 최적화(실행이 원할)가 가능한가에 대한 대기업의 대답

        구글
            구글은 최대 1000개의 검색 결과만 제공함
            4000페이지로 바로 이동할 시 예외처리되어 검색 불가

        인스타
            페이지 이동이 불가능함. 무조건 무한 스크롤로 보는 수밖에 없음.
        
        네이버
            10페이지까지만 제공

# 두개의 select 값을 합산하는 방법
    SELECT SUM(cnt) 
    FROM (
		SELECT COUNT(*) as CNT FROM tb_user
		UNION ALL
		SELECT COUNT(*) as CNT FROM tb_admin
    ) ad s

    두개의 select에 alias을 똑같이 붙여주고 UNION ALL 한 다음 상위의 select에서 alias의 sum을 구한다.

    from에도 alias를 필수적으로 붙여야 함

# 스케줄러
    1. 스케줄러 사용 설정 확인하기
        show variables like 'event%';
            => 조회 결과 value가 OFF인 경우 아래 명령어를 실행한다
    2. 스케줄러 사용 설정 변경
        SET GLOBAL event_scheduler = ON;
    3. 생성되어 있는 스케줄러 확인
        SELECT * FROM information_schema.events;

    4. 스케줄러 생성
        CREATE EVENT 스케줄러명
        ON SCHEDULE EVERY 1 WEEK
        STARTS '시작일 2022-11-09 10:11:00 의 형식'
        COMMENT '코멘트 내용'
        DO 실행문
        
        스케줄러 반복 주기
            SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER(분기), YEAR
            
            만약 every 10 second 그리고 starts로 00초에 시작하면 ~:00, ~:10, ~:20 이렇게 딱 정확한 시간에 스케줄러가 실행된다.

    5. 스케줄러 삭제
        DROP event 스케줄러명

# union(full outer join)
    mysql에선 full outer join을 지원하지 않아서 left join과 right join한 값을 union해서 구한다.

    select residents.name as resident_name, animals.name as animal_name
    from residents left join animals
    on residents.id = animals.owner_id
    union
    select residents.name as resident_name, animals.name as animal_name
    from residents right join animals
    on residents.pet_id = animals.id;

    union / union all 차이
        union은 중복제거
        union all 은 중복된 것도 그대로 표현(중복 데이터 2개 표시됨)

# 날짜 데이터 포맷 바꾸기
    데이터 형식 : 2022-11-09 00:00:00 
    
    위 데이터를 2022-11-09 로 나타내기 위해서 다음처럼 쓸 수 있음

    left(stats_datetime_start, 10)
    DATE_FORMAT(stats_datetime_start, "%Y-%m-%d")

    근데 left로 잘라서 쓰는 건 눈으로 확인하기 어려우니 DATE_FORMAT을 사용하자

# index
    참고 : https://jeong-pro.tistory.com/242
    구조
        인덱스 컬럼을 관리하기 위해 트리(자료구조)를 이용
            최상위에 루트(Root) 노드, 가장 끝단에 실제 레코드의 주소가 저장된 리프(Leaf) 노드가 있고, 그 사이에 브랜치(Branch) 노드가 있다.
            루트와 브랜치 노드는 실제 레코드의 주소는 모르지만, 레코드 저장된 리프 노드에 대한 매핑정보를 갖고 있다. 이를 통해서 트리를 타고 가면서 레코드를 찾는다.
            루트 노드에서 브랜치 노드를 통해 리프노드로 들어가면 프라이머리 키가 정렬되지 않은 뒤죽박죽인 상태로 존재함. 그 이유는 데이터를 순서대로 생성하여 관리해도 데이터가 삭제되면 빈 자리가 생기고 나중에 다시 데이터를 생성할 때 그 자리를 활용하기 때문.

        MySQL에서 가장 많이 사용하는 실제 구조 = InnoDB
            InnoDB의 인덱스는 데이터 파일 저장 관리 방식이 트리 구조와 다르게, 프라이머리 키 인덱스로 정렬하여 관리한다. 

    인덱스 종류
        프라이머리 키 인덱스 : 프라이머리 키를 기준으로 만들어지는 인덱스
            => 프라이머리 키 인덱스는 반드시 존재한다! : 레코드 저장 자체가 프라이머리 키로 이루어지기 때문.
        세컨더리 키 인덱스 : 프라이머리 키를 제외한 모든 인덱스

    인덱스 사용의 종류
        1. 인덱스 레인지 스캔
            SELECT * FROM employees WHERE first_name BETWEEN 'Jeong' AND 'Pro';
                first_name 컬럼에서 설정한 범위만큼의 "일부"만 읽어서 검색하는 방법
                매우 이상적인
        2. 인덱스 풀 스캔
            인덱스를 쓰긴 쓰는데 인덱스를 처음부터 끝까지 다 읽는 방식으로 인덱스를 이용하는 것
            즉, 인덱스를 이용했지만 효율적이지 않은 경우이다.
        3. 루스(Loose) 인덱스 스캔
            인덱스 레인지 스캔처럼 일부만 읽는데 한 번에 쭉 읽는 게 아니라 중간에 필요치 않는 인덱스 키 값은 무시하고 듬성듬성 읽는 방법
        4. 인덱스 스킵 스캔
            => 나중에 정리.. 무슨 말인지 모름

    트레이드오프
        조회(SELECT) 성능에는 크게 도움이 되지만, 삽입(INSERT)/수정(UPDATE)/삭제(DELETE) 성능은 오히려 더 떨어진다
        레코드를 추가/수정/삭제할 때는 생성된 인덱스에도 데이터 동기화가 필요해서 오버헤드가 생기기 때문
            (오버헤드 : 어떤 처리를 하기 위해 들어가는 간접적인 처리 시간과 메모리)

    인덱스 설정의 기준
        카디널리티가 가장 높은 것

    카디널리티(Cardinality) : 특정 데이터 집합의 유니크한 값의 개수
        ex) "성별" 컬럼에 남자와 여자 값을 가짐. 이 경우 카디널리티는 2 이다.
    
        중복도가 낮으면, "카디널리티가 높다"고 표현
        중복도가 높으면, "카디널리티가 낮다"고 표현

        카디널리티 판단의 기준은 상대적이다.
            주민등록번호 같은 중복되지 않는 값은 카디널리티가 높다라고 표현한다.
            이름은 주민등록번호에 비해 중복되는 값이 많으므로 주빈등록번호에 비해 '카디널리티가 낮다' 라고 할 수 있다.

    성능 최적화 방법
        1. 가급적 로직을 DB상에서 처리하지 않고 WEB Application 상에서 구현한다.
            web에서 부하 조절이 더 원활하기 때문
        2. 칼럼의 데이터 길이를 최대한 작게, 보수적으로 설정한다.
            Bigint보다는 int를 사용. Autoincrement로 설정되어 있어도 int를 대부분 다 활용 못 한다.
            int 범위 : –2,147,483,648 ~ 2,147,483,647
            unsigned int 범위 : 0 ~ 4,294,967,295

            이름을 저장하는 컬럼이 과도하게 varchar(255)로 설정되어 있지 않은지 확인이 필요
        3. 파티션 테이블
            테이블 하나에 데이터를 전부 저장하지 않고 테이블을 나누어 저장하는 방식
            관리하기 힘들고, 다중 테이블 조회도 감안해야 하고, 어떻게 나눌 것인지 고민해야 하는 과정이 있다
            하지만 테이블을 분리함으로써 데이터 훼손 가능성을 감소시켜주고, 테이블 별 독립적인 복구도 가능하고, I/O 성능이 향상된다.
    
    인덱스 적용의 차이와 적용 방법
        인덱스를 적용한 칼럼과 적용되지 않은 칼럼의 차이는 Full Scan을 하느냐/안 하느냐 이다.
        1억개의 row를 하나하나 찾아가는 것보다 목차를 보고 한 번에 찾아가는 것이 훨씬 빠르다.

        where 절에서 검색 대상 칼럼이 인덱스여야 한다.
            검색할 대상으로 인덱스를 써서 원하는 데이터에 빠르게 접근할 수 있다.
        
        AND절 검색시 하나의 컬럼에만 인덱스 조회가 된다.
            인덱스가 지정된 여러개의 컬럼을 검색할때는 다수의 인덱싱 조회가 불가능하기 때문에 내부적인 로직에 의해 알아서 최적화된 인덱스만 검색한다.
            따라서 FORCE INDEX(칼럼) 을 지정함으로써 해당 칼럼도 인덱스 조회가 한번 더 진행되게 한다.

            // id 기준으로만 인덱싱 조회 
                SELECT * FROM test WHERE id = '15' and age = '24'; 
            // id와 age 모두 인덱싱을 조회하기 때문에 2번 조회한다. 
                SELECT * FROM test FORCE INDEX(age) WHERE id = '15' and age = '24';

        OR절 검색은 무조건 Full SCAN 된다.
            // 인덱싱을 걸어도 걍 무조건 Full Scan 
                SELECT * FROM test WHERE id = '1' OR age = '20'; 
            
            따라서 union을 사용하거나, web application 단에서 처리하는게 좋다.
            // UNION을 이용한 인덱싱 조회 
                SELECT * FROM test WHERE id = '1'; UNION SELECT * FROM test WHERE age = '20';
            // Web Application단에서 SELECT 두번 사용 
                $sql_id = "SELECT * FROM test WHERE id = '1'"; 
                mysqli_query($sql_id); 
                $sql_age = "SELECT * FROM test WHERE age = '20'"; 
                mysqli_query($sql_age);

        LIMIT가 되는 기준을 정해준다.
            LIMIT를 잘못 사용하게 되면 Full SCAN하게 될 수 있다.
            LIMIT를 사용할때는 LIMIT가 되는 기준을 무조건 정해주는것이 원칙
            // Full SCAN 
                SELECT * FROM test LIMIT 10, 5; 
            // 기준을 정해서 검색해서 조금 더 빨라짐 
                SELECT * FROM test ORDER BY id LIMIT 10; 
            // 기준을 정했으나 실제로는 10x100 = 1000번을 조회해야함. 
                SELECT * FROM test ORDER BY id LIMIT 10, 100; 
            // 기준 + WHERE절 사용으로 조회횟수 최소화 (*권장)
                SELECT * FROM test WHERE id > '100' ORDER BY id LIMIT 10;

        LIKE % 보다는 FULLTEXT를 활용한다.
            LIKE절은 칼럼안에 데이터를 확인해야하기 때문에 무조건 Full SCAN이 이뤄진다
            따라서 자연어 검색처리를 위한 FULLTEXT를 사용해야한다
            //Full SCAN 
                SELECT * FROM test WHERE name LIKE '%홍길동%'; 
            //FULLTEXT를 활용한 검색 
                SELECT * FROM test WHERE MATCH(name) AGAINST('홍길동');

            다중 LIKE 조회에서 포함되는 내용들을 검색할 때
                SELECT * FROM test WHERE MATCH(name) AGAINST("+'홍길동'+'강감찬'+'박명수'" IN BOOLEAN MODE)

            다중 LIKE 조회에서 누구는 포함되고 누구는 포함되지 않는 내용들을 검색할 때
                SELECT * FROM test WHERE MATCH(name) AGAINST("+'홍길동'-'넌빼고'-'난빼고'" IN BOOLEAN MODE)

# distinct
    범주 설정

    select count(distinct(usr_key)) from ~
        : 중복되는 usr_key에 대해 1개로 인식(하나의 범주로 인식)시키고 중복되지 않는 usr_key의 갯수를 조회함

# 비밀번호 변경
    컴퓨터에서 처음 mysql 설치할 때 입력한 비밀번호
    디비버에서 db연결할 때 mysql 비밀번호를 입력해야 하는데 까먹어서 초기화시킴
    https://simple-ing.tistory.com/57

# Event Scheduler
    리눅스의 crontab과 같이 주기적으로 특정 시간에 프로시저를 수행하는 것
    event에 필요한 쿼리를 등록하고, 특정 시간에 이 것을 수행한다.
    (매번 프로시저를 call하지 않고 이벤트 스케줄러에 등록하여 지정한 시간에 자동으로 이벤트가 실행됨)

    ex) DB에 많은 데이터가 쌓이게 되면, 주기적으로 데이터를 지워줘야하는데 이 때 사용한다.

    - event 명령어
        event scheduler 켜기
            SET GLOBAL event_scheduler = ON;

        이벤트 목록 보기
            SELECT * FROM information_schema.EVENTS
            또는
            SHOW EVENTS

        등록
            CREATE EVENT 이벤트 명
            ON SCHEDULE 스케쥴
            DO 쿼리문

            ex) 매일 오후 3시에 1번 select 쿼리 수행
            CREATE EVENT event
            ON SCHEDULE EVERY 1 DAY STARTS '2022-10-31 17:00:00'
            DO select * from table;

        등록되어 있는 이벤트 내용 보기
            SHOW CREATE EVENT `이벤트명`;
        
        수정
            ALTER EVENT 이벤트 명
            ON SCHEDULER 스케쥴
            DO 쿼리문

            ex) 매달에 오후 2시에 1번 select 쿼리 수행
            ALTER EVENT event
            ON SCHEDULE EVERY 1 MONTHS 
            STARTS '2022-10-31 17:00:00'
            DO select * from table;

        삭제
            DROP event `이벤트명`;
 
# DATE_ADD() / DATE_SUB()
    MySQL에서 시간 더하기, 빼기 함수
    DATE_ADD : 기준날짜 + 입력된 기간
    DATE_SUB : 기준날짜 - 입력된 기간

    date_add(CURDATE(),INTERVAL -1 day)
        : 오늘 년월일을 기준으로 하루를 뺀 날짜

# PUT 과 PATCH 차이
    PUT은 모든 항목을 수정함. 따라서 입력받지 않은 항목은 null로 바꿔버린다.
    PATCH는 입력받은 항목만 수정함. 따라서 입력받지 않은 항목은 그대로 남고 입력받은 항목만 수정된다.

# INTO OUTFILE 사용 & 에러
    SQL Error [1290] [HY000]: The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
        : --secure-file-priv 옵션은 데이터 export/import 기능을 제한하는 옵션이므로 추가 설정이 필요하다.
        
        0. 작업관리자 서비스에서 mysql 중지
        1. show variables like "secure_file_priv";
            를 통해서 데이터 export/import 가 가능한 경로 확인
        2. 모든 경로에서 파일을 읽고 쓸 수 있도록 설정
            my.ini는 보통 MySQL basedir 하위에 있으므로 show variables like '%dir'; 명령어를 통해 위치 확인 가능.
            또는 PROGRAMDATA/MySQL/MySQL Server X.X 경로에서 MySQL 설정 파일(my.ini)를 찾는다.
            ini 파일에서 secure-file-priv = "" 로 수정
        3. show variables like "secure_file_priv";로 경로 업데이트 된 것 확인
        4. 데이터 조작하기

# 테이블 이동 및 데이터 복사
    디비버에서 기능을 지원하지만 sql문으로 작성해봄

    테이블 구조만 복사
        CREATE TABLE IF NOT EXISTS 복사테이블 LIKE 원본테이블;

    테이블 생성 및 데이터 복사
        use 사용할db명;
        create table if not exists 테이블명 select * from db명.테이블명;

    데이터 복사
        INSERT INTO 복사테이블 SELECT * FROM 원본테이블;
        INSERT INTO 복사테이블 (컬럼1 [, 컬럼2 ...]) SELECT 컬럼1 [, 컬럼2 ...] FROM 원본테이블;

    특이사항
        1. 이렇게 복사된 테이블과 데이터는 원본에서 걸어두었던 제약조건(primary key, auto_increment 등)까지는 가져오지 못하므로 복사해온 테이블에 대해 새로 추가해줘야 한다.

        *** auto_increment를 추가했다면, 테이블의 auto_increment 초기값도 수정해줘야 한다!! 수정하지 않으면 기본 0으로 되어있어서 duplicate key 오류가 발생함

        2. 복사해서 새로 생긴 테이블의 크기(용량)이 원본 테이블보다 작게 보임
            => 복사해오면서 필요없는 공간이 빠져나가서 생긴 차이인 듯
            원본 테이블에서 delete/update 등으로 커졌던 테이블크기가 그대로 유지되기 때문으로 보인다.

# view
    db에 존재하는 가상 테이블
    실제 테이블처럼 행과 열을 가지고 있지만, 실제로 데이터를 저장하고 있지는 않음.
    
    장점
        특정 사용자에게 테이블 전체가 아닌 필요한 필드만 보여줄 수 있음
        복잡한 쿼리를 단순화해서 사용할 수 있음?
    단점
        한 번 정의된 뷰는 변경 불가
            => 새로운 뷰를 생성하고 명령어를 통해 대체 가능
        삽입/삭제/갱신 작업에 제한
        뷰는 자신만의 인덱스를 가질 수 없음

    -- 여러 테이블을 조회하는 VIEW 생성 명령어
    CREATE VIEW [view_name] AS alias
    SELECT a.[field_name_1], b.[field_name_2]
    FROM [table_name_1] AS a, [table_name_2] AS b
    WHERE [조건];

    이렇게 만들어진 view를 select를 이용하여 사용(조회)할 수 있음
    
    -- 생성된 뷰 조회(뷰 이름 : view_name)
    SELECT * FROM view_name;

# from절에는 concat을 쓸 수 없다
    controller에서 파라미터를 받아와서 from절에서 조건별로 리스트를 가져오려고 했다.

    정확하게는 from절에 concat 자체는 사용 가능하지만 concat으로 만든 것은 문자열이라서 테이블로 인식하지 못한다. 따라서 concat으로 만든 테이블명은 실제 존재하는 테이블명이 아니기 때문에 해당 테이블의 데이터를 가져올 수 없다.

    mybatis from에 파라미터 받는 방법???
        파라미터로 테이블명을 통째로 넘겨주어도 인식하지 못하는걸 보면 from에 #{} 사용이 불가한 것 같다.

        해결
            넘겨줄 파라미터 값을 hashmap에 저장해서 가져오고 from에 if test문 작성.
            파라미터를 조건으로 if test문을 여러개 작성해서 값을 가져올 수 있음!

            select
                1,
                2
            from 
                <if test = "파라미터.equals('비교값')">
                    db명.테이블명
                </if>
