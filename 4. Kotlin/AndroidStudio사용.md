# 시작
    empty activity로 프로젝트 생성
    패키지 이름 오른쪽 클릭 - new - kotlin class/file - sample1 이름의 file 생성
        ().kt 확장자의 파일이 생성됨. 여기서 코틀린 코드 작성)

# 휴대폰 화면
    확대 : ctrl + 마우스 스크롤

# 텍스트/이미지 중앙정렬
    블럭 좌우 o으로 된 것을 양 옆으로 드래그하면 가운데 정렬됨
    위치 수정 후 생기는 app:layout_constraintHorizontal_bias="0.496" 은 제거

# AVD(Android Virtual Device) 설정 & 사용
    우측상단 Device Manager 클릭 - create device - 휴대폰 선택 - 안드로이드 시스템 이미지 다운로드하고 선택 - 기본 설정 그대로 finish

    만들어진 device 옆에 play 버튼 클릭 

# LogCat
    앱의 로그 메시지를 확인할 수 있다.
    상단 View - Tool Windows - LogCat 으로 실행
    
    로그캣 화면의 상단에서 메세지를 error만 보이게 할 수도 있다.

# 깃허브 연동 & 푸쉬
    1. 깃허브에서 토큰 생성
        Settings - Developer settings - Personal access tokens - generate new token - 이름설정 & repo/admin:org/gist 정도 체크 하고 생성 - 토큰 복사
    2. 안드로이드 스튜디오에서 깃허브 계정 연결
        File - Settings... - Version Control - GitHub - Log in with token - 복사한 토근 넣고 add account하면 계정 연동됨
    3. 작업한 프로젝트 올리기
        VCS - Create Git Repository - 올릴 프로젝트 경로에 설정 - 파일들이 빨간색으로 변함(안 변하면 실행해보기) : 깃허브에 올라가지 않은 새로운 코드라서 빨갛게 표시됨
        Git - Manage Remotes... - + 버튼 눌러서 연결할 저장소 주소 입력 후 OK 눌러서 창 종료 - 상단 표시줄의 Git 옆에 체크 버튼 클릭 - 새로 뜬 창에서 commit할 것들 체크하고 커밋 메세지 입력 후 아래 버튼으로 commit - 상단 표시줄에서 push

    push 오류
        could not read Username for 'https://github.com': No such file or directory
        => File - Settings - Version Control - Git - Use credential helper 체크하기
            이렇게 하면 계정 정보가 저장된다