# 구조도
    Job 인터페이스 
        : 실제 수행되는 execute 메소드를 명시함. 개발자는 해당 메소드를 구현한다.
    JobDetail 인터페이스 
        : Job 구현 객체를 실행시키기 위한 정보를 정의함
            JobClass (Job 구현 클래스)
            Description (Job 설명)
            JobDataMap (Job 실행시 필요한 정보)
    Trigger 인터페이스 
        : Job 실행조건 정의
    Scheduler 인터페이스 
        : 등록된 Job과 Trigger를 관리하는 기능 정의
    JobListener 인터페이스 
        : Job 수행 전, 완료 이벤트와 중단 이벤트를 확인할 수 있는 기능을 정의
    JobStore 인터페이스 
        : Job, Trigger 정보를 저장하는 메커니즘을 정의. 메모리 또는 데이터베이스를 사용함.

# Job and Triggers
    Quartz 설계자들은 Job과 스케줄을 분리하였다. 
    Quartz에서 Trigger는 Job이 트리거링 되거나 발생되어야 할 때, Scheduler에게 알려주는데 사용된다. 
    Quartz 프레임워크에서는 간단한 Trigger 타입들을 제공하고 있는데, SimpleTrigger와 CronTrigger가 가장 일반적으로 사용된다.

# Quartz에서 사용하는 trigger의 종류
    SimpleTrigger와 CronTrigger
        SimpleTrigger는 스케줄을 간단히 발생시키는데 사용될 목적으로 설계되었다. 일반적으로, 주어진 시간에 Job을 발생시켜 (m) 초 간격을 두고 여러 번(n) 이를 실행할 필요가 있을 경우 SimpleTrigger가 적합한 선택이 된다. 
        반면, Job에 요구되는 스케줄링이 복잡할 경우, CronTrigger가 적합할 것이다.

    SimpleTrigger
        interval, delay, repeat times 등을 설정할 수 있다
        Job 을 특정 시간에 실행되게 하거나 특정 기간에 반복 수행하도록 할 시에 사용됨

    CronTrigger
        공백으로 구분되는 6~7 자리의 문자(cron 표현)로 수행시간이 설정됨
            
# System.currentTimeMillis()
    1970-1-1 부터 경과한 시간을 long 타입, ms(1/1000초) 단위로 리턴

# scheduler.scheduleJob(jobDetail, trigger);
    jobDetail : Job의 실제 구현 내용과 Job 실행에 필요한 제반 상세 정보가 담겨 있다.
    trigger : Job을 언제, 어떤 주기로, 언제부터 언제까지 실행할지에 대한 정보가 담겨 있다.
    scheduler : jobDetail과 trigger에 담긴 정보를 이용해서 실제 Job의 실행 스케줄링을 담당한다.

# properties 파일 생성 & 파일 위치
    생성 방법
        others > General > Untitled Text File 로 생성하고 필요한 설정 적으면 됨

    다른 설정을 하지 않고 properties 파일의 설정을 적용시키려면 다음의 경로에 위치해야 한다.
        webapp/WEB-INF/classes/quartz.properties

    web.xml에서 경로 지정
        <servlet>
            <servlet-name>QuartzInitializer</servlet-name>
            <servlet-class>org.quartz.ee.servlet.QuartzInitializerServlet</servlet-class>
            <init-param>
                <param-name>config-file</param-name>
                <param-value>/com/company/scheduler/quartz.properties</param-value>
            </init-param>
        </servlet>

# Quartz와 Batch 차이
    quartz가 제공하는 기능, Job Scheduling
        특정한 시간에 등록한 작업(job)을 자동으로 실행시키는 일

    Batch가 제공하는 기능, Batch Job
        일괄처리. 여러 개의 작업(job)을 중단 없이 연속적으로 처리하는 일
        사용자와의 상호 작용 없이 여러 작업(job)들을 미리 정해진 순서에 따라 일괄적으로 처리
        정기적인 수행을 위해 Job Scheduling 기능을 이용해야 함

# Quartz 장단점
    장점
        데이터베이스를 기반으로 클러스터링(clustering) 기능을 제공한다
        시스템의 failover와 라운드-로빈(round-robbin) 방식의 분산 처리를 지원
        기본적으로 여러가지 플러그인(plug-in)을 제공한다
            ShutdownHookingPlugin - JVM 종료 이벤트를 확인하고 스케줄러에게 종료를 알림
            LoggingJobHistoryPlugin - Job 실행에 대한 로그를 남김
    단점
        클러스터링 기능을 제공하지만, 단순한 랜덤(random) 방식이라 완벽한 분산 처리는 안 됨
        ADMIN UI 제공 X
        스케줄링 실행에 대한 history 보관 X
            => 스프링부트에서 history를 제공해주므로 보완 가능
        Fixed Delay 타입을 보장하지 않으므로 해당 타입을 사용하려면 추가 작업 필요