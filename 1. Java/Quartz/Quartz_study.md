# Job and Triggers
    Quartz 설계자들은 Job과 스케줄을 분리하였다. 
    Quartz에서 Trigger는 Job이 트리거링 되거나 발생되어야 할 때, Scheduler에게 알려주는데 사용된다. 
    Quartz 프레임워크에서는 간단한 Trigger 타입들을 제공하고 있는데, SimpleTrigger와 CronTrigger가 가장 일반적으로 사용된다.

# SimpleTrigger와 CronTrigger
    Quartz에서 사용하는 trigger의 종류

    SimpleTrigger는 스케줄을 간단히 발생시키는데 사용될 목적으로 설계되었다. 일반적으로, 주어진 시간에 Job을 발생시켜 (m) 초 간격을 두고 여러 번(n) 이를 실행할 필요가 있을 경우, SimpleTrigger가 적합한 선택이 된다. 반면, Job에 요구되는 스케줄링이 복잡할 경우, CronTrigger가 적합할 것이다.

    SimpleTrigger
        interval, delay, repeat times 등을 설정할 수 있다
        Job 을 특정 시간에 실행되게 하거나 특정 기간에 반복 수행하도록 할 시에 사용됨

    CronTrigger
        공백으로 구분되는 6~7 자리의 문자로 수행시간이 설정됨
        크론 표현식
            https://en.wikipedia.org/wiki/Cron#CRON_expression 참조

            ex) 초 분 시 일 월 요일 연도
                0 15 10 * * ? 2014 : 2014년 동안 매일 오전 10시 15분에
                0 10,44 14 ? 3 WED : 3월 동안 매주 수요일 오후 2 :10과 2:44분에
                0 0 12 1/5 * ? : 해당 월의 첫날부터 시작하여 매월 5일 마다 평일 정오에

            크론 생성 사이트 : http://www.cronmaker.com/
            
# System.currentTimeMillis()
    1970-1-1 부터 경과한 시간을 long 타입, ms(1/1000초) 단위로 리턴

# scheduler.scheduleJob(jobDetail, trigger);
    jobDetail : Job의 실제 구현 내용과 Job 실행에 필요한 제반 상세 정보가 담겨 있다.
    trigger : Job을 언제, 어떤 주기로, 언제부터 언제까지 실행할지에 대한 정보가 담겨 있다.
    scheduler : jobDetail과 trigger에 담긴 정보를 이용해서 실제 Job의 실행 스케줄링을 담당한다.

# properties 파일 생성 & 위치
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
                <param-value>/com/company/scheduler/quartz.properties
                </param-value>
            </init-param>
        </servlet>