package com.example.demo.batch;

import javax.persistence.EntityManagerFactory;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.database.JpaItemWriter;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.mapping.BeanWrapperFieldSetMapper;
import org.springframework.batch.item.file.mapping.DefaultLineMapper;
import org.springframework.batch.item.file.transform.DelimitedLineTokenizer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;

import com.example.demo.domain.Dept;
import com.example.demo.dto.TwoDto;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class CsvToJob1 { // 단일 csv 파일을 DB에 insert
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	private final EntityManagerFactory entityManagerFactory;
	
	private int chunkSize = 5;
	
	@Bean
	public Job csvToJpaJob1_batchBuild() throws Exception{
		return jobBuilderFactory.get("csvToJpaJob1")
				.start(csvToJpaJob1_batchStep1())
				.build();
	}
	
	@Bean
	public Step csvToJpaJob1_batchStep1() throws Exception{
		return stepBuilderFactory.get("csvToJpaJob1_batchStep1")
				.<TwoDto, Dept>chunk(chunkSize) // TwoDto에서 Dept타입으로
				.reader(csvToJpaJob1_FileReader())
				.processor(csvToJpaJob1_processor())
				.writer(csvToJpaJob1_dbItemWriter())
				.build();
	}
	
	@Bean
	public ItemProcessor<TwoDto, Dept> csvToJpaJob1_processor(){
		return twoDto -> new Dept(Integer.parseInt(twoDto.getOne()), twoDto.getTwo(), "기타");
	}

	@Bean
	public JpaItemWriter<Dept> csvToJpaJob1_dbItemWriter(){
		JpaItemWriter<Dept> jpaItemWriter = new JpaItemWriter<>();
		jpaItemWriter.setEntityManagerFactory(entityManagerFactory);
		return jpaItemWriter;
	}
	
	@Bean
	public FlatFileItemReader<TwoDto> csvToJpaJob1_FileReader(){
		FlatFileItemReader<TwoDto> flatFileItemReader = new FlatFileItemReader<>();
		flatFileItemReader.setResource(new ClassPathResource("/sample/csvToJpaJob1_input.csv")); // 해당 경로 파일 읽음
//		flatFileItemReader.setLinesToSkip(1); // 첫줄은 컬럼명이기 때문에 스킵
		DefaultLineMapper<TwoDto> defaultLineMapper = new DefaultLineMapper<>(); // line mapper 생성
		DelimitedLineTokenizer delimitedLineTokenizer = new DelimitedLineTokenizer();
		delimitedLineTokenizer.setNames("one", "two"); // 컬럼명으로 구분
		delimitedLineTokenizer.setDelimiter(":"); // csv의 기본 구분자 , 대신에 : 로 구분함
		 
		BeanWrapperFieldSetMapper<TwoDto> beanWrapperFieldSetMapper = new BeanWrapperFieldSetMapper<>();
		beanWrapperFieldSetMapper.setTargetType(TwoDto.class); // set하기 위한 타입 지정
		defaultLineMapper.setLineTokenizer(delimitedLineTokenizer); // line mapper에 구분자 입력
		defaultLineMapper.setFieldSetMapper(beanWrapperFieldSetMapper); // type 입력
		flatFileItemReader.setLineMapper(defaultLineMapper);
		return flatFileItemReader;
	}
}
