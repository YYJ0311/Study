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
    또는 applicationContext.xml
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

# MockMvc
    MockMvc는 웹 어플리케이션을 어플리케이션 서버에 배포하지 않고 테스트용 MVC환경을 만들어 요청 및 전송, 응답기능을 제공해주는 유틸리티 클래스이다.
    즉, 내가 컨트롤러를 테스트하고 싶을 때, 실제 서버에 올리지 않고 테스트용으로 시뮬레이션하여 MVC가 되도록 도와주는 클래스이다.

# spring 버전 변경하기
    pom.xml의 <org.springframework-version> 항목에서 버전을 직접 바꾸면 된다.
        <org.springframework-version>3.1.1.RELEASE</org.springframework-version>
        ==> <org.springframework-version>4.3.6.RELEASE</org.springframework-version>
    
    Maven Dependencies 라이브러리를 확인하면 입력한 버전으로 업데이트 된 걸 볼 수 있다.

    * 스프링 버전 별 지원하는 jdk 버전이 정해져 있음
    * 저장 후 maven - update project 하기

# MVC 프로젝트 실행순서
    요청 -> DispatcherServlet -> HandlerMapping -> 요청 처리하기 (Controller <-> Service <-> DAO <-> DB) -> DispatcherServlet -> ViewResolver -> View -> DispatcherServlet -> 응답
    
    1. 요청
        Client가 url로 접근하여 정보 요청
    2. DispatcherServlet 
        web.xml에 포함되어 출력 역할을 하는 클래스
        Springframework에서 기본 제공
    3. HandlerMapping
        servlet 설정파일에 포함
        Springframework에서 기본 제공
        @RequestMapping 제공
    4. Controller <-> Service <-> DAO <-> DB
        controller로 처리 요청을 보냄
        Bean 등록

        db에서 다시 거꾸로 controller로 돌아오게 됨
        클라이언트의 요청을 처리하고 결과를 출력할 View의 이름을 return함
    5. DispatcherServlet
        컨트롤러에서 보내온 View 이름을 토대로 처리 View를 검색
    6. ViewResolver
        web.xml에 포함
        Springframework에서 기본 제공
        p:prefix="/WEB-INF/jsp/" p:suffix=".jsp"

        처리결과를 View에 송신
    7. View
        처리결과가 포함된 View를 DispatcherServlet로 송신
    8. DispatcherServlet
        최종결과 출력

# DAO (Data Access Object)
    DB의 data에 접근하기 위한 객체
    DB에 접근하기 위한 로직과 비즈니스 로직을 분리하기 위해 사용

    service에서 이어지는 mapper와 비슷한 개념인듯
    db 쿼리 결과를 받아서 service로 결과를 넘겨준다

# JPA) @Commit과 @Transactional
    @Transactional
        JPA에서 update나 delete를 사용할 때 꼭 필요한 어노테이션
        
        해당 어노테이션을 붙여서 테스트(@Test가 붙은) 메소드가 종료될 때 메소드 내부에서 생성했던 데이터를 롤백시킬 수 있다.

    @Commit
        해당 어노테이션을 추가한 후 테스트를 실행하면 DB에서 변경했던 데이터들이 롤백되지 않고 그대로 남아있다.

