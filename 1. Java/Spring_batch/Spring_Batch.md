# 스프링 배치(Spring Batch)
    대용량 일괄처리의 편의를 위해 설계된 가볍고 포괄적인 배치 프레임워크
    로깅/추적, 트랜잭션 관리, 작업 처리 통계, 작업 재시작, 건너뛰기, 리소스 관리 등의 기능을 제공
    배치가 실패하여 작업 재시작을 하게 된다면 처음부터가 아닌 실패한 지점부터 실행을 하게 되고, 중복 실행을 막기 위해 성공한 이력이 있는 Batch는 동일한 Parameters로 실행 시 Exception이 발생한다.

    Spring의 특성을 그대로 가져왔기 때문에 DI, AOP, 서비스 추상화 같은 Spring 프레임워크의 3대 요소를 모두 사용할 수 있다.

# 사용 예
    - 대용량의 비즈니스 데이터를 복잡한 작업으로 처리해야하는 경우
    - 특정한 시점에 스케쥴러를 통해 자동화된 작업이 필요한 경우 (ex. 푸시알림, 월 별 리포트)
    - 대용량 데이터의 포맷을 변경, 유효성 검사 등의 작업을 트랜잭션 안에서 처리 후 기록해야하는 경우
    - 데이터베이스 파일 읽기 또는 저장 프로시저 실행
    - 데이터베이스 간에 대량 데이터 이동, 변환

    Spring Batch는 로깅/추적, 트랜잭션 관리, 작업 처리 통계, 작업 재시작, 건너뛰기, 리소스 관리 등 대용량 레코드 처리 에필 수적인 재사용 가능한 기능을 제공한다. 또한 최적화 및 파티셔닝 기술을 통해 대용량 및 고성능 일괄 작업을 가능하게 하는 고급 기술 서비스 및 기능을 제공한다.

# 사용 조건
    배치 애플리케이션은 다음의 조건을 만족해야만 한다.

    - 대용량 데이터 : 대량의 데이터를 가져오거나, 전달하거나, 계산하는 등의 처리를 할 수 ​​있어야 한다.
    - 자동화 : 심각한 문제 해결을 제외하고는 사용자 개입 없이 실행되어야 한다.
    - 견고성 : 잘못된 데이터를 충돌/중단 없이 처리할 수 있어야 한다.
    - 신뢰성 : 무엇이 잘못되었는지를 추적할 수 있어야 한다. (로깅, 알림)
    - 성능 : 지정한 시간 안에 처리를 완료하거나 동시에 실행되는 다른 애플리케이션을 방해하지 않도록 수행되어야 함.

# Batch와 Quartz / Scheduler
    Spring Batch는 Scheduler가 아니기에 비교 대상이 아니다. 
    Quartz는 스케줄러의 역할, Batch는 대용량 데이터 배치 처리기능을 한다. 
    Quartz + Batch로 조합해서 많이 사용한다.

# 계층 구조 1
    Application <-> Batch Core <-> Batch Infrastructure <-> Application
    
    Application
        Spring Batch를 사용하여 개발자가 작성한 모든 배치 작업과 사용자 정의 코드
    Batch Core
        배치 작업을 시작하고 제어하는데 필요한 핵심 런타임 클래스를 포함
    Batch Infrastructure
        개발자와 애플리케이션에서 사용하는 일반적인 Reader와 Writer 그리고 RetryTemplate와 같은 서비스를 포함

    위와 같은 구조 덕분에 개발자는 Application 계층의 비즈니스 로직에 집중할 수 있고, 배치의 동작과 관련된 것은 Batch Core에 있는 클래스들을 이용하여 제어할 수 있다.

