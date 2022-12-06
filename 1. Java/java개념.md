# JRE, JDK 차이
    JRE(Java Runtime Environment)
        : 자바 가상 머신, 자바 클래스 라이브러리, 자바 명령 및 기타 인프라를 포함한 컴파일된 Java 프로그램을 실행하는데 필요한 패키지.
    JDK(Java Development Kit)
        : Java를 사용하기 위해 필요한 모든 기능을 갖춘 Java용 SDK(Software Development Kit)이다.
        JDK는 JRE를 포함하고 있다.(JRE + 컴파일러(javac), jdb, javadoc 등)
        프로그램을 생성하고 컴파일 할 수있다.
        
    컴퓨터에서 Java 프로그래밍을 하려면 JDK를 설치해야하고, 실행하는 것은 JRE만 설치하면 된다.

# java 버전
    Java SE(Standard Edition)

    Java SE 8은 Version Number이고, 이 버전에 대한 Version String은 1.8.0(java -version)

# @Value 어노테이션
    resource에 위치한 properties 파일의 이름을 @Value("${}") 의 중괄호 안에 넣음으로써 해당 파일의 value를 가져온다.

# @Resource 어노테이션
    @Autowired 와 같은 역할
    @Autowired 이 타입을 이용해서 의존성을 주입한다면, @Resource 는 빈 이름을 이용해 의존성을 주입한다.

    사용방법 : @Resource(name ="클래스 파일 경로")

# Gson : JsonParser / JsonObject / JsonArray
    gson
        JSON의 자바 오브젝트의 직렬화, 역직렬화를 해주는 오픈 소스 자바 라이브러리
        아래 함수들을 가진다
    jsonparser
        json 포맷으로 된 데이터를 jsonParser.parse()를 이용해서 Object 타입으로 변환
    JsonObject
        객체를 (주로 String) Json 객체로 바꿔주거나 Json 객체를 새로 만들 떄 사용함
    JsonArray
        json들이 들어있는 Array

# JsonObject와 JsonArray 차이
    대략적인 표현 차이
    jsonObject1：{"UserName":"ZHULI","age":"30","workIn":"ALI"}
    jsonArray1：["ZHULI","30","ALI"]
    jsonArray의 [] 안의 요소들은 다시 json이 될 수 있음.
        jsonArray1：[{"name" : "YoungJoon", "age" : "30"}, {"familiy" : "4", "address" : "abc"}]

# JSON의 getAsString, toString 차이
    json 데이터를 parsing 할 때 getAsString은 "" 1쌍으로 감싸서 보내고, toString은 "" 2쌍으로 감싸서 보낸다.
    그래서 다른 곳에서 데이터를 호출해서 볼 때, (데이터 = 123)
        getAsString은 123
        toString은 "123"
    으로 보이게 됨

# 헷갈리는 속성
    - @RequestMapping
        value, method, produces 등의 값이 따라옴
        produces
            ex) @RequestMapping(value = "~", method = ~, produces="application/zip")
            text로 변환하는 과저에서 한글이 깨지면 인코딩 포맷도 속성으로 같이 적는다. (produces="application/text;charset=utf-8")

    - @RequestParam
        쿼리스트링 사용하기 위해 씀
    
        @RequestParam(value = "this_name", required = false) String name
            value는 쿼리스트링으로 사용하기 위해 주소에 입력하는 값. 
            여기서는 ?this_name= 으로 사용

            required는 쿼리스트링으로 받아오는 값에 null을 허용할지 결정한다.
            required = false
                name으로 받는 값에 null이 있어도 오류가 발생하지 않음
            required = true
                name에 null이 있으면 Bad Request 오류가 발생하므로 없게 만들어줘야 한다
    
    - @PathVariable
        주소에 파라미터를 직접 입력

        @PathVariable("usrKey") String usrKey
            => 사용 주소 : localhost:0000/abc/usrKey

    - @ResponseBody
    메소드에 @ResponseBody 로 어노테이션이 되어 있다면 메소드에서 리턴되는 값은 View 를 통해서 출력되지 않고 HTTP Response Body 에 직접 쓰여지게 된다.

