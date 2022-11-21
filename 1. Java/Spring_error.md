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