package com.example.demo.batch;

import javax.persistence.EntityManagerFactory;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemWriter;
import org.springframework.batch.item.database.JpaPagingItemReader;
import org.springframework.batch.item.database.builder.JpaPagingItemReaderBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.example.demo.domain.Dept;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class JpaPageJob1 {

	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	private final EntityManagerFactory entityManagerFactory;
	
	private int chunkSize = 10; // 10개씩 잘라서 배치를 처리(db 부하 줄이기 위해)
	
	@Bean
	public Job JpaPageJob1_batchBuilder() { // job 설정
		return jobBuilderFactory.get("JpaPageJob1")
				.start(JpaPageJob1_step1()).build();
	}
	
	@Bean
	public Step JpaPageJob1_step1() { // step1 설정
		return stepBuilderFactory.get("JpaPageJob1_step1")
			.<Dept, Dept>chunk(chunkSize) // <읽는 DB , out DB> 
			.reader(jpaPageJob1_dbItemReader())
			.writer(jpaPageJob1_printItemWriter())
			.build();
	}
	
	@Bean
	public JpaPagingItemReader<Dept> jpaPageJob1_dbItemReader(){ // reader 생성
		return new JpaPagingItemReaderBuilder<Dept>()
				.name("JpaPageJob1_dbItemReader")
				.entityManagerFactory(entityManagerFactory)
				.pageSize(chunkSize)
				.queryString("SELECT d FROM Dept d order by dept_no asc")
				.build();
	}
	
	@Bean
	public ItemWriter<Dept> jpaPageJob1_printItemWriter(){ // read 확인용 writer 생성
		return list -> {
			for(Dept dept: list) {
				log.debug(dept.toString());
			}
		};
	}
}