# Integer.valueOf() 와 Integer.parseInt() 차이
    stirng을 숫자값으로 변형할 때 사용

    valueOf : Integer 래퍼(wrapper)객체를 반환
        메소드 인자로 int가 아닌 object를 요구할 때 래퍼 클래스로 감싸서 사용함
    parseInt : 원시데이터인 int 타입을 반환

# String.valueOf() 와 toString() 차이
    object의 값을 String으로 변환
    
    변경하고자 하는Object가 null인 경우, 
        toString() :  Null PointerException(NPE)을 발생
        valueOf() : "null" 문자열로 처리
    
    NPE 발생 유무가 차이점임

# 파일/폴더 확인하는 메소드 exists(), isFile(), isDirectory() 의 차이
    exists() : 지정한 경로에 디렉토리/파일 구분없이 존재하는지 확인
    isFile() : 지정한 경로에 파일이 있는지 확인
    isDirectory() : 지정한 경로에 디렉토리가 있는지 확인함

# File 클래스
    자바에서 지원하는 파일과 디렉토리(폴더)를 다루는 클래스

    File(String pathname) : 입력한 pathname(파일명 포함) 경로 파일의 객체를 생성한다.
    list() : 디렉토리나 파일을 String배열로 반환
    listFiles() : 디렉토리나 파일을 File배열로 반환
    delete() : 디렉토리나 파일을 삭제. 디렉토리를 지울 경우 디렉토리는 반드시 비워진 상태여야 한다.
    isDirectory() : 디렉토리가 맞는지 확인

# mkdir(), mkdirs() 차이
    공통점 : 둘다 자바 프로그래밍에서 파일을 저장시 디렉토리를 생성하는 함수이다.

    mkdir()은 만들고자 하는 folder의 상위 folder가 존재하지 않을 경우에 생성 불가
        C:\base\want
        want 디렉토리를 만들고자 하는데, base 디렉토리가 없는 경우, 생성 불가
    mkdirs() 만들고자 하는 folder의 상위 폴더가 존재하지 않을 경우에 상위 폴더까지 모두 생성

## ResponseEntity
    API에서 반환하는 리소스는 Value 뿐만 아니라, 상태코드, 응답 메시지 등이 포함된다.
    이 때 사용하는 것이 ResponseEntity Class.
    HTTP 요청(Request) 또는 응답(Response)에 해당하는 HttpHeader와 HttpBody 를 HttpEntity 통해서 상속받음

# BufferedReader 클래스
    버퍼를 이용해서 읽고 쓰는 함수
    버퍼를 이용하기 때문에 입출력의 효율이 매우 좋다
    
    버퍼를 거치는데 속도가 빠른 이유
        키보드나 모니터와 같은 외부 장치와의 데이터 입출력은 생각보다 시간이 걸리는 작업이다. 따라서 버퍼링 없이 키보드가 눌릴 때마다 눌린 문자의 정보를 목적지로 바로 이동시키는 것보다 중간에 메모리 버퍼를 둬서 데이터를 한데 묶어서 이동시키는 것이 보다 효율적이고 빠르다.

    BufferedReader는 Scanner로 입력받는 것과 비슷
        Scanner는 띄어쓰기(스페이스)와 엔터(개행문자)를 경계로 입력 값을 인식하기 때문에 따로 가공할 필요가 없어서 사용하기 편리함
        BufferedReader는 엔터만 경계로 인식하고 받은 데이터가 String으로 고정되기 때문에 추가 가공이 필요한 경우가 많다. 하지만 Scanner보다 빠르다.

