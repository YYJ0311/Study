package test.every.things;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;

public class HttpConnection {
	public static void main(String[] args) {
		getJson();
	}
	
	public static void getJson() {
		try {
			URL url = new URL("주소");
			HttpURLConnection conn = (HttpURLConnection)url.openConnection();
			
			conn.setRequestMethod("GET"); // 
			conn.setRequestProperty("Content-Type", "application/json");
			conn.setRequestProperty("auth", "myAuth");
			conn.setDoOutput(true); // 서버로부터 받는 값이 있다면 true
            // conn.setDoInput(true); // 서버에 전달할 값이 있다면 true
			
			BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			StringBuilder sb = new StringBuilder();
			String line = null;
			
			while((line = br.readLine()) != null) {
				sb.append(line);
			}
			
			JSONObject obj = new JSONObject(sb.toString());
			System.out.println("response= " + obj.get("response"));
            // response 대신 첫 {} 안에 들어오는 key 값을 적으면 됨.
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
