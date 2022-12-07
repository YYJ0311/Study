# 멀티 db 사용
    1. 프로젝트 생성
        spring boot
        dependencies
            devtools, lombok, spring configuration process, batch, data jpa, mysql, google-collections 필요
    2. db 2개 생성
       데이터를 읽을 db에 batch meta 테이블 생성
       타겟 db은 테이블을 비움
    3. yaml 파일 설정
        db 2개 정의
    4. domain 파일들 생성
        db1 폴더 : Dept1, Dept1Repository
        db2 폴더 : Dept2, Dept2Repository
    5. db1과 매칭되는 DbConfig1 파일 작성
        yaml 설정과 mapping 시키기 위한 annotation추가
        @primary를 붙여서 DataSource, EntityManagerFactory, PlatformTransactionManager 생성하고 mapping
    6. 같은 방법으로 DbConfig2 생성
        @Primary 없음
    7. batch 파일(JpaPageJob2) 생성
        @Resource를 이용해서 DbConfig1에서 만들었던 entityManagerFactory와 mapping, datasource2와 mapping
        Job, Step, Reader/Processor/Writer 생성
            Writer는 Jdbc Writer를 사용
    8. dept1 테이블 생성
        다른 db로 이전시킬 데이터를 가진 테이블을 생성함
        test 패키지에서 repository를 불러와서 save를 통해 데이터 저장
    9. 실행
        db1 dept1 테이블에 있던 데이터가 db2 dept2 테이블로 복사됨