# java 입출력 (inputStream, OutputStream)
    INPUT
        InputSream 클래스
            바이트 단위로 데이터를 읽어들이는 모든 입력 스트림이 상속하는 최상위 클래스

            대표적인 메소드
                read() : public abstract int read() throw IOException
                close() : public void close() throw IOException

            read()는 abstract로 선언되어서 InputStream을 상속하는 다른 클래스(FileInputStream이 아닌) 에서도 read 메소드를 사용할 수 있다.
                InputStream in = new FileInputStream("input.exe");
                int bData = in.read();
                bData는 더 이상 읽어올 데이터가 없을 경우 -1을 반환한다.

        FileInputStream 클래스
            파일에서 바이트 단위로 입력할 수 있도록 하기 위해 사용
            FileInputStream(File file) : 주어진 File 객체가 가리키는 파일을 바이트 스트림으로 읽기 위한 FileInputStream 객체를 생성
            FileInputStream(String name) : 주어진 이름이 가리키는 파일을 바이트 스트림으로 읽기 위한 FileInputStream 객체를 생성

            read 메소드
                read(byte[] b) : byte array 타입 변수의 길이를 읽는다. while문에서 반복 횟수 정할 때 사용.
                    만약 byte array를 다 읽으면 -1을 반환한다.
                    
                    int len;
                    in은 FileInputStream 타입의 변수 

                    while ((len = in.read(buf)) > 0){ ... } 처럼 사용함

        InputStreamReader 클래스
            바이트 단위로 읽어 들이는 형식을 문자단위의 데이터로 변환시키는 중개자 역할
            (바이트 데이터 -> 문자 변환은 Charset 클래스에서 담당)
    
    OUTPUT
        OutputStream 클래스
            바이트 단위로 출력하는 스트림의 최상위 클래스

        FileOutputStream
            File 또는 FileDescriptor에 데이터를 쓰기 위한 출력 스트림
            이미지 데이터와 같은 raw bytes를 쓸 수 있다
            문자(characters) 스트림을 적기 위해서는 FileWriter를 써야한다

# IOUtils
    IO(입출력, In Out) 스트림 조작 유틸리티

    Apache Commons IO dependency 주입 필요
        <dependency>
            <groupId>commons-io</groupId>
            <artifactId>commons-io</artifactId>
            <version>2.0.1</version>
        </dependency>

    메소드
        closeQuietly - 이 메서드는 null 및 예외를 무시하고 스트림을 닫습니다.
        toXxx/read - 이 메서드는 스트림에서 데이터를 읽습니다.
        write - 이 메서드는 스트림에 데이터를 씁니다.
        copy - 이 메소드는 한 스트림에서 다른 스트림으로 모든 데이터를 복사합니다.
        contentEquals - 이 메서드는 두 스트림의 내용을 비교합니다.
        toByteArray - 바이트로 된 inputstream의 내용을 가져옴

# spring 파일 다운로드 구현
    headers.setContentType(MediaType.APPLICATION_OCTET_STREAM)
    MediaType.APPLICATION_OCTET_STREAM
        표준으로 정의되어 있지 않은 파일인 경우에 지정하는 타입
        octet stream이 8비트로 된 데이터이므로 순수한 바이너리 데이터로 받아온다는 의미

# URLEncoder / URLDecoder 클래스
    URL 관련하여 인코딩이 필요한 경우 사용
    URL 규칙에 사용되는 문자들이 정해져있고, 특정한 값들은 규칙에 맞게 변환되어야 함
    또 쿠키와 같이 한글을 표현하지 못하는 경우 한글을 ASCII 값으로 인코딩해주어야 함
        => 이런 경우 URLEncoder와 URLDecoder 를 사용한다
    
    url = URLEncoder.encode("한글 인코딩 이라네~", "UTF-8");
    url = URLDecoder.decode("%ED%95%9C%EA%B8%80+%EC%9D%B8%EC%BD%94%EB%94%A9+%EC%9D%B4%EB%9D%BC%EB%84%A4%7E", "UTF-8");
        둘은 같은 값

# 0과 0L의 차이
    L : long
    0L : long형 0
    long형 변수와 값을 비교할 땐 0보다 0L이라고 사용한다.

    int
        32비트(4바이트)
        범위 : -2,147,483,648 ~ 2,147,483,647
        저장하는데 필요한 메모리가 long보다 적음
    long
        64비트(8바이트)
        범위 : -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807

# UUID
    범용 고유 식별자(Universally Unique Identifiers)
    각 개체를 고유하게 식별 가능한 값
    규칙에 따라 식별자를 만들어서 중복이 날 확률을 매우 많이 낮춘다

    UUID test = UUID.randomUUID() 로 랜덤하게 UUID값을 받아온 뒤 내가 중복을 피하고자 하는 변수에 붙여서 사용하면 됨

