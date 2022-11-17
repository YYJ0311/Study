// csv 파일 기반 sqlite db 생성
    Connection connection = null;
    String filesname = 경로1 + 경로2 + "db명.db"; // 저장할db명(경로)

    Class.forName ("org.sqlite.JDBC");
    connection = DriverManager.getConnection("jdbc:sqlite:file:"+ filesname + 비밀번호 등의 db 정보);

    Statement statement = connection.createStatement(); // sql문을 실행할 Statement 생성
    statement.setQueryTimeout(5);
    statement.executeUpdate("drop table if exists 테이블명");
    statement.executeUpdate("문자와 + 로 이어진 테이블 생성을 위한 create문");

    BufferedReader 읽을변수이름 = new BufferedReader(new InputStreamReader(new FileInputStream(csv파일의 경로),"UTF-8"));

    String line;
    while ( (line = 읽을변수이름.readLine()) != null)
    {
        line = line.replace("\'", "`"); // ' -> `
        String[] values = line.split("\t"); // \t : tab으로 구문을 나눔

        statement.executeUpdate("values를 활용한 INSERT 문"); // 테이블에 데이터 넣음
    }
    읽을변수이름.close(); // 버퍼리더 종료

    if(connection != null) connection.close(); // 작업 다 했는데도 연결이 되어있으면 강제 종료
    // 처음에 지정한 파일 경로에 지정한 이름으로 db가 생성된다.

// 만든 db 가져오기
    InputStream downloadFile = new FileInputStream(filesname); // db 읽을 준비
    byte[] encodeDownloadFile = IOUtils.toByteArray(downloadFile); // db를 byte[] 타입으로 변환

    final HttpHeaders headers = new HttpHeaders();
    headers.setContentType(MediaType.APPLICATION_OCTET_STREAM);
    String realfilename = URLEncoder.encode("db명.db", "UTF-8");
    headers.add("Content-Disposition", "attachment; filename=\"" + realfilename + "\"");

    ResponseEntity<byte[]> downloadDBfileEntity = new ResponseEntity<byte[]>(encodeDownloadFile, headers, HttpStatus.OK); // db를 ResponseEntity에 넣어서 가져올 준비
    downloadFile.close(); // InputStream 종료

    return downloadDBfileEntity; // db 파일 가져옴

// 옵션
    // 생성된 파일 삭제
    File sqliteFile = new File(filesname); // 파일 지정
    folderByFile.delete(); // 삭제

    // db 가져온 로그 기록하는 메소드 생성(modelmap 이용)