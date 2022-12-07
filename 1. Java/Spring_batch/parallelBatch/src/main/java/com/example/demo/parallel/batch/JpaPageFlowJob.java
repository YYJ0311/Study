package com.example.demo.parallel.batch;

import javax.persistence.EntityManagerFactory;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.core.job.builder.FlowBuilder;
import org.springframework.batch.core.job.flow.Flow;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.database.JpaItemWriter;
import org.springframework.batch.item.database.JpaPagingItemReader;
import org.springframework.batch.item.database.builder.JpaPagingItemReaderBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.task.SimpleAsyncTaskExecutor;

import com.example.demo.parallel.domain.Dept;
import com.example.demo.parallel.domain.Dept2;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class JpaPageFlowJob {
	
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	private final EntityManagerFactory entityManagerFactory;
	
	private int chunkSize = 10;

// 10000건의 배치를 2개로 나눠서 처리할 것임
	
	// JOB (Flow 사용)
	@Bean
	public Job jpaPageFlowJob_batchBuild() {
		Flow flow1 = new FlowBuilder<Flow>("flow1")
				.start(jpaPageJob_1_batchStep1()) // 1번째 step
				.build();
		
		Flow flow2 = new FlowBuilder<Flow>("flow2")
				.start(jpaPageJob_2_batchStep1()) // 2번째 step
				.build();
		
		// flow 합침
		Flow parallelStepFlow = new FlowBuilder<Flow>("parallelStepFlow")
				.split(new SimpleAsyncTaskExecutor())
				.add(flow1, flow2)
				.build();
		
		return jobBuilderFactory.get("jpaPageFlowJob")
				.start(parallelStepFlow)
				.build().build(); // flowJob과 job에 대한 build()
	}
	
	// STEP
	@Bean
	public Step jpaPageJob_1_batchStep1() {
		return stepBuilderFactory.get("JpaPageFlowJob_1_Step")
				.<Dept,Dept2>chunk(chunkSize)
				.reader(jpaPageJob_1_dbItemReader())
				.processor(jpaPageJob_1_processor())
				.writer(jpaPageJob_1_dbItemWriter())
				.build();
	}	
	@Bean
	public Step jpaPageJob_2_batchStep1() {
		return stepBuilderFactory.get("JpaPageFlowJob_2_Step")
				.<Dept,Dept2>chunk(chunkSize)
				.reader(jpaPageJob_2_dbItemReader())
				.processor(jpaPageJob_2_processor())
				.writer(jpaPageJob_2_dbItemWriter())
				.build();
	}
	
	// BATCH
	// 5000을 포함하고 그보다 작은 dept_no에 대하여 batch1 수행
	@Bean
	public JpaPagingItemReader<Dept> jpaPageJob_1_dbItemReader() {
		return new JpaPagingItemReaderBuilder<Dept>()
				.name("JpaPageJob1_Reader")
				.entityManagerFactory(entityManagerFactory)
				.pageSize(chunkSize)	
				.queryString("SELECT d FROM Dept d where dept_no < 5000 order by dept_no asc")
				.build();
	}
	@Bean
	public ItemProcessor<Dept, Dept2> jpaPageJob_1_processor() {
		return new ItemProcessor<Dept, Dept2>() {
			@Override
			public Dept2 process(Dept dept) throws Exception {
				return new Dept2(dept.getDeptNo(), "NEW_" + dept.getDName(), "NEW_" + dept.getLoc());
			}
		};
	}
	@Bean
	public JpaItemWriter<Dept2> jpaPageJob_1_dbItemWriter() {
		JpaItemWriter<Dept2> jpaItemWriter = new JpaItemWriter<Dept2>();
		jpaItemWriter.setEntityManagerFactory(entityManagerFactory);
		return jpaItemWriter;
	}
	
	// 5000보다 큰 dept_no에 대하여 batch2 수행
	@Bean
	public JpaPagingItemReader<Dept> jpaPageJob_2_dbItemReader() {
		return new JpaPagingItemReaderBuilder<Dept>()
				.name("JpaPageJob1_Reader")
				.entityManagerFactory(entityManagerFactory)
				.pageSize(chunkSize)
				.queryString("SELECT d FROM Dept d where dept_no >= 5000 order by dept_no asc")
				.build();
	}
	@Bean
	public ItemProcessor<Dept, Dept2> jpaPageJob_2_processor() {
		return new ItemProcessor<Dept, Dept2>() {
			@Override
			public Dept2 process(Dept dept) throws Exception {
				return new Dept2(dept.getDeptNo(), "NEW_" + dept.getDName(), "NEW_" + dept.getLoc());
			}
		};
	}
	@Bean
	public JpaItemWriter<Dept2> jpaPageJob_2_dbItemWriter() {
		JpaItemWriter<Dept2> jpaItemWriter = new JpaItemWriter<Dept2>();
		jpaItemWriter.setEntityManagerFactory(entityManagerFactory);
		return jpaItemWriter;
	}
}
