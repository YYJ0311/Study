# 구동과정
    스프링 프로젝트를 생성하고 바로 실행하면 home.jsp가 실행된다. home.jsp가 구동되는 과정은 다음과 같다.
    1. 클라이언트 요청( /, root 페이지 요청)
    2. web.xml에서 dispatcherServlet가 클라이언트 요청을 핸들링
    3. servlet-context.xml에서 해당 클래스의 웹요청을 처리하는 컨트롤러를 사용(HandlerMapping으로 Controller를 검색)
    4. 해당 Controller가 요청을 처리후, home을 리턴
    5. View에 출력

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