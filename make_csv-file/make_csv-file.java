// csv 파일이 저장될 경로를 미리 설정
String path = "C:\\temp\\";
String folder = "폴더이름1-1" + 폴더이름에_들어갈_변수 + "폴더이름1-2\\";
File folderByFile = new File(path + folder); 

String parameterFilePath = path + folder + "parameter.csv";
String commSpecFilePath = path + folder + "commspec.csv";
String dtcBankFilePath = path + folder + "dtcbank.csv";

// 폴더가 존재하는 경우 삭제 후 재생성(오류 방지)
if (folderByFile.exists()){
    File[] folder_list = folderByFile.listFiles();
    
    for (int j = 0; j < folder_list.length; j++){
        folder_list[j].delete();				
    }
            
    if(folder_list.length == 0 && folderByFile.isDirectory()){ 
        folderByFile.delete();
    }
}

try{folderByFile.mkdir();} 
catch(Exception e){e.getStackTrace();}

// 프로시저의 파라미터로 넘겨 줄 modelMap 생성이 선행되어야 함
Map<String, Object> modelMap = new HashMap<String, Object>();
modelMap.put("key", value);

// mvc 패턴으로 프로시저 호출, csv 파일 생성
this.서비스.메소드명(modelMap);