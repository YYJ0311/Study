# XSS (cross Site Scripting)
    웹 해킹 공격 기법 중 하나로, 게시판이나 웹 메일 등에 자바스크립트 같은 스크립트 코드를 삽입해서 개발자가 고려하지 않은 기능이 작동하게 하는 치명적일 수 있는 공격.
    대부분의 웹 해킹 공격기법과는 다르게 사용 서버가 아니라 사용자를 대상으로 함.
    이미 CSS(Cascading Style Sheet)가 있어서 XSS라고 불림. Code Injection Attack 라고도 함.
    
    종류
        Reflected XSS, Stored XSS, DOM Based XSS

# Reflected XSS
    입력 폼에 <script>alert(1);</script>를 입력했을 때, 별다른 필터링 없이 실행되면 1을 내용으로 가지는 알림창이 뜨게 된다.
    공격자는 이런 취약점이 존재하는 페이지를 탐색한 후, XSS 공격을 위한 스크립트가 포함된 URL을 공격대상자에게 노출시키는 방법으로 공격할 수 있다.

    공격 순서
        1. 공격자가 미리 XSS 공격에 취약한 웹 사이트를 탐색하고, 스크립트를 포함한 URL을 사용자에게 노출시킴
        2. 사용자가 해당 URL을 클릭할 경우, 취약한 웹 사이트의 서버에 스크립트가 포함된 URL을 통해 Request를 전송 & 웹 서버에서는 해당 스크립트를 포함한 Response를 사용자에게 전송하게된다.

# Stored XSS
    웹 사이트의 게시판에 스크립트를 삽입하는 공격 방식

    공격 순서
        1. 공격자가 XSS 공격에 취약한 사이트 탐색, XSS 공격 스크립트를 포함한 게시글을 사이트에 업로드
        2. 게시글의 url을 사용자에게 노출하고, 사용자가 게시글을 확인함으로써 URL에 대한 요청을 서버에 전송
        3. 웹 서버에서 스크립트를 포함한 Response를 전송하며 공격이 수행됨

# XSS의 위험성
    1. 쿠키 정보 및 세션 ID 획득
        공격자가 페이지와 게시판에 XSS공격을 수행함으로써 해당 페이지/게시판을 이용하는 사용자의 쿠키정보나 세션 ID를 획득할 수 있다.
        쿠키는 주로 사용자의 상태를 기록하기 위해 로그인 및 버튼 클릭 등에 대한 정보를 저장한다.
        만약 세션ID 등을 쿠키에 포함하는 경우, XSS 공격을 통해서 페이지 사용자의 세션ID를 획득하여 공격자가 정상 사용자인척 할 수 있다.

    2. 시스템 관리자 권한 획득
        공격자는 웹 서버에 악성데이터를 포함시킨 후 사용자의 브라우저가 악성 데이터를 실행하게 할 수 있다.
        공격자는 이를 이용해 사용자의 시스템을 통제할 수 있다.
        만약 회사 등 조직의 개인 PC가 해킹될 경우, 조직 내부로 악성코드가 이동해서 내부의 중요 정보가 탈취될 수도 있다.

    3. 악성코드 다운로드
        악성 스크립트 자체로 악성 프로그램을 다운로드 받게 할 수는 없다.
        하지만, 사용자가 악성 스크립트가 있는 URL을 클릭하도록 유도해서 악성 프로그램을 다운받는 사이트로 리다이렉트하거나 트로이 목마 프로그램을 다운로드 하도록 유도할 수 있다.

    4. 거짓 페이지 노출
        XSS 공격에 취약한 페이지일 경우, <script> 태그 뿐만 아니라 <img>와 같은 그림을 표시하는 태그를 사용해 원래 페이지와 전혀 관련이 없는 페이지를 표시할 수 있다.
        원래 페이지의 일부를 변조하고, 이를 통해서 사용자의 개인정보 유출등의 위험이 있다.

# XSS 방지법
    XSS 공격은 IPS, IDS, 방화벽 등으로 방지할 수 없다.
    따라서 단순히 문자를 필터링하는 등의 방법만이 존재한다.

    1. script 문자 필터링
        사용자의 모든 입력값에 대하여 서버측에서 필터링 한다.
        주로 스크립트를 실행하기 위한 특수문자를 필터링 함(<, >, ", ' 등)
        PHP의 경우 eregi 함수를 이용
        
    2. htmlentities 사용(PHP)
        php는 htmlentities함수를 이용하여 모든 특수문자를 HTML entity로 변환할 수 있다.
        * HTML entity : < 를 &lt; > 를 &gt; 로 표현함