# 스프링 Component-scan
    개념
        빈으로 등록 될 준비를 마친 클래스들(@Controller, @Service, @Component, @Repository)을 스캔하여, 빈으로 등록해주는 것
    사용 방법
        1. xml 파일에 설정
            <context:component-scan base-package="com.rcod.lifelog"/>

            base package를 적어주면 그걸 기준으로 클래스들을 스캔하여 빈으로 등록한다.
            base package에는 여러개의 패키지를 쓸 수 있다.
            base package 하위의 @Controller, @Service, @Repository, @Component 클래스가 모두 빈으로 등록되므로 특정한 객체만 빈으로 등록하여 사용하고 싶다면 include-filter나 exclude-filter를 통해 설정할 수 있다.

        2. 자바 파일 안에서 설정
            @Configuration
            @ComponentScan(basePackages = "com.rcod.lifelog")
            public class ApplicationConfig { }

            @Configuration 은 이 클래스가 xml을 대체하는 설정 파일임을 알려준다. 해당 클래스를 설정 파일로 설정하고 @ComponentScan을 통하여 basePackages를 설정해준다.

        만약 Component-scan을 사용하지 않으면, 빈으로 설정할 클래스들을 xml 파일에 일일이 등록해주어야 한다.
        <bean id="mssqlDAO" class="com.test.spr.MssqlDAO"></bean>
        <!-- MemberList 객체에 대한 정보 전달 및 의존성 주입 -->
        <bean id="member" class="com.test.spr.MemberList">
            <!-- 속성의 이름을 지정하여 주입 -->
            <property name="dao">
                <ref bean="mssqlDAO"/>
            </property>
        </bean>

        => MssqlDAO 와 MemberList를 빈으로 등록하고, MemberList에 Mssql을 주입한 것

    동작 과정
        ConfigurationClassParser 가 Configuration 클래스를 파싱한다.
        @Configuration 어노테이션 클래스를 파싱하는 것이다.
                        ⬇
        ComponentScan 설정을 파싱한다.
        base-package 에 설정한 패키지를 기준으로
        ComponentScanAnnotationParser가 스캔하기 위한 설정을 파싱한다.
                        ⬇
        base-package 설정을 바탕으로 모든 클래스를 로딩한다.
                        ⬇
        ClassLoader가 로딩한 클래스들을 BeanDefinition으로 정의한다.
        생성할 빈의 대한 정의를 하는 것이다.
                        ⬇
        생성할 빈에 대한 정의를 토대로 빈을 생성한다.
    
    참고 : https://velog.io/@hyun-jii/%EC%8A%A4%ED%94%84%EB%A7%81-component-scan-%EA%B0%9C%EB%85%90-%EB%B0%8F-%EB%8F%99%EC%9E%91-%EA%B3%BC%EC%A0%95

# @ComponentScan 과 @Autowired 동작원리의 차이
    @ComponentScan은 BeanFactoryPostProcessor를 구현한 ConfigurationClassPostProcessor에 의해 동작한다.
    BeanFactoryPostProcessor는 다른 Bean들을 등록하기 전에 컴포넌트 스캔을해서 Bean으로 등록해준다.

    @Autowired는 BeanPostProcessor라는 라이프 사이클 인터페이스의 구현체인 AutowiredAnnotationBeanPostProcessor에 의해 의존성 주입이 이루어진다.
    BeanPostProcessor는 초기화 라이프 사이클 이전과 이후에 필요한 부가 작업을 할 수 있는 라이프 사이클 콜백이다. 즉, bean이 만들어지는 시점 이전 혹은 이후에 추가적인 작업을 하고 싶을 때 사용된다.
    AutowiredAnnotationBeanPostProcessor가 bean 초기화 라이프 사이클 이전(bean 인스턴스 생성 이전)에 @Autowired가 붙어 있는 bean을 찾아 주입해주는 작업을 한다.

    참고 : https://jjingho.tistory.com/6


