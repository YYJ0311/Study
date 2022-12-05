# maven war 프로젝트 Cannot access defaults field of Properties 에러
    처음 infocar_Server2 프로젝트를 import 했을 때, pom.xml 첫줄에 오류발생
    해결방법) pom.xml에 maven-war-plugin을 추가한다.

    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.3.2</version>
    </plugin>

# project configuration is not up-to-date with pom.xml 에러
    import 이후 프로젝트 최상단에 X 표시 생성되어있음
    해결방법) alt + f5를 눌러서 프로젝트를 업데이트 시킨다.
        그래도 안 되면 "Force Update of Snapshots/Releases" 를 선택하고 업데이트

# Cannot find DTD '경로'. 에러
    log4j.xml 파일을 열었을 때 발생함
    해결방법
        1. log4j.dtd 를 다운받아서 설정한 경로에 넣어주기
            <!DOCTYPE log4j:configuration PUBLIC "-//APACHE//DTD LOG4J 1.2//EN" "log4j.dtd"> 에서 마지막이 경로임.

            다운로드 방법
                1) https://logging.apache.org/log4j > legacy site > log4j 1.2 > download 에서 zip 파일 다운로드 후, src > main > resources > org > apache > log4j > xml 폴더 내 dtd 파일 압축해제

                2) https://logging.apache.org/log4j > legacy site > log4j 1.2 > JavaDoc > Packages : org.apache.log4j > org.apache.log4j.xml > DOMConfigurator 에서 log4j.dtd 파일 다운로드

        2. log4j.xml 에서 log4j.dtd 경로 바꾸기
            수정 전 : <!DOCTYPE log4j:configuration PUBLIC "-//APACHE//DTD LOG4J 1.2//EN" "log4j.dtd">

            수정 후 : <!DOCTYPE log4j:configuration PUBLIC "-//APACHE//DTD LOG4J 1.2//EN" "https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/xml/doc-files/log4j.dtd">

        3. 파일 넣고 이클립스 재실행

        => 이 에러는 프로젝트의 java 버전과 컴퓨터의 java 버전이 맞지 않아 발생하기도 하는 것 같다. 컴퓨터의 java 버전을 바꿔주면 해결 되었음.

# The server time zone value '´ëÇÑ¹Î±¹ Ç¥ÁØ½Ã'
    root-context.xml에서 db 주소를 바꾼 뒤 생긴 에러

    이유) MySQL Connector java 5.1.x 버전 이상에서 제대로 시간을 읽지 못해서 생기는 듯

    해결방법
        db주소 뒤에 serverTimezone=UTC를 붙여준다.
        ex) <property name="url" value="jdbc:mysql://db주소:포트번호/db명?serverTimezone=UTC&amp;"/>

# mockMvc 테스트 에러
    1. Class<SpringJUnit4ClassRunner> cannot be resolved to a type
        @RunWith 가 제대로 import되지 않고 빨간줄 에러남
        
        해결방법
            - pom.xml에서 org.springframework-version과 spring-test의 버전을 똑같게 맞춰줌
            - spring-test의 scope 항목을 주석처리
    
    2. WebAppConfiguration cannot be resolved to a type
        @WebAppConfiguration 빨간줄 에러

        해결방법
            - 스프링 프레임워크 버전을 3.2 이상으로 변경
            - spring-test의 scope 항목을 주석처리

# Dynamic Web Module 4.0 requires Java 1.8 or newer.
    폴더 탐색창에는 어디서 난 에러인지 안 보임

    해결방법
        pom.xml에서 maven-compiler-plugin 아래 source와 target의 숫자를 jdk 버전과 일치시킴
            <source>1.8</source>
            <target>1.8</target>

# java.lang.UnsupportedClassVersionError
# ~ has been compiled by a more recent version of the Java Runtime
# org/springframework/scheduling/quartz/JobDetailFactoryBean has been compiled by a more recent version of the Java Runtime
    특정 파일의 컴파일 버전이 설치된 자바 버전보다 높아서 생기는 오류

    해결방법
        일반적으로는 프로젝트 jdk 버전을 올려서 해결함
        근데 내가 겪은 건 dependency 추가 후 생긴 에러여서 찾아본 결과, spring-context-support의 버전을 낮추니 오류가 없어졌다.
        <dependency>
		    <groupId>org.springframework</groupId>
		    <artifactId>spring-context-support</artifactId>
		    <version>6.0.0</version>
		</dependency>
        버전 6.0.0에서 생긴 오류가 5.2.9.RELEASE 에선 사라짐
        jdk 8버전이 spring-context-support 6버전과 호환 불가해서 생긴 오류였다.
        
