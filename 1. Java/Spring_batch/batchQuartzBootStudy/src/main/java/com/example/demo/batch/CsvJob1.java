package com.example.demo.batch;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.mapping.BeanWrapperFieldSetMapper;
import org.springframework.batch.item.file.mapping.DefaultLineMapper;
import org.springframework.batch.item.file.transform.DelimitedLineTokenizer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;

import com.example.demo.dto.TwoDto;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class CsvJob1 {
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	
	private int chunkSize = 5; // 10개씩 잘라서 배치를 처리(db 부하 줄이기 위해)

	@Bean
	public Job csvJob1_batchBuild() {
		return jobBuilderFactory.get("csvJob1")
				.start(csvJob1_batchStep1())
				.build();
	}
	
	@Bean
	public Step csvJob1_batchStep1() {
		return stepBuilderFactory.get("csvJob1_batchStep1")
				.<TwoDto, TwoDto>chunk(chunkSize)
				.reader(csvJob1_FileReader())
				.writer(twoDto -> twoDto.stream().forEach(twoDto2 -> {
					log.debug(twoDto2.toString());
				})).build();
	}
	
	@Bean
	public FlatFileItemReader<TwoDto> csvJob1_FileReader(){
		FlatFileItemReader<TwoDto> flatFileItemReader = new FlatFileItemReader<>();
		flatFileItemReader.setResource(new ClassPathResource("/sample/csvJob1_input.csv")); // 해당 경로 파일 읽음
		flatFileItemReader.setLinesToSkip(1); // 첫줄은 컬럼명이기 때문에 스킵
		
		DefaultLineMapper<TwoDto> dtoDefaultLineMapper = new DefaultLineMapper<>(); // line mapper 생성
		
		DelimitedLineTokenizer delimitedLineTokenizer = new DelimitedLineTokenizer();
		delimitedLineTokenizer.setNames("one", "two"); // 컬럼명으로 구분
		delimitedLineTokenizer.setDelimiter(":"); // csv의 기본 구분자 , 대신에 : 로 구분함
		 
		BeanWrapperFieldSetMapper<TwoDto> beanWrapperFieldSetMapper = new BeanWrapperFieldSetMapper<>();
		beanWrapperFieldSetMapper.setTargetType(TwoDto.class); // set하기 위한 타입 지정
		
		dtoDefaultLineMapper.setLineTokenizer(delimitedLineTokenizer); // line mapper에 구분자 입력
		dtoDefaultLineMapper.setFieldSetMapper(beanWrapperFieldSetMapper); // type 입력
		flatFileItemReader.setLineMapper(dtoDefaultLineMapper);
		
		return flatFileItemReader;
	}
}