# 계층 구조 2
    JobRepository
     ├─ Job
     │   │
     ├─ JobLauncher
     │   │
     └─ Step
         ├─ ItemReader
         ├─ ItemProcessor
         └─ ItemWriter

    JobRepository
        모든 배치 처리 정보를 담고있는 매커니즘
        다양한 배치 수행과 관련된 수치 데이터와 Job의 상태를 유지 및 관리한다.
        Job이 실행되면 JobRepository에 JobExecution과 StepExecution을 생성하고, JobRepository에서 Execution 정보들(Step, 현재 상태, 읽은 아이템 및 처리된 아이템 수 등)을 저장하고 조회하며 사용하게 된다.

        일반적으로 관계형 데이터베이스를 사용하며 스프링 배치 내의 대부분의 주요 컴포넌트가 공유한다.
    Job
        배치 처리 과정을 하나의 단위로 만들어 표현한 객체이고, 여러 Step 인스턴스를 포함하는 컨테이너이다.
        배치처리 과정에 있어서 전체 계층 최상단에 위치한다.

        Job이 실행될 때 스프링 배치의 많은 컴포넌트는 탄력성(resiliency)을 제공하기 위해 서로 상호작용을 한다.
    JobLauncher
        Job과 JobParameters를 사용하여 Job을 실행하는 객체 (Job.execute을 호출)
        Job의 재실행 가능 여부 검증, 잡의 실행 방법, 파라미터 유효성 검증 등을 수행한다.
        스프링 부트의 환경에서는 부트가 Job을 시작하는 기능을 제공하므로, 일반적으로 직접 다룰 필요가 없는 컴포넌트다.
        Job을 실행하면 해당 잡은 각 Step을 실행한다. 각 스텝이 실행되면 JobRepository는 현재 상태로 갱신된다.    
    Step
        스프링 배치에서 가장 일반적으로 상태를 보여주는 단위
        각 Step은 Job을 구성하는 독립된 작업의 단위로, Job은 최소한 1개 이상의 Step을 가져야 하며 Job의 실제 일괄 처리를 제어하는 모든 정보가 들어있다.
        Step은 Tasklet, Chunk 2가지의 처리방식을 지원한다.
    Tasklet
        하나의 메소드로 구성되어 있는 간단한 인터페이스
        Step이 중지(예외 반환 또는 throw)될 때까지 execute 메서드가 계속 반복해서 수행하고 수행할 때마다 독립적인 트랜잭션이 얻어진다. 
        초기화, 저장 프로시저 실행, 알림 전송과 같은 잡에서 일반적으로 사용된다.
    Chunk
        한 번에 하나씩 데이터(row)를 읽어 Chunk라는 덩어리를 만든 뒤, Chunk 단위로 트랜잭션을 다룬다.
        Chunk 단위로 트랜잭션을 수행하기 때문에 실패할 경우엔 해당 Chunk 만큼만 롤백이 되고, 이전에 커밋된 트랜잭션 범위까지는 반영이 된다.
        Chunk 기반 Step은 ItemReader, ItemProcessor, ItemWriter라는 3개의 주요 부분으로 구성될 수 있고 다음과 같이 실행된다.
            읽기(Read) : DB에서 배치처리를 할 Data를 읽어온다
            처리(Processing) : 읽어 온 Data를 가공, 처리한다.
            쓰기(Write) : 가공, 처리한 데이터를 DB에 저장한다.

            ItemReader와 ItemProcessor에서 데이터는 1건씩 다뤄지고, Writer에선 Chunk 단위로 처리된다.
    
        Chunk 지향 처리에서 배치 수행 코드
            List items = new Arraylist();
            for(int i = 0; i < commitInterval; i++){
                Object item = itemReader.read()
                Object processedItem = itemProcessor.process(item);
                items.add(processedItem);
            }
            itemWriter.write(items);

        일반적으로 스프링 배치는 대용량 데이터를 다루는 경우가 많기 때문에 Tasklet보다 상대적으로 트랜잭션의 단위를 짧게 하여 처리할 수 있는 Chunk 지향 프로세싱(ItemReader, ItemProcessor, ItemWriter)을 이용한다.

    ItemReader
        Step에서 Item을 읽어오는 인터페이스
        ItemReader에 대한 다양한 인터페이스가 존재하며 다양한 방법으로 Item을 읽어 올 수 있다.
    ItemProcessor
        Reader에서 읽어온 Item의 데이터를 처리함
        배치를 처리하는데 필수 요소는 아니며 Reader, Processor, Writer 처리를 분리하여 각각의 역할을 명확하게 구분한다.
    ItemWriter
        처리 된 Data를 Writer 할 때 사용
        Writer는 처리 결과물에 따라 Insert 또는 Update가 될 수 있고, Queue를 사용한다면 Send가 될 수도 있다. 
        Read와 동일하게 다양한 인터페이스가 존재한다.
        기본적으로 Item을 Chunk로 묶어 처리한다.
    
# Chunk Size와 Paging
    Spring Batch에는 다양한 ItemReader와 ItemWriter가 존재한다. 대용량 배치 처리를 하게되면 item을 읽어올 때 Paging 처리를 하는게 효과적이며, Reader에서는 이 Paging 처리를 지원하고 있다.
    또한 적절한 Paging 처리와 Chunk Size를 설정하여 더욱 효과적인 배치처리를 할 수 있다.

    Paging Size가 5, Chunk Size가 10인 경우, 2번의 Read가 이루어진 후에 1번의 Transaction이 수행된다. 즉, 1번의 Transaction을 위해 2번의 쿼리 수행이 발생하는 것이다.
    1번의 Read 쿼리 수행시 1번의 Transaction이 수행되는 것이 성능을 위한 가장 적절한 Paging Size와 Chunk Size이기 때문에, 둘을 동일하게 설정하는 것이 추천된다.

