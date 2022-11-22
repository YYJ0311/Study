/* 
하드코딩?
    어떤 데이터가 코드 내에 그대로 입력된 것
    입력받아야 할 정보를 소스코드 내에 바로 입력하거나 중요 정보를 주석 처리하는 것 또한 하드코딩
*/

/* 
CASE
    DB 연결을 위한 패스워드를 소스코드 내부에 상수 형태로 하드코딩하는 경우, 
    리버스 엔지니어링으로 비밀번호와 같은 접속정보가 그대로 노출될 수 있어 위험하다.
*/

// 안전하지 않은 코드
public class MemberDAO {
    private static final String DRIVER = "oracle.jdbc.driver.OracleDriver";
    private static final String URL = "jdbc:oracle:thin:@192.168.0.3:1521:ORCL";
    private static final String USER = "SCOTT"; // DB ID;
    private static final String PASS = "SCOTT"; // DB PW;
    // 이런식의 하드코딩이 위험

    Member_List mList
    public MemberDAO() { }
    public MemberDAO(Member_List mList) {
        this.mList = mList
    }
    public Connection getConn() {
        Connection con = null;
        try {
            Class.forName(DRIVER);
            con = DriverManager.getConnection(URL, USER, PASS);
        } catch (Exception e) {
            log.error(e.getMessage());
        }
        return con;
    }
}

// 안전한 코드
    /* 
    암호는 암호화하여 별도의 분리된 공간(파일)에 저장하고, 
    암호화된 패스워드를 사용하기 위해서는 복호화 과정을 거치도록 만듦
    */
public class MemberDAO {
    private static final String DRIVER = "oracle.jdbc.driver.OracleDriver";
    private static final String URL = "jdbc:oracle:thin:@192.168.0.3:1521:ORCL";
    private static final String USER = "SCOTT"; // DB ID

    Member_List mList;

    public Connection getConn() {
        Connection con = null;
        try {
            Class.forName(DRIVER);
            // 암호화된 비밀번호를 복호화해서 가져옴
            String PASS = props.getProperty("EncryptedPswd");
            byte[] decryptedPswd = cipher.doFinal(PASS.getBytes());
            PASS = new String(decryptedPswd);

            con = DriverManager.getConnection(URL, USER, PASS);
        } catch (Exception e) {
            log.error(e.getMessage());
        }
        return con;
    }
}

/* 안전한 암호 사용 방법 */
    // - 암호를 중앙 관리해주는 Valut 서비스

    /*
    1. 메인 소스와 설정 파일 분리
        가장 간단한 방법으로, 메인 소스와 비밀번호가 담긴 설정 파일을 분리하고
        Git과 같은 SCM 툴에 올릴 때 설정파일은 올리지 않고 별도로 관리하는 방법이다.

        단점
            - 개발 담당자가 직접 설정 파일을 로컬에서 관리해줘야 함
            - 개발 담당자가 배포 과정에 직접 개입해야 함
            - 배포 자동화를 위해서는 결국 설정 파일이 어딘가에 노출된 채로 있어야 함
    
    2. 설정 파일을 S3에 업로드
        AWS의 IAM 권한을 이용
        S3에 설정 파일을 업로드하고 버킷 정책을 통해서 특정 IAM 권한 외에는 접근을 차단

        단점
            - 개발 담당자가 설정파일을 S3에서 관리해야 함
            - 버킷 정책을 효과적으로 통제하기 어려움
            - 정책을 직접 수정할 수 있는 권한을 가진 사람이 많음

    3. 환경 변수로 민감한 데이터 제공
        AWS Lambda 사용과 연계
        Lambda에서는 KMS를 이용하여 환경 변수를 암호화된 상태로 제공할 수 있음
        
        단점
            - 복호화 로직을 넣어야 하는데 코드가 길어져서 비효율적
            - 환경 변수의 관리가 제대로 이루어지지 않음
            - IaC로 넘어가면서 환경변수도 코드로 제공되면서 무의미해짐
    
    4. IAM 기반의 권한 관리 - Parameter Store
        AWS에서 각종 매개 변수를 한 곳에서 모아서 관리하는 것을 가능하게 해주는 Systems Manager의 Parameter Store를 이용
        민감한 정보에 대해서 KMS의 키를 이용해서 암호화를 해놓을 수 있다
        
        SecureString에 대한 접근 권한을 2단계로 관리 가능
            매개변수 자체에 대한 읽기 권한과 KMS키를 이용한 복호화 권한이 모두 있어야만 실제 값을 알 수 있음

    5. Secrets Manager
        암호 관리에 최적화된 서비스
        AWS의 RDS 등에 대한 호스트, DB, 사용자 계정 등에 대한 정보를 하나로 묶어서 관리하는데 이것들을 모두 암호화 시켜 놓음
        Parameter Store에선 변수 여러개로 관리하던 것을 한번에 관리할 수 있음
        일정 기간을 주기로 암호를 자동으로 변경할 수 있음

        단점
            Parameter Store 보다 비쌈
    */