# Lombok 어노테이션
    @Getter/@Setter
        aaa라는 필드에 선언하면 getAaa() ( boolean인 경우, isAaa() ) 와 setAaa() 메소드를 생성해준다.

    @Constructor 시리즈
        생성자를 자동으로 생성해준다.

        public class User {
            private Long id;
            @NonNull
            private String username;
            @NonNull
            private String password;
            private int[] scores;
        }
        위 클래스에 대해서 다음의 어노테이션을 붙이면,
            @NoArgsConstructor
                파라미터가 없는 기본 생성자 생성
                User user1 = new User();

            @RequiredArgsConstructor
                final이나 @NonNull인 필드 값만 파라미터로 받는 생성자를 생성
                User user2 = new User("dale", "1234");

            @AllArgsConstructor
                모든 필드값을 파라미터로 받는 생성자를 생성
                User user3 = new User(1L, "dale", "1234", null);

    @ToString
        toString()을 자동으로 생성해준다.
        이걸 사용 안 해서 결과물을 출력할 때 필요한 문자대신 @a1s2d3 같은 표현으로 출력되었다.
        결과물의 타입으로 설정한 클래스에 @ToString을 붙여줌으로써 원하는 문자를 얻을 수 있었다!
        exclude를 사용해서 원하는 결과에서 제외시킬 수도 있다.

        @ToString(exclude = "password")
        public class User {
        private Long id;
        private String username;
        private String password;
        private int[] scores;
        }

        어노테이션을 붙인 위 클래스에 다음과 같이 setting
        User user = new User();
        user.setId(1L);
        user.setUsername("dale");
        user.setUsername("1234");
        user.setScores(new int[]{80, 70, 100});
        
        그리고 출력하면
        System.out.println(user);
        => User(id=1, username=1234, scores=[80, 70, 100])

    @EqualsAndHashCode
        equals와 hashCode 메소드를 자동으로 생성해준다
        callSuper 속성을 통해서 부모 클래스의 필드까지 감안할지 안 할지에 대해 설정할 수 있다
            callSuper = true로 설정하면 부모 클래스 필드 값들도 동일한지 체크하고, callSuper = false로 설정하면(기본값) 자신 클래스의 필드 값들만 고려한다.

            public class User {
            private Integer Id;
            }

            @EqualsAndHashCode(callSuper = true/false)
            public class Member extends User{
            private String name;
            private String email;
            }

            위 클래스에 대해서 member1과 member2를 만들어서 equals()로 비교

            Member member1 = new Member();
            member1.setId(1);
            member1.setName("A");
            member1.setEmail("A@naver.com");

            Member member2 = new Member();
            member2.setId(2);
            member2.setName("A");
            member2.setEmail("A@naver.com");

            member1.equals(member2);
            => Member 클래스에 선언했던 어노테이션의 속성이 true이면, 
                부모 클래스인 User의 필드 Id까지 확인하게 되므로 Id 값이 1과 2로 서로 달라서 false 반환됨
            속성이 false 이면,
                User의 필드를 제외한 Member의 필드만으로 비교하기 때문에 Name과 Email이 같아서 true 반환됨
                
    @Data
        위 어노테이션들을 모두 설정해줌

# @Qualifier
    bean을 설정할 때 <context:annotation-config/> 를 사용함으로써 굳이 bean 태그 안에 <constructor-arg>나 <property>태그를 추가하지 않아도 스프링의 @Autowired 어노테이션이 적용된 생성자, 필드, 메소드에 대해 의존 자동 주입을 처리한다.

    이 때 만약 동일한 타입을 가진 bean 객체가 두개가 있다면?
        스프링이 어떤 빈을 주입해야 할 지 알 수 없어서 스프링 컨테이너를 초기화하는 과정에서 Exception을 발생시킨다.
    
    이런 문제를 해결하기 위해 @Qualifier 어노테이션을 이용하여 사용할 의존 객체를 선택할 수 있도록 할 수 있다.
        설정에서 bean의 한정자 값을 설정. 아래에선 m1과 m2가 해당됨.
            <context:annotation-config>
                <bean id="member1" class="example.Member">
                    <qualifier value="m1"/>
                </bean>

                <bean id="member2" class="example.Member"/>
                    <qualifier value="m2"/>
                </bean>
            <context:annotation-config/>

        @Autowired 어노테이션이 적용된 주입 대상에 @Qualifier 어노테이션과 한정자를 설정
            pubic class MemberDao{  
                @Autowired  @Qualifier("m1")
                private Member member;       

                public void setMember(Member member){      
                    this.member = member;  
                }
            }

# 프로젝트 JDK 버전 변경
    방법 1) 상단 Window - Preferences - Java > Installed JREs - Add - Standard VM - 추가할 JDK 경로 설정후 finish

    방법 2) 프로젝트 우클릭 - properties - java build path - add library - execution environment에서 버전을 변경

# project faucet
    개발환경에 맞춤 세팅, 자동 완성, 빈 지원(XML, config 등)의 도우미 역할을 하는 기능

# JPA) @Entity 와 @Table
    @Entity
        JPA로 테이블과 매핑할 클래스에 붙임으로써 JPA가 관리하도록 함
        기본 생성자 필수
        final, enum, interface, inner 클래스에는 사용 불가

    @Table
        엔티티와 매핑할 테이블 지정
        클래스 이름과 테이블 이름이 다를 경우 JPA에게 테이블의 이름을 알려주는 역할

# JPA) hibernate
    JPA의 구현체로, JPA 인터페이스를 구현하고 내부적으로 JDBC API를 사용하는 자바 언어를 위한 ORM 프레임워크

    MyBatis와 같은 역할

    장점
        - SQL을 직접 사용하지 않고 메소드 호출만으로 쿼리가 수행되기 때문에 SQL 반복 작업을 하지 않아서 생산성이 높음
        - 테이블 컬럼이 변경되었을 때 테이블과 관련된 DAO 파라미터, 결과, SQL등을 대신 수행해줌으로써 유지보수가 수월
