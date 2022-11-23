import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class ScrapingMenu {
	public static String id = "webdriver.chrome.driver";
	public static String path = "C:\\sts3Test-workspace\\practice\\chromedriver.exe";
	
	@Scheduled(cron="0 * * * * *") // 매 분 0초마다 실행됨
	public void readMenu() throws IOException {
		// 크롬 드라이버 로딩
		System.setProperty(id, path); 
		// 크롬 브라우저를 열 때 사용할 옵션을 설정하기 위한 객체
		ChromeOptions options = new ChromeOptions();
		
		String url = "https://ccc.pe.kr/";
		
		// 위에서 설정한 옵션으로 크롬 드라이버 실행
		WebDriver driver = new ChromeDriver(options);
		
		driver.get(url);
		
		try {
			Thread.sleep(1000); // 페이지 열림 기다림
			
//			String fileName = "";
			String filePath = "C:\\Users\\Mureung\\Downloads\\";
//			File folder = new File(filePath);
			
			WebElement searchInput = driver.findElement(By.cssSelector("div#menu_menuDIV li.m4 a.depth1"));
			searchInput.click();
			searchInput = driver.findElement(By.xpath("//*[contains(text(), '[공지]구내식당 주간식단표 ')]"));
			searchInput.click();
			searchInput = driver.findElement(By.cssSelector("div.content p.files a"));
			String searchFile = searchInput.getText().replace("[다운로드]", "");
			System.out.println("searchFile : "+searchFile);
			
			File checkFile = new File(filePath+searchFile);
			if(checkFile.isFile()) { // isFile()로 파일 유무 체크
				System.out.println(searchFile+"이 이미 존재함");
			} else {
				searchInput.click(); // 로컬에 파일이 존재하지 않으면 식단 다운로드
				System.out.println(searchFile+" 다운로드함");
			}
			
			Thread.sleep(5000); // 파일 다운로드 3초 기다림
			
			if(!Desktop.isDesktopSupported()) {
				System.out.println("not supported");
				return;
			}
			Desktop desktop = Desktop.getDesktop();
			desktop.open(checkFile); // 파일 열기

			driver.quit(); // 열었던 웹페이지 닫기
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	} 
}
