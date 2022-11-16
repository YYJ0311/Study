# 구동과정
    스프링 프로젝트를 생성하고 바로 실행하면 home.jsp가 실행된다. home.jsp가 구동되는 과정은 다음과 같다.
    1. 클라이언트 요청( /, root 페이지 요청)
    2. web.xml에서 dispatcherServlet가 클라이언트 요청을 핸들링
    3. servlet-context.xml에서 해당 클래스의 웹요청을 처리하는 컨트롤러를 사용(HandlerMapping으로 Controller를 검색)
    4. 해당 Controller가 요청을 처리후, home을 리턴
    5. View에 출력

# 이클립스 JDK 변경
    컴퓨터에 기존 설치돼있던 jdk가 12버전이어서 git에서 다운받은 8버전으로 만들어진 프로젝트를 import 했더니 다발적인 오류 발생
    => jdk 버전 변경으로 해결

    1. java 8(jdk 1.8) 다운로드 받아서 설치
    2. 이클립스 window > preferences > java > installed JREs에서 add - Standard VM - jdk 경로 설정 후 finish - 추가된 jdk 체크표시하기
    3. Java > compiler 에서 버전 1.8 설정하고 apply
    4. 프로젝트 우클릭 > properties > Java Build Path 에서 기존 JRE System Library 제거, Add Library 클릭 - JRE System Library 선택 - JRE 버전 확인하고 finish
    5. Java Compiler 버전 1.8로 변경
    6. Project Facets 에서 Java 1.8 버전 변경
    7. Apply and Close

# 스프링 톰캣 서버 설치
    콘솔창 위치에 Servers > create a new server... > tomcat 버전 선택 & 설치된 경로 입력 > 사용할 프로젝트 add 후 finish

# DispatcherServlet
    Model 파트와 Controller파트 View파트를 조합하여 브라우저로 출력해주는 역할을 수행하는 클래스

# web.xml
    웹프로젝트의 배치 기술서(deploy descriptor, 웹프로젝트의 환경설정파일)

    WAS가 처음 구동될 때 web.xml을 읽어 웹 애플리케이션 설정을 구성한다.
    DispatcherServlet을 등록해주면서 스프링 설정 파일을 지정한다.

    <context-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>/WEB-INF/spring/root-context.xml</param-value> <!-- 스프링의 환경설정 파일인 root-context.xml을 가장 먼저 참조 -->
    </context-param>
    
    <!-- Creates the Spring Container shared by all Servlets and Filters -->
    <listener>
        <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
    </listener>
 
    <!-- Processes application requests -->
    <servlet>
        <servlet-name>appServlet</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class> <!-- 스프링에 내장된 서블릿 클래스-->
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
            <!-- /WEB-INF/spring/appServlet/servlet-context.xml을 참조. xml 파일 안에 정의된 객체들을 로딩한다. -->
        </init-param>
        <load-on-startup>1</load-on-startup> <!-- 가장 첫번째 우선순위를 뜻한다. -->
    </servlet>
        
    <servlet-mapping>
        <servlet-name>appServlet</servlet-name>
        <url-pattern>/</url-pattern>
        <!-- DispatcherServlet이 모든 요청을 가로챌 수 있도록 등록 -->
        <!-- 특정 url으로 변경하여 사용가능 ex) *.do -->
    </servlet-mapping>

# root-context.xml
    스프링의 환경설정 파일

