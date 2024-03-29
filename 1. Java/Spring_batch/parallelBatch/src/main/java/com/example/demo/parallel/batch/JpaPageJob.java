package com.example.demo.parallel.batch;

import javax.persistence.EntityManagerFactory;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.JobScope;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.database.JpaItemWriter;
import org.springframework.batch.item.database.JpaPagingItemReader;
import org.springframework.batch.item.database.builder.JpaPagingItemReaderBuilder;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.example.demo.parallel.domain.Dept;
import com.example.demo.parallel.domain.Dept2;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class JpaPageJob {
	
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	private final EntityManagerFactory entityManagerFactory;
	
	@Bean
	public Job jpaPageJob_batchBuild() {
		return jobBuilderFactory.get("jpaPageJob")
				.start(jpaPageJob_batchStep1(0))
				.build();
	}
	
	@Bean
	@JobScope
	public Step jpaPageJob_batchStep1(@Value("#{jobParameters[chunkSize]}") int chunkSize) {
		return stepBuilderFactory.get("JpaPageJob1_Step")
				.<Dept,Dept2>chunk(chunkSize)
				.reader(jpaPageJob_dbItemReader(0))
				.processor(jpaPageJob_processor())
				.writer(jpaPageJob_dbItemWriter())
				.build();
	}
	
	@Bean
	@JobScope
	public JpaPagingItemReader<Dept> jpaPageJob_dbItemReader(@Value("#{jobParameters[chunkSize]}") int chunkSize) {
		return new JpaPagingItemReaderBuilder<Dept>()
				.name("JpaPageJob1_Reader")
				.entityManagerFactory(entityManagerFactory)
				.pageSize(chunkSize)
				.queryString("SELECT d FROM Dept d order by dept_no asc") // 여기서 FROM 뒤에 오는 것은 domain의 클래스명과 일치해야 함!
				.build();
	}
	
	@Bean
	public ItemProcessor<Dept, Dept2> jpaPageJob_processor(){
		return new ItemProcessor<Dept, Dept2>() {
			@Override
			public Dept2 process(Dept dept) throws Exception {
				return new Dept2(dept.getDeptNo(), "NEW_"+dept.getDName(), "NEW_"+dept.getLoc());
			}
		};
		// return dept -> new Dept2(dept.getDeptNo(), "NEW_"+dept.getDName(), "NEW_"+dept.getLoc()); java 1.8부터 람다식 지원
	}
	
	@Bean
	public JpaItemWriter<Dept2> jpaPageJob_dbItemWriter() {
		JpaItemWriter<Dept2> jpaItemWriter = new JpaItemWriter<Dept2>();
		jpaItemWriter.setEntityManagerFactory(entityManagerFactory);
		return jpaItemWriter;
	}
}