# Map <-> JSON 변환 메소드
    - writeValueAsString(value)
        value : String 타입으로 변환할 대상

    - readValue(arg, type)
        arg : 지정된 타입으로 변환할 대상
        type : 변환할 타입을 명시함(Class, TypeReference 객체도 가능)

        JSON 파일을 Java 객체로 deserialization(역직렬화) 하기 위해 사용
            serialization : 객체의 인스턴스를 Byte Code로 저장하는 작업
            deserialization : 저장된 Byte Code로부터 객체를 불러오는 작업
    
    - 사용 예시
        writeValueAsString()

            ObjectMapper mapper = new ObjectMapper();
            HashMap<String, String> map = new HashMap<String, String>();
            map.put("name", "steave");
            map.put("age", "32");
            map.put("job", "baker");

            System.out.println(map); // {age=32, name=steave, job=baker}
            System.out.println(mapper.writeValueAsString(map)); // {"age":"32","name":"steave","job":"baker"}

            : map 타입이 JSON 형태의 String 타입으로 변환됨
            자바스크립트에 JSON을 넘겨줄 때 사용한다
        
        readValue()
            
            ObjectMapper mapper = new ObjectMapper();
            HashMap<String, String> map = new HashMap<String, String>();
            String jsn = "{\"age\":\"32\",\"name\":\"steave\",\"job\":\"baker\"}";
            map = mapper.readValue(jsn, new TypeReference<HashMap<String, String>>() {});        

            System.out.println(map); // {name=steave, age=32, job=baker}

            : 위와 반대로 JSON을 Map 타입으로 변환

# access토큰을 .으로 나누기 위해 사용한 방법
    accessToken.split("\\.")
    
    이유) split의 인자로 들어가는 String 토큰이 regex 정규식이기 때문
        .은 정규식에서 무작위의 한 글자를 의미
        따라서 이스케이프 문자를 앞에 붙여 줘야 하는데, String 안에 이스케이프 문자인 \를 쓰려면 \\라고 써야 한다.

# uri 와 url 차이
    uri
        특정 리소스를 식별하는 통합 자원 식별자(Uniform Resource Identifier)
        웹 기술에서 사용하는 논리적 또는 물리적 리소스를 식별하는 고유한 문자열 시퀀스

    url
        웹 주소
        컴퓨터 네트워크 상에서 리소스가 어디 있는지 알려주기 위한 규약
        URI의 서브셋
    
    가장 큰 차이점
        URI는 식별하고, URL은 위치를 가르킨다.
    
    예시
        "영준" 은 내 이름이며 식별자(Identifier)다. 이는 URI라고 생각할 수 있지만 내 위치나 연락처에 대한 정보가 없으므로 URL은 될 수 없다.

        https://www.naver.com/index.html
            => 웹서버의 실제 파일 위치를 나타내는 주소이므로 URI이면서 URL이다.
        https://www.naver.com/index
            => "index라는 파일이 웹서버에 존재하지 않으므로" URL은 아니다. 하지만 서버 내부에서 이를 처리하여 결국 index.html을 가리키기 때문에 URI라고 볼 수 있다.

# Connection 인터페이스
    특정 데이터베이스와의 연결(세션)이 필요할 때 사용함
    SQL 문이 실행되고 연결 컨텍스트 내에서 결과가 반환됨

    연결 개체의 데이터베이스는 테이블, 지원되는 SQL 문법, 저장 프로시저, 연결 기능 등을 설명하는 정보를 제공하고, 이 정보는 getMetaData 메소드로 얻을 수 있다.

# Statement 인터페이스
    Connection이 자바 프로그램과 DB 사이에 연결되었다면 이 연결을 통해 자바프로그램은 DB에 SQL문을 전송하고, DB는 처리된 결과를 다시 자바프로그램 쪽으로 전달해야 하는데 이 역할을 statement가 함
    즉, Statement는 SQL문을 실행하고 생성된 결과를 반환시키는데 사용됨

    Statement의 메소드
        setQueryTimeout
            statement 객체가 실행될 때까지 드라이버가 기다릴 대기시간 설정

        executeUpdate
            select 구문을 제외하고 INSERT/UPDATE/DELETE와 같이 반환되는 것이 없는 SQL문을 수행할 때 사용
            
            수행 결과로 Int 타입의 값을 반환(CREATE/DROP은 -1 반환)

# BufferedReader 클래스
    문자 입력 스트림에서 텍스트를 읽고 문자, 배열 및 행을 효율적으로 읽을 수 있도록 문자를 버퍼링함

    버퍼 크기를 지정하거나 기본 크기를 사용할 수 있음 
    기본값은 대부분의 목적에 충분히 크다
    
    BufferedReader 메소드
        기본 크기의 입력 버퍼를 사용하는 버퍼링 문자 입력 스트림을 만듦

