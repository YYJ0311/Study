# 사용
    내장되어 있는 spring task 기능을 사용해서 scheduler를 구현한다.

    mvc 패턴과 같이 사용
        스케줄을 저장할 클래스를 별도로 작성, 해당 클래스에 @Component를 붙이고, 스케줄 설정함 (@Scheduled(cron=" ~ "))
        사용자의 요청을 받아서 실행되는 경로(controller - service)에서 스케줄 클래스를 new로 가져와서 스케줄이 저장된 클래스의 메소드 호출

# 설정
    appServlet > servlet-context.xml
        - bean 태그에 task 추가
            <beans:beans xmlns="~"
                xmlns:xsi="~"
                xmlns:task="http://www.springframework.org/schema/task"
                
                xsi:schemaLocation=" ~.xsd
                    ~.xsd
                    http://www.springframework.org/schema/task http://www.springframework.org/schema/task/spring-task-3.1.xsd">

        - 스케줄러 파일이 존재하는 패키지 찾기 & 스케줄러 pool size 설정
            servlet-context.xml에서 다음 코드 추가
            
            <context:component-scan base-package="패키지 경로" />
                <task:scheduler id="jobScheduler" pool-size="10" />
                <task:annotation-driven scheduler="jobScheduler" />

    클래스 파일
        @Component
        public class SchedulerTest {
            private static final Logger logger = LoggerFactory.getLogger(SchedulerTest.class);
            
        //	매 0초마다 실행됨
            @Scheduled(cron = "0 * * * * *")
            public void autoUpdate() throws Exception {
                logger.info(new Date() + "스케줄러 실행");
            }
        }

        => Tue Nov 22 14:27:00 KST 2022스케줄러 실행
           Tue Nov 22 14:28:00 KST 2022스케줄러 실행
           ...
    
    클래스파일에 Job과 원하는 스케줄 시간을 작성하여 사용