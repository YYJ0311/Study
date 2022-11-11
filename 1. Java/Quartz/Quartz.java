package co.kr.mureng.src.quartz;

import org.quartz.DisallowConcurrentExecution;
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

@DisallowConcurrentExecution 
public class MyWorker implements Job{
	
	private static boolean isWorking = false;
	  
	@Override
	public void execute(JobExecutionContext context) throws JobExecutionException {
		// TODO Auto-generated method stub
		todo();
	}

//	class에 어노테이션 없이 사용하는 코드 => 스케줄러가 뒤죽박죽 실행됨
//	private void todo() {
//		synchronized (this) {
//			if(!isWorking){
//		        isWorking = true;
//		        for(int i = 0;i < 10; i++){
//		          try {
//		            Thread.sleep(300);
//		          } catch (InterruptedException e) {
//		            e.printStackTrace();
//		          }
//		        }
//		        System.out.println("[***" + Thread.currentThread().getName() + "***]");
//		        isWorking = false;
//			}
//		}
//	}

//	아래는 @DisallowConcurrentExecution 어노테이션을 class에 붙이고 사용 => 스케줄러의 동작이 겹치지 않아서 순차적으로 실행됨
	private void todo(){
		for(int i = 0; i < 10; i++){
			try {
				Thread.sleep(3); // 딜레이 시간설정
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println("[***" + Thread.currentThread().getName() + "***]");
	}
}

// [***MyScheduler_Worker-1***]
// [***MyScheduler_Worker-2***]
// [***MyScheduler_Worker-3***]
// [***MyScheduler_Worker-1***]
// [***MyScheduler_Worker-2***]
// [***MyScheduler_Worker-3***]
// ...
// 3개의 쓰레드로 작업이 계속 반복됨