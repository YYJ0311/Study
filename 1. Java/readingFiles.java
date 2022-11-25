/* 1. Desktop 클래스를 사용하여 Java에서 파일 열기 */
// 파일 또는 URI를 처리하기 위해 기본 데스크탑에서 등록된 애플리케이션을 시작하는 데 사용되는 AWT 패키지의 Desktop 클래스를 사용

import java.awt.*;
import java.io.File;

public class OpenFile {
    public static void main(String args[]){
        try
        {
            File file = new File("/Users/john/Desktop/demo.txt"); // 파일 경로
            if(!Desktop.isDesktopSupported())
            {
                System.out.println("not supported");
                return;
            }
            Desktop desktop = Desktop.getDesktop();
            if(file.exists())
                desktop.open(file); // 파일 실행
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}    

/* 2. FileInputStream 클래스 사용 */
// 오디오, 이미지 데이터, 비디오 등과 같은 바이트 지향 데이터를 읽을 수 있는 FileInputStream 클래스를 사용

import java.io.File;
import java.io.FileInputStream;

public class OpenFile {
    public static void main(String args[]){
       try
        {
            File f = new File("/Users/john/Desktop/demo.txt");
            FileInputStream fIS = new FileInputStream(f);
            System.out.println("file content: ");
            int r = 0;
            while((r = fIS.read())!=-1) 
            // 더이상 읽을 데이터가 없으면 read()는 -1을 반환하고 while 문이 종료된다.
            {
                System.out.print((char)r);
            }
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}
/* 3. BufferedReader 클래스 사용 */
// 문자 기반 입력 스트림에서 텍스트를 읽기 위해 BufferedReader 클래스를 사용하고, 문자 파일을 읽기 위해 FileReader를 사용함
// BufferedReader로 만든 버퍼링 문자 입력 스트림을 read()를 통해 읽어온다.

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class OpenFile {
    public static void main(String args[]){
       try
        {
            File fil = new File("/Users/john/Desktop/demo2.txt");
            BufferedReader br = new BufferedReader(new FileReader(fil));
            System.out.println("file content: ");
            int r=0;
            while((r=br.read())!=-1)
            {
                System.out.print((char)r);
            }
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}

/* 4. Scanner 클래스 사용 */
// Scanner 클래스의 hasNextLine()를 이용해서 파일을 한 줄씩 읽음

import java.io.File;
import java.util.Scanner;

public class OpenFile {
    public static void main(String args[]){
        try
        {
            File file = new File("/Users/john/Desktop/demo1.txt");
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine())
                System.out.println(scanner.nextLine());
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}