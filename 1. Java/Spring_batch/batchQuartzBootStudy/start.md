# 참고
    https://www.youtube.com/watch?v=wy99cPHlMlA
    https://jojoldu.tistory.com/328

# 파일 목적
    job과 step 간단한 사용 예시

# 사용
    1. 프로젝트 생성
        DevTools, Lombok, Spring Batch, JPA, MySQL Driver 추가해서 생성
    2. 기본 application 클래스에 배치파일 인식
        @EnableBatchProcessing 를 붙인다
    3. yaml 파일 설정
        db 사전 생성 및 연결
    4. task 생성
        TaskletJob 클래스 생성 & job과 step 구현
    5. db 테이블 생성
        job과 step 구현 뒤에 실행시켜보면 db에 테이블이 없다고 나온다.
        Project and External Dependencies - spring-batch-core - schema-db종류.sql 파일에서 sql문을 복사해서 수동으로 테이블과 레코드를 생성한다.
    6. 실행
        처음에 하나의 step1만 생성하여 테스트해보면, 첫 실행시에는 db에 기록이 되지만 이후에 다시 실행하면(같은 파라미터로 실행하면) 기록되지 않는다. 즉, batch는 재실행되지 않는다.

        재실행하기 위해서는 실행될 때 파라미터를 다르게 해줘야 한다.

        * 파라미터 변경
            프로젝트 우클릭 - run as.. - run configurations - arguments - program arguments에서 파라미터를 추가한다.

            ex) --job.name=job이름 v=버전정보
                --job.name=taskletJob v=1

        step 추가
            파라미터를 받으며 step1에 이어서 실행되는 step2를 추가한다.
            
            프로젝트의 파라미터로 date를 지정함
                --job.name=taskletJob date=20221201 v=2

            step의 파라미터로 (@Value("#{jobParameters[date]}") String date) 을 추가

            job에 next로 step2 실행(초기값 null)

        파라미터를 바꾸며 batch를 실행할 수 있다.

# db 튜플 읽기
    1. db에 대한 domain 정의
        domain 폴더 생성 후 그 아래에
            Dept 테이블에 대한 정보 클래스 생성,
            Dept repository 인터페이스로 생성(db에 파일을 CRUD하기 위한 CrudRepository 클래스 상속받아서 test로 데이터를 넣기 위함)
    2. 읽기 위한 더미 데이터 생성
        test 폴더 아래에 똑같이 domain 폴더와 TestDeptRepository 클래스 생성

        for문으로 CrudRepository의 save 메소드를 이용하여 데이터 입력

        이 때 테스트가 종료된 후에도 데이터가 남아있기 위해 @Commit 어노테이션 사용하기
    3. 튜플 읽는 job 생성
        batch 폴더 아래에 JpaPageJob1 클래스 생성
        job, step, reader와 read한 것을 확인하기 위한 writer 생성하고 log로 표시
    
# db 튜플 쓰기
    1. 쓰기용 타겟 db 정의
        Dept와 DeptRepository를 복붙해서 ~2 파일 생성
    2. job 생성
        복붙하고 이름 변경으로 JpaPageJob2 파일 생성
        내부의 job, step, reader, writer 이름 변경
    3. step 수정
        step 코드에 processor 추가하고 메소드도 추가
            processor에서 데이터를 가공함
        chunk의 out을 Dept2로 수정
    4. writer 수정
        ItemWriter -> JpaItemWriter
        jpaPageJob2_printItemWriter -> jpaPageJob2_dbItemWriter
        Dept2에 엔터티를 넣는 코드 작성

# text 읽기
    1. dto 생성
        하나씩 읽기 위한 OneDto 파일 생성
    2. 읽을 파일과 그 classpath 생성
        resources 폴더 아래에 sample 폴더 생성
        그 아래에 txt파일 생성
    3. job(TextJob1) 생성 및 코드작성
        job, step, reader 작성

# text 쓰기
    1. lineAggregator 커스텀
        custom 폴더, CustomPassThroughLineAggregator 클래스 생성
        LineAggregator<T> 상속받아서 item을 가공하여 return
        
        이렇게 custom하는 것은 원래 processor의 역할임
        여기서 custom을 쓴 것은 이렇게도 가능하다를 보여주기 위함
    2. 읽을 파일 생성
        쓰기 전에 참고할 읽을 파일을 sample에 생성
    3. Job(TextJob2) 생성 및 코드작성
        읽기 했던 것에서 writer추가
        위에서 만든 lineAggregator를 통한 쓰기 값 가공
    
# csv 읽기
    1. 읽을 csv 파일 생성
        구분자도 새로 지정해줄 것이므로 csv 기본 구분자인 "," 대신 ":" 로 구분해서 작성한다
            one:two
            1:일
            2:이
            ...
    2. job(CsvJob1) 생성 및 작성
        reader, step, job을 작성하고 reader에서 구분자와 기타 설정을 추가함

        읽을 때 타입을 가져오는 클래스에 어노테이션을 주의한다!

# csv 쓰기
    