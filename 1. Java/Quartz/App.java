package co.kr.mureng.src.quartz;

import static org.quartz.CronScheduleBuilder.cronSchedule;
import static org.quartz.JobBuilder.newJob;
import static org.quartz.TriggerBuilder.newTrigger;

import org.quartz.CronTrigger;
import org.quartz.JobDetail;
import org.quartz.Scheduler;
import org.quartz.SchedulerException;
import org.quartz.SchedulerFactory;
import org.quartz.impl.StdSchedulerFactory;

public class App {
	
	private static final SchedulerFactory SF = new StdSchedulerFactory();
	private static Scheduler sched = null;
	private static JobDetail job = null;
	private static CronTrigger trigger = null;
	
	public static void main(String[] args) {
		System.out.println( "Schedule start" );
		String cronSch = "0/1 * * * * ?"; // 1초마다 실행
		try {
			sched = SF.getScheduler();
			job = newJob(MyWorker.class).withIdentity("MyWorker", "jobGroup").build();
			trigger = newTrigger() .withIdentity("MyWorker", "jobGroup").withSchedule(cronSchedule(cronSch)) .build();
			sched.scheduleJob(job, trigger);
			
			Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
			scheduler.start();
			
			sched.start(); // 작업을 실행하기 전 호출
		} catch (Exception e) {
			e.printStackTrace();
			if(sched != null){ // 스케줄러에 데이터가 존재한 상태로 예외가 발생하면 shutdown 시킴
				try {
					sched.shutdown();
				} catch (SchedulerException e1) {
					e1.printStackTrace();
				}
			}
			sched = null;
		}
	}
}