# servlet-context.xml
    web.xml에서 DispatcherServlet(스프링에 내장된 컨트롤러)로 이동하고, servlet-context.xml를 참조함

    <annotation-driven /> <!-- 어노테이션을 사용가능하도록 설정 -->
 
    <!-- Handles HTTP GET requests for /resources/** by efficiently serving up 
         static resources in the ${webappRoot}/resources directory -->
    <resources mapping="/resources/**" location="/resources/" />
 
    <!-- Resolves views selected for rendering by @Controllers to .jsp 
         resources in the /WEB-INF/views directory -->
    
    <beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver"> <!-- view resolver(뷰 리졸버, 뷰 해석기) -->

        <!-- 뷰(jsp)의 접두어, 접미어 설정 : 파일명만 작성할 수 있게 세팅 -->
        <beans:property name="prefix" value="/WEB-INF/views/" /> <!-- 접두어(디렉토리) -->
        <beans:property name="suffix" value=".jsp" /> <!-- 접미어(확장자) -->
    </beans:bean>

# pom.xml 에서 dependency와 plugin의 차이
    공통점 : 둘 다 Jar 파일
    차이점
        dependency 
            : 테스크가 실행되는 동안 classpath에서 사용할 수 있도록 프로젝트에서 요구하는 jar 파일
            프로젝트가 의존할 클래스의 패키지
        plugin 
            : 프로젝트 빌드 과정에서 무언가를 하기 위해 설정하는 jar 파일.
            대부분의 실행은 plugin을 가지고 실행한다.

## throws Exception 사용하는 이유
    프로그램 실행 중에 의도치 않은 오류가 생기면 도중에 비정상적으로 종료되면서 나머지 코드가 실행되지 않는다.
    그래서 자바에서는 예외 관련 프로그램을 정상적으로 종료하도록 도와주는데 이걸 Exception Handling(예외 처리) 라고 한다.
    
    예외가 발생한 곳에서 try ~ catch 블록으로 예외를 직접 처리할 수 있지만, 자신이 직접 처리하지 않고 메소드를 호출한 곳으로 예외를 위임할 때(넘김) throws 키워드를 사용

    예외 처리를 위임받은 메서드는 다시 예외 처리에 대한 책임이 발생하며, 자신이 직접 처리하거나 또 다른 곳으로 위임할 수 있음.

    최종적으로 마지막 단계의 메서드에서는 try ~ catch 블록을 통해 처리해야 함

# spring - sql문(mapper xml)에서 useGeneratedKeys와 keyProperty
    id가 auto_increment이고 name과 password를 받아서 db에 insert 하는 경우, id는 입력하지 않아도 자동으로 1씩 증가하며 저장된다.
    insert를 성공하면 추가된 id, name, password를 리턴하게끔 하면 id는 null로 나오게 되는데 이 때, useGeneratedKeys를 이용하여 id도 null값 대신 실제 증가된 값이 출력되게 만들 수 있다.
    
    getGeneratedKeys은 JDBC의 메소드로 자동 생성 키값들을 사용하기 위해서 사용된다.

    keyProperty는 리턴 된 키 값들을 어느 필드에 set 할 건지를 정한다. id를 적으면 id값을 받아온다.

    <insert id="insert" parameterType="타입 주소" useGeneratedKeys="True" keyProperty="id"> 와 같이 사용한다.

# servlet-context.xml / root-context.xml / web.xml 차이점
    우선, xml 파일은 모두 객체(Bean)를 정의함

    servlet-context.xml
        요청과 관련된 객체를 정의
        url과 관련된 controller나, @(어노테이션), ViewResolver, Interceptor, MultipartResolver 등의 설정을 함
    
    root-context.xml
        view와 관련되지 않은 객체를 정의
        Service, Repository(DAO), DB등 비즈니스 로직과 관련된 설정을 함

    web.xml
        설정을 위한 설정파일
        최초로 WAS가 최초로 구동될 때, 각종 설정을 정의
        여러 xml파일을 인식하도록 각 파일을 가리켜 준다.

# swagger
    프로젝트에서 지정한 URL들을 HTML 화면으로 확인할 수 있게 해주는 프로젝트
    API서버가 어떤 spec을 가진 데이터를 주고 받는지에 대한 문서를 자동으로 만들어준다

    dependency 추가, SwaggerConfig 파일에서 swagger설정, api 클래스에 @ApiOperation, api 메소드에 @ApiParam 등을 붙여서 표시할 정보를 선택할 수 있음
    서버 실행시키고 localhost:8080/swagger-ui.html로 접속하여 swagger를 사용할 수 있다.