# @Transactional
    transaction 의 개념
        모든 작업들이 성공적으로 완료되어야 작업들의 결과를 적용하고, 만약 어떤 하나의 작업에서 오류가 발생했을 때는 이전에 있던 모든 작업들이 성공적이었더라도 없었던 일처럼 완전히 되돌리는 것
    
    사용
        데이터베이스를 다룰 때 트랜잭션을 적용하면 데이터 추가, 갱신, 삭제 등으로 이루어진 작업을 처리하던 중 오류가 발생했을 때 모든 작업들을 원상태로 되돌릴 수 있다. 모든 작업들이 성공해야만 최종적으로 데이터베이스에 반영하도록 한다.

        클래스/메소드에 @Transactional 어노테이션을 달아서 사용함

        @Transactional이 붙은 메서드는 메서드가 포함하고 있는 작업 중에 하나라도 실패할 경우 전체 작업을 취소한다.

    옵션
        rollbackFor
            @Transactional(rollbackFor = {Exception.class})
                에러가 발생하면 이전 초기상태로 롤백

            @Transactional(rollbackFor = {NullPointerException.class})
                NullPointerException 에러만 롤백

    주의사항
        insert 작업시 id를 auto increment로 했을 때, 롤백되어도 증가한 id는 다시 감소하지 않는다. auto increment는 transaction 범위 밖에서 동작하기 때문.

# @Repository와 @Service
    @Controller와 같이 해당 클래스를 컨테이너에 빈(Bean) 객체로 생성해주는 어노테이션
    둘 다 기능이 같아서 어떤 걸 써도 상관이 없지만, 명시적으로 구분해주기 위해 분리해서 사용한다.
    부모 어노테이션인 @Component를 써도 똑같이 루트 컨테이너에 생성되지만 가시성이 떨어져서 잘 사용하지 않음

    루트 컨테이너 또는 서블릿용 컨테이너를 생성할 때 어노테이션을 검색하기 때문에, 컨테이너 생성 시 참조하는 xml 파일에 다음의 어노테이션 스캔 설정이 존재해야 한다.
    <context:component-scan base-package="패지지 경로" />

# Hashcode
    Hashcode는 객체를 식별하는 Integer 값
    객체가 갖고 있는 데이터를 알고리즘에 적용하여 계산된 정수 값

    한 객체에 대해 hashCode() 메소드를 호출하면 객체에 대한 해쉬코드를 얻을 수 있다.

    Hashcode를 사용하는 이유
        객체를 비교할 때 드는 비용을 낮추기 위함

        자바에서 2개의 객체가 같은지 비교할 때 사용하는 equals()는 여러 객체를 비교할 때 Integer를 비교하는 것에 비해 많은 시간이 소요된다. 따라서 hashcode를 이용하여 비교하면 equals()를 이용하는 것보다 시간이 단축된다.

# BigInteger
    int : -2^31 ~ (2^31 - 1) = -2,147,483,648 ~ 2,147,483,647
    long : -2^63 ~ (2^63 - 1) = -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807

    long 범위를 넘어서는 값을 다룰 때 BigInteger를 사용한다.

    BigInteger는 내장 Class가 아니고 math package에 포함되어 있기 때문에 import가 필요함
    BigInteger 사칙연산은 int형과는 다르다
        나눗셈(divide)
        BigInteger totalMinute = (BigInteger) data.get("totalDrivingTime");
        BigInteger minute = new BigInteger("60");
        => totalMinute.divide(minute)

# Class.forName()
    컴파일 타임에 직접적인 참조 없이 런타임에 동적으로 클래스를 로드하기 위함
    Class.forName()를 이용하여 필요한 데이터베이스의 드라이버를 로드한다.
    사용을 위해서 dependency(sqlite-jdbc) 추가가 필요하다.

    사용 예 
        Class.forName ("org.sqlite.JDBC");
        Class.forName("oracle.jdbc.driver.OracleDriver");

    JDBC를 이용하여 SQLite를 사용하기 위한 방법
        1. Class.forName("org.sqlite.JDBC");
        2. connection = DriverManager.getConnection(jdbc:sqlite:file:~)
        3. Statement statement = connection.createStatement();
        4. statement.executeUpdate("sql 문")

        JDBC 4.0 이후로는 Class.forName() 메소드를 호출하지 않아도 자동으로 드라이버를 초기화한다.

