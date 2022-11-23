import java.io.IOException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import co.kr.패키지명.ScrapingMenu;

@Controller
@RequestMapping(value = "/test")
public class TestController {
	
	@GetMapping(value = "/")
	public Object test() throws IOException {
		System.out.println("식당메뉴 스케줄러 실행");
		ScrapingMenu menu = new ScrapingMenu();
		menu.readMenu(); // 스케줄러 메소드 실행
		return null;
	}
}
