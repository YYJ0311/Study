# quartz 스케줄러와 batch 작업을 동시에 하는 프로젝트 작성 과정
# https://www.youtube.com/watch?v=hcNf-h8CU4g
# 1. task 생성(tasklet)
    task 폴더 아래에 task 수만큼 클래스 생성
    task 클래스에 tasklet을 implements 하고 task 코드 작성

# 2. Job 생성
    job폴더 아래에 Job 클래스를 생성하고 QuartzJobBean을 상속받음(extends)
    jobName, JobLauncher, JobLocator 변수를 지정하고 setter, getter 메소드 생성
    QuartzJobBean의 executeInternal를 override함
        job 생성
        job 시작

# 3. Job Runner 생성
    config 폴더 아래에 job을 포함한 여러 설정을 정의하기 위한 config 클래스를 생성
    1) BatchConfig 생성해서 batch 설정
        @Configuration 와 @EnableBatchProcessing 어노테이션 추가
        JobBuilderFactory와 StepBuilderFactory 를 @Autowired로 연결
        step 메소드를 정의하고 tasklet으로 위에서 정의했던 task를 수행하는 코드 작성
        job 메소드를 정의하고 바로 전에 만든 step을 수행하는 코드 작성

    2) QuartzConfig 생성해서 트리거와 job을 등록
        @Configuration 추가
        JobLauncher와 JobLocator에 연결
        JobDetail 클래스에서 jobDataMap을 구성하고, JobBuilder로 위에서 만든 job을 읽고 설정함

        Trigger생성
            job 반복실행 간격 설정
            jobOneDetail를 가지고 job 설정 완료

        quartz 설정파일 생성
            main > resources 폴더 아래에 quartz.properties 파일을 생성
            해당 파일에서 스케쥴러 이름, 쓰레드 수, jobStore 등을 설정할 수 있음

        Properties 생성
            PropertiesFactoryBean 생성
            PropertiesFactoryBean 에 위에서 만든 quartz.properties 파일의 위치를 set
        
        SchedulerFactoryBean 생성
            SchedulerFactoryBean 에 trigger를 set
            SchedulerFactoryBean 에 quartz 설정파일 set
            SchedulerFactoryBean 에 JobDetail를 set
            