# sqlcipher
    SQLite는 기본적으로 데이터베이스 파일 암호화를 지원하지 않음
    데이터 암호화를 하기 위해 SEE, SQLCipher, SQLiteCrypt, wxSQLite3 같은 수정된 버전의 SQLite를 사용해야 한다.

# Enum 클래스
    JDK 1.5부터는 C언어의 열거체보다 더욱 향상된 성능의 열거체를 정의한 Enum 클래스를 사용할 수 있다.

    자바 열거체의 장점
        1. 열거체를 비교할 때 실제 값뿐만 아니라 타입까지도 체크
        2. 열거체의 상수값이 재정의되더라도 다시 컴파일 할 필요가 없음

    enum 정의 및 사용
        문법 ) enum 열거체이름 { 상수1이름, 상수2이름, ... }
        예제 ) enum Rainbow { RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET }
        사용 ) 열거체이름.상수이름 => Rainbow.RED
    
    열거체의 상수값 정의
        첫 번째 상수값은 0부터 설정되며, 그다음은 바로 앞의 상수값보다 1만큼 증가되며 설정됨
        불규칙한 값을 상수값으로 설정하고 싶으면 상수의 이름 옆에 괄호()을 추가하고 상수값을 명시해서 사용 가능. 하지만 특정 값을 저장할 수 있는 인스턴스 변수와 생성자를 추가해야 함.

        예제
        enum Rainbow {
            RED(3), ORANGE(10), YELLOW(21), GREEN(5), BLUE(1), INDIGO(-1), VIOLET(-11);
            private final int value;
            Rainbow(int value) { this.value = value; }
            public int getValue() { return value; }
        }
    
    메소드
        enum Rainbow { RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET }

        values() : 해당 열거체의 모든 상수를 저장한 배열을 생성하여 반환
            예제        
                public class Enum01 {
                    public static void main(String[] args) {
                        Rainbow[] arr = Rainbow.values();
                        for (Rainbow rb : arr) {
                            System.out.println(rb); // RED, ORANGE, YELLOW, ...
                        }
                    }
                }

        valueOf() : 전달된 문자열과 일치하는 해당 열거체의 상수
            예제
                public class Enum02 {
                    public static void main(String[] args) {
                        Rainbow rb = Rainbow.valueOf("GREEN");
                        System.out.println(rb); // GREEN
                    }
                }
        
        ordinal() : 해당 열거체 상수가 열거체 정의에서 정의된 순서(0부터 시작)를 반환함
            반환되는 값은 열거체 정의에서 해당 열거체 상수가 정의된 순서이며, 상숫값 자체가 아님
            예제
                public class Enum03 {
                    public static void main(String[] args) {
                        int idx = Rainbow.YELLOW.ordinal();
                        System.out.println(idx); // 2
                    }
                }

            불규칙적인 상수값을 가지는 열거체에서의 예제
            enum Rainbow {
                RED(3), ORANGE(10), YELLOW(21), GREEN(5), BLUE(1), INDIGO(-1), VIOLET(-11);
                private final int value;
                Rainbow(int value) { this.value = value; }
                public int getValue() { return value; }
            }
            public class Enum04 {
                public static void main(String[] args) {
                    System.out.println(Rainbow.YELLOW.ordinal()); // 21이 아닌 기존 자리수에 해당하는 2 가 반환됨
                }
            }

# AWT(Abstract Window Toolkit)
    GUI프로그래밍(윈도우 프로그래밍)을 위한 도구
    Java로 구현하지 않고 OS의 컴포넌트를 그대로 사용

    * Swing
        AWT를 확장한 GUI프로그래밍 도구
        AWT보다 더 많은 종류의 컴포넌트 제공
        OS의 컴포넌트를 사용하지 않고 J~로 구현
    
    awt의 Desktop 클래스를 이용하여 윈도우에서 파일 실행이 가능함

# java 1.6에서 ArrayList<>()
    1.8에서 타입을 생략해서 쓰던 ArrayList<>()을 1.6에선 사용할 수 없다.
    <> 안에 타입을 꼭 지정해줘야 한다.

