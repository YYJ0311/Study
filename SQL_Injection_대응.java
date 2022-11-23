/* 입력값 검증 */
    // 사용자 입력이 DB Query에 동적으로 영향을 주는 경우, 입력된 값이 개발자가 의도한 값인지 검증함
    // *, –, ‘, “, ?, #, (, ), ;, @, =, *, +, union, select, drop, update, from, where, join, substr, user_tables, user_table_columns, information_schema, sysobject, table_schema, declare, dual 등과 같이 의도하지 않은 입력값에 대해 검증하고 차단해야 한다
    
    // JAVA 검증
    final Pattern SpecialChars = Pattern.compile(“[‘\”\\-#()@;=*/+]”);
    UserInput = SpecialChars.matcher(UserInput).replaceAll(“”);
    final String regex = “(union|select|from|where)”;
    final Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
    final Matcher matcher = pattern.matcher(UserInput);
    if(matcher.find()){
        out.println(“<script>alert(‘No SQL-Injection’);</script>”);
    }


/* 저장 프로시저(Stored procedure), prepared Statement 사용 */
    // 저장 프로시저 : 사용하고자 하는 Query의 형식을 미리 지정하는 것
    // 지정된 형식의 데이터가 아니면 Query가 실행되지 않는다.
    
    // JAVA 취약코드
    try{
        String uId = props.getProperty(“jdbc.uId”);
        String query = “SELECT * FROM tb_user WHERE uId=” + uId;
        stmt = conn.prepareStatement(query);
        ResultSet rs = stmt.executeQuery();
        while(rs.next()){
            ...
        }
    }catch(SQLException se){
        ...    
    }finally{
        ...
    }

    // JAVA 안전한 코드
    try{
        String uId = props.getProperty(“jdbc.uId”);
        String query = “SELECT * FROM tb_user WHERE uId= ?”
        stmt = conn.prepareStatement(query);
        stmt.setString(1, uId); // 취약코드와 다른점. 위에 있는(첫번째) ?에 uId 변수 넣음
        // 내 생각으로는 위에서 쿼리를 parse하고 바인딩한 변수 uId를 읽어오는데 이미 parse가 완료되어 uId는 문법적인 의미를 가지지 않기 때문에 안전한 것 같다.
        ResultSet rs = stmt.executeQuery();
        while(rs.next()){
            ...
        }
    }catch(SQLException se){
        ...
    }finally{
        ...
    }
        /* 
        prepared statement와 바인딩 변수를 사용하면 sql injection 공격이 불가한 이유
            select문 실행 과정을 보면 DBMS 내부적으로 4가지 과정을 거쳐 결과를 출력한다
                구문분석(parse)
                    문법검사, 의미검사, 권한 검사, 실행 계획
                -> 치환(bind) 
                    값을 입력받아 변수 선언
                -> 실행(execute) 
                    디스크에서 블록을 찾아서 버퍼에 복사
                -> 인출(fetch)
                    블록에서 원하는 데이터를 추출
            
            prepared statement에서 바인딩 변수를 사용하였을 때, 쿼리의 문법 처리과정이 미리 선 수행되기 때문에 바인딩 데이터는 SQL 문법적인 의미를 가질 수 없다.
            따라서 sql 인젝션 공격으로부터 안전하다.
         */

/* 서버보안 */
    // DB 권한을 가진 유저를 최소로 운영
    // 사용하지 않는 저장프로시저와 내장함수 제거 & 권한 제어
    // 목적에 따라 Query 권한 수정
    // 공용 시스템 객체에 접근 제어
    // 신뢰할 수 있는 네트워크, 서버에 대해서만 접근 허용
    // 에러 메세지 노출 차단