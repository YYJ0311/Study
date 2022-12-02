package com.example.demo.batch;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.mapping.BeanWrapperFieldSetMapper;
import org.springframework.batch.item.file.mapping.DefaultLineMapper;
import org.springframework.batch.item.file.transform.FixedLengthTokenizer;
import org.springframework.batch.item.file.transform.Range;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;

import com.example.demo.dto.TwoDto;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class fixedLengthJob1 {
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	
	private int chunkSize = 5;
	
	@Bean
	public Job fixedLengthJob1_batchBuild() {
		return jobBuilderFactory.get("fixedLengthJob1")
				.start(fixedLengthJob1_batchStep1())
				.build();
	}
	
	@Bean
	public Step fixedLengthJob1_batchStep1() {
		return stepBuilderFactory.get("fixedLengthJob1_batchStep1")
				.<TwoDto, TwoDto>chunk(chunkSize)
				.reader(fixedLengthJob1_FileReader())
				.writer(twoDto -> twoDto.stream().forEach(twoDto2 ->{
					log.debug(twoDto2.toString());
				}))
				.build();
	}
	
	@Bean
	public FlatFileItemReader<TwoDto> fixedLengthJob1_FileReader() {
		FlatFileItemReader<TwoDto> flatFileItemReader = new FlatFileItemReader<>();
		flatFileItemReader.setResource(new ClassPathResource("/sample/fixedLengthJob1_input.txt"));
		flatFileItemReader.setLinesToSkip(1); // 첫째 줄 스킵
		
		DefaultLineMapper<TwoDto> defaultLineMapper = new DefaultLineMapper<>();
		FixedLengthTokenizer fixedLengthTokenizer = new FixedLengthTokenizer();
		
		fixedLengthTokenizer.setNames("one", "two");
		fixedLengthTokenizer.setColumns(new Range(1, 5), new Range(6, 10)); // 1~5자리가 one, 6~10자리가 two
		BeanWrapperFieldSetMapper<TwoDto> beanWrapperFieldSetMapper = new BeanWrapperFieldSetMapper<>();
		beanWrapperFieldSetMapper.setTargetType(TwoDto.class);
		
		defaultLineMapper.setLineTokenizer(fixedLengthTokenizer);
		defaultLineMapper.setFieldSetMapper(beanWrapperFieldSetMapper);
		
		flatFileItemReader.setLineMapper(defaultLineMapper);
		return flatFileItemReader;
	}
}