# Error creating bean with name XXX defined in ServletContext resource [/WEB-INF/spring/root-context.xml]
    경로가 root-context라고 나와서 거기만 찾아봤는데, 문제는 거기가 아니라 servlet-context.xml(dispatcher-servlet.xml)이었다.

    해결방법
        <context:component-scan base-package="co.kr.infocar"/>
        를 다음과 같이 바꿈
        <context:component-scan base-package="co.kr.infocar">
            <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Service"/>
            <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Repository"/>	 
	    </context:component-scan>

# Error creating bean with name 'dataSource' defined in ServletContext
# Invalid bean name 'txAdvice' in bean reference
    스프링과 DB를 연동할 때 dataSource를 빈으로 생성하지 못함

    해결방법
        찾는중

# Class '~' not found [config set: testQuartz/web-context]
    실제 클래스가 없는지 확인(jar 파일 유무 확인)
    패키지명이나 클래스명, jar파일 모두 이상이 없으면 상태(nature)를 제거했다가 다시 추가한다.

    프로젝트 우클릭 - spirng - Remove Spring Project Nature -  Add Spring Project Nature

# 기본 클래스 help.me.from.App을(를) 찾거나 로드할 수 없습니다.
    test에 작성한 클래스 파일을 실행하면 위 문구가 나왔다.
    다른 이유로 클래스 파일을 읽지 못해 생긴 오류인 것 같다
    실행될 경로를 수동으로 잡아준다.

    해결방법
        1. 이클립스 메뉴 중 Run -> run configurations -> Classpath -> User Entries -> 우측 Advanced -> Add Folders -> 해당 프로젝트 클릭 후 -> classes 선택

        2. 프로젝트 우클릭 - properties - run/debug settings - 모두 delete - new - Main class에 실행하고자 하는 클래스 선택 - apply

# Failed to classload type while reading annotation metadata.
# java.lang.ClassNotFoundException
    시도한 것들
        프로젝트 clean
        maven update
        job 설정 xml 내용 삭제
        jackson 최신버전 주입
        

# Could not create connection to database server.
    프로젝트에 사용한 mysql 버전이 낮아서 에러 발생
    해결방법
        pom.xml에 설정된 mysql 버전을 올려서 해결
        <dependency>
            <groupId>mysql</groupId> 
            <artifactId>mysql-connector-java</artifactId> 
            <version>8.0.23</version>
        </dependency>

# web.xml is missing and <failOnMissingWebXml> is set to true
    갑자기 생김

    해결방법
        <build>아래에 failOnMissingWebXml 세팅 false로 추가

        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <version>2.4</version>
            <configuration>
                <warSourceDirectory>src/main/webapp</warSourceDirectory>
                <warName>sample</warName>

                <failOnMissingWebXml>false</failOnMissingWebXml>
            </configuration>
        </plugin>

# yaml) expected <block end>, but found BlockMappingStart
    yaml 파일에서 에러 발생

    해결방법
        들여쓰기 확인, 재입력

# jpa test) No matching tests found in any candidate test task.
    @Test 어노테이션의 import를 잘못해서 인식을 못 함

    해결방법
        import org.junit.Test;
        대신에
        import org.junit.jupiter.api.Test;
        로 사용한다.

    그리고 test에선 print 찍어도 안 나온다.

# proeprties 파일 한글 깨짐
    방법1. 인코딩 타입 변경
        Window - Preferences - General > Content Types > Text 와 Text > Java Properties File을 한번씩 클릭하고 각각 Default enxoding을 UTF-8로 Update & Apply and Close

    방법2. 플러그인 설치
        Help - Install New Software - Add - Location에 다음 주소 입력하고 Add
        http://propedit.sourceforge.jp/eclipse/updates/
        파일 로딩이 끝나면 가장 아래에 ProeprtiesEditor 체크하고 설치