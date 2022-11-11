## STS4에서 MVC 프로젝트(Spring Legacy Project) 만들기
    기존 STS3 에서는 [Spring Legacy Project]를 통해 새로운 MVC 프로젝트를 생성하면 되었지만, STS4에서는 [Spring Legacy Project]를 포함해서 STS3에서 기본적으로 제공해주던 기능이 없어졌다.

    그 이유는 STS4는 STS3를 기반으로 만든 것이아니라 SpringBoot 사용 환경에 맞도록 완전히 새로 제작된 제품이기 때문.
    STS4 출시 초반 기존 STS3에 익숙한 사용자들이 많은 불만과 기존 기능 추가를 요청하였고 이러한 요청들로 인해 Spring 개발자들은 STS3에 있었던 기능들을 Eclipse Marketplace를 통해 설치할 수 있도록 제공함

    따라서 "sts3 add-on for sts 4"를 추가 설치하면 spring 프로젝트를 생성할 수 있다.
    => sts4 버전이 업데이트 되고, sts add-on의 지원이 중단되면서 sts4에서 더이상 spring legacy project 생성이 불가해졌다!!!

    sts3는 jdk 11 이후의 버전만 지원한다!!

# STS 개념
    STS랑 Eclipse랑 같음
    sts는 eclipse에 스프링 관련 플러그인이 미리 설치돼서 배포되는 버전이다

# spring tools3 사용
    설치
        sts3는 지원이 중단되었기 때문에 github의 archive에서 다운받는다
        https://github.com/spring-attic/toolsuite-distribution/wiki/Spring-Tool-Suite-3
        압축해제 후 sts.exe 파일 실행
    
    실행
        jdk 1.8로 실행하려고 하면 최소 11이 필요하다고 나온다.
        11 이상의 jdk를 설치한 뒤 프로젝트 안에서 project facets, java compiler의 jdk를 내가 필요한 1.8버전으로 바꾼다.

    프로젝트 생성
        new - other - spring>spring legacy project - Spring MVC Project로 생성
        
    db 연결
        pom.xml dependency에 다음 라이브러리 추가
            mysql : mysql 연동
            jdbc : jdbc 라이브러리
            MyBatis : mybatis
            mybatis-spring : spring에서 사용할 mybatis 정보

        root-context.xml에 DBMS 객체 설정
            JDBC-MYSQL
                jdbc.properties 생성 후 넘겨 줄 데이터 작성
            MyBatis-Spring
                mybatis-config.xml 생성

    resource annotation 사용을 위한 dependency
        javax.annotation-api 추가

# ??
    public abstract interface DistanceTimeMapper { }
    에서 abstract 있고 없고의 차이??

# 에러
    1. Error creating bean with name 'countDataController': Injection of resource dependencies failed; No bean named 'co.kr.mureung.src.CountData.service.Impl' is defined
        해결 ) root-context에서 xml을 제대로 인식하지 못해 생긴 오류였다
        <property name="mapperLocations" value="classpath:mappers/**/**_sql.xml"/>
        이 항목의 value를 다음과 같이 직접 입력함으로써 해결됨
        <property name="mapperLocations" value="/resources/mappers/**/**_sql.xml"/>

    2. 포스트맨으로 요청보내면 406에러 발생
        크롬으로 response headers를 확인해 보니 content-type이 text/html로 되어있는걸 볼 수 있었다.
        -> codehaus.jackson dependency를 추가했다.. 2개
        <dependency>
		    <groupId>org.codehaus.jackson</groupId>
		    <artifactId>jackson-core-asl</artifactId>
		    <version>1.9.13</version>
		</dependency>
		<dependency>
    		<groupId>org.codehaus.jackson</groupId>
		    <artifactId>jackson-mapper-asl</artifactId>
		    <version>1.9.13</version>
		</dependency>
        
        이게 있어야 content-type을 application/json으로 바꿔준다!!

    3. 에러 : NoClassDefFoundError: com/fasterxml/jackson/core/util/JacksonFeature
        jwt 클래스를 가져와서 토큰을 발급받고 update 하는 과정에서 오류 발생
        해결 ) 토큰 발급 서버와 api 실행 서버의 jackson 버전이 달라서 생긴 오류이다. api 서버 pom.xml의 jackson 라이브러리 버전을 토큰 서버의 버전과 동일하게 맞춰준다.