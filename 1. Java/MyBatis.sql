-- useGeneratedKeys와 keyProperty

    <insert id="insert" parameterType="파라미터 타입" useGeneratedKeys="true" keyProperty="id">

    -- getGeneratedKeys
        -- JDBC의 메소드로 자동 생성된 키값들을 가져오는 속성을 설정한다.
        -- true : 자동 생성된 키 가져옴

    -- keyProperty
        -- 리턴 될 key 설정
        -- 리턴 된 키 값들을 어느 필드에 set 할 건지를 정한다. id를 적으면 id값을 받아온다.
        
    -- 테이블에서 id컬럼이 auto_increment인 상황
        -- name과 password를 받아서 db에 insert 하는 경우, id는 입력하지 않아도 자동으로 1씩 증가하며 저장된다.
        -- insert를 성공하면 추가된 id, name, password를 리턴하게끔 하면 id는 null로 나온다.
        -- 이 때, useGeneratedKeys와 keyProperty를 이용하면 id도 null값 대신 실제 증가된 값이 출력되게 만들 수 있다.

-- selectKey
    https://sowon-dev.github.io/2021/07/26/210727MyBatis-keyProperty/