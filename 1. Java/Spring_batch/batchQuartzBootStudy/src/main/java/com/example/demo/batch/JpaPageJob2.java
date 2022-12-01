package com.example.demo.batch;

import javax.persistence.EntityManagerFactory;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.database.JpaItemWriter;
import org.springframework.batch.item.database.JpaPagingItemReader;
import org.springframework.batch.item.database.builder.JpaPagingItemReaderBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.example.demo.domain.Dept;
import com.example.demo.domain.Dept2;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class JpaPageJob2 {

	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	private final EntityManagerFactory entityManagerFactory;
	
	private int chunkSize = 10; // 10개씩 잘라서 배치를 처리(db 부하 줄이기 위해)
	
	@Bean
	public Job JpaPageJob2_batchBuilder() { // job 설정
		return jobBuilderFactory.get("JpaPageJob2")
				.start(JpaPageJob2_step1()).build();
	}
	
	@Bean
	public Step JpaPageJob2_step1() { // step1 설정
		return stepBuilderFactory.get("JpaPageJob2_step1")
			.<Dept, Dept2>chunk(chunkSize) // <읽는 DB , out DB> 
			.reader(jpaPageJob2_dbItemReader())
			.processor(jpaPageJob2_processor())
			.writer(jpaPageJob2_dbItemWriter())
			.build();
	}
	
	private ItemProcessor<Dept, Dept2> jpaPageJob2_processor() {
		return dept -> {
			return new Dept2(dept.getDeptNo(), "NEW_"+dept.getDName(), "NEW_"+dept.getLoc());
		};
	}

	@Bean
	public JpaPagingItemReader<Dept> jpaPageJob2_dbItemReader(){ // reader 생성
		return new JpaPagingItemReaderBuilder<Dept>()
				.name("JpaPageJob2_dbItemReader")
				.entityManagerFactory(entityManagerFactory)
				.pageSize(chunkSize)
				.queryString("SELECT d FROM Dept d order by dept_no asc")
				.build();
	}
	
	@Bean
	public JpaItemWriter<Dept2> jpaPageJob2_dbItemWriter(){ // read 확인용 writer 생성
		JpaItemWriter<Dept2> jpaItemWriter = new JpaItemWriter<>();
		jpaItemWriter.setEntityManagerFactory(entityManagerFactory);
		return jpaItemWriter;
	}
}