# 그 외 Spring Batch 용어
    JobInstance
        Job의 실행의 단위
        Job을 실행시키면 하나의 JobInstance가 생성된다.
        예를들어 1월 1일 실행, 1월 2일 실행을 하게 되면 각각의 JobInstance가 생성되며 1월 1일 실행한 JobInstance가 실패하여 다시 실행을 시키더라도 이 JobInstance는 1월 1일에 대한 데이터만 처리한다.

    JobParameters
        JonInstance를 구분하는 단위. JobParameters 객체로 JonInstance를 구분한다.
        JobInstacne에 전달되는 매개변수 역할도 함.

        String, Double, Long, Date 4가지 형식만 지원

    JobExecution
        JobInstance 실행 시도에 대한 객체
        1월 1일에 실행한 JobInstacne가 실패하여 재실행을 하여도 동일한 JobInstance를 실행시키지만 이 2번에 실행에 대한 JobExecution은 개별로 생기게 된다. 
        JobExecution는 이러한 JobInstance 실행에 대한 상태,시작시간, 종료시간, 생성시간 등의 정보를 담고 있다.

    StepExecution
        JobExecution과 동일하게 Step 실행 시도에 대한 객체이며, 실제 시작이 될 때만 생성된다.
        하지만 Job이 여러개의 Step으로 구성되어 있을 경우 이전 단계의 Step이 실패하게 되면 다음 단계가 실행되지 않으므로 실패 이후 StepExecution은 생성되지 않는다. 
        StepExecution에는 JobExecution에 저장되는 정보 외에 read 수, write 수, commit 수, skip 수 등의 정보들도 저장된다.

    ExecutionContext
        Job에서 데이터를 공유 할 수 있는 데이터 저장소
        ExecutionContext의 종류는 JobExecutionContext, StepExecutionContext 2가지가 있고 각각은 지정되는 범위가 다르다.

        JobExecutionContext은 Commit 시점에 저장되고, StepExecutionContext은 실행 사이에 저장된다.

        ExecutionContext를 통해 Step간 Data 공유가 가능하며, Job 실패시 ExecutionContext를 통한 마지막 실행 값을 재구성 할 수 있다.

# MySQL 연동과 Meta Table
    Spring Batch는 비즈니스 로직만 작성해서 정상적으로 실행되지 않는다! 
    개발자가 작성한 작업이 아주 잘 만들어졌다고 하더라도, 주기에 따라 지속적으로 작동한다면 오류가 생길 수밖에 없다. 
    따라서 Spring Batch에서는 작업을 수행하면서 일련의 상태에 관한 메타 데이터들을 메타 테이블에 저장해서 실패한 작업에 대한 기록을 남겨 이후의 일어날 수도 있는 실패를 대비 할 수 있다.

    메타 테이블을 사용하기 위해 DB와 Batch를 연동해야 한다.
    연동하는 방법은 DB에 Batch가 사용하는 table을 직접 만들거나, 프로젝트 실행 시 자동으로 만들게 할 수 있다. 
    하지만 application이 DDL에 대한 권한(테이블 생성)을 갖는 것은 추천되지 않으므로, SQL문을 직접 실행하는 것이 낫다.

    sql문은 프로젝트 내부 Spring Batch JAR 파일(Maven Dependencies에서 org.springframework.batch.core)을 확인거나, 공식 사이트(https://docs.spring.io/spring-batch/docs/3.0.x/reference/html/metaDataSchema.html)에서 확인 가능

    테스트용 자동 생성
        <jdbc:initialize-database data-source="dataSource"> 
            <jdbc:script location="org/springframework/batch/core/schema-drop-mysql.sql" /> 
            <jdbc:script location="org/springframework/batch/core/schema-mysql.sql" /> 
        </jdbc:initialize-database>

# Batch Meta Table
    BATCH_JOB_INSTANCE
        실행한 Job에 대한 기록
        JobInstance에 대한 모든 정보를 가지고 있다

        JOB_INSTANCE_ID : pk
        VERSION : 해당 레코드에 update 될 때마다 1씩 증가
        JOB_NAME : 실행한 Job의 이름
        JOB_KEY : 실행 시점에 부여된 값으로, JobParameter의 값을 통해 식별함

    BATCH_JOB_EXECUTION
        BATCH_JOB_INSTANCE의 부모테이블
        BATCH_JOB_INSTANCE가 실행했던 Job의 성공/실패 내역을 보여준다

        Batch는 실패한 실행에 대해서 동일한 파라미터로 다시 실행 요청이 들어와도 실행시켜준다
    
    BATCH_JOB_EXECUTION_PARAMS
        테이블의 파라미터 값을 담고 있는 테이블
