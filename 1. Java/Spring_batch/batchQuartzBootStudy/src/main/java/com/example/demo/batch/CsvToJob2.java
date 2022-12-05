package com.example.demo.batch;

import java.io.IOException;

import javax.persistence.EntityManagerFactory;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.database.JpaItemWriter;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.FlatFileParseException;
import org.springframework.batch.item.file.MultiResourceItemReader;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ResourceLoader;
import org.springframework.core.io.support.ResourcePatternUtils;

import com.example.demo.domain.Dept;
import com.example.demo.dto.TwoDto;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class CsvToJob2 { // 멀티 csv 파일을 DB에 insert
	
	private final ResourceLoader resourceLoader;
	
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	private final EntityManagerFactory entityManagerFactory;
	
	private int chunkSize = 5;
	
	@Bean
	public Job csvToJpaJob2_batchBuild() throws Exception{
		return jobBuilderFactory.get("csvToJpaJob2")
				.start(csvToJpaJob2_batchStep1())
				.build();
	}
	
	@Bean
	public Step csvToJpaJob2_batchStep1() throws Exception{
		return stepBuilderFactory.get("csvToJpaJob2_batchStep1")
				.<TwoDto, Dept>chunk(chunkSize) // TwoDto에서 Dept타입으로
				.reader(csvToJpaJob2_FileReader())
				.processor(csvToJpaJob2_processor())
				.writer(csvToJpaJob2_dbItemWriter())
				.faultTolerant()
				.skip(FlatFileParseException.class) // 해당 에러에 대해 그냥 넘어가고 다음 항목 write하기
				.skipLimit(100) // 넘길 수 있는 skip 제한수
				.build();
	}
	
	@Bean
	public ItemProcessor<TwoDto, Dept> csvToJpaJob2_processor(){
		return twoDto -> new Dept(Integer.parseInt(twoDto.getOne()), twoDto.getTwo(), "기타");
	}

	@Bean
	public JpaItemWriter<Dept> csvToJpaJob2_dbItemWriter(){
		JpaItemWriter<Dept> jpaItemWriter = new JpaItemWriter<>();
		jpaItemWriter.setEntityManagerFactory(entityManagerFactory);
		return jpaItemWriter;
	}
	
	@Bean
	public MultiResourceItemReader<TwoDto> csvToJpaJob2_FileReader(){
		MultiResourceItemReader<TwoDto> twoDtoMultiResourceItemReader = new MultiResourceItemReader<>();
		try {
			twoDtoMultiResourceItemReader.setResources(
					ResourcePatternUtils.getResourcePatternResolver(this.resourceLoader).getResources(
							"classpath:sample/csvToJpaJob2/*.txt")
			);
		} catch (IOException e) {
			e.printStackTrace();
		}
		twoDtoMultiResourceItemReader.setDelegate(multiFileItemReader());
		return twoDtoMultiResourceItemReader;
	}
	
	@Bean
	public FlatFileItemReader<TwoDto> multiFileItemReader(){ // 이전까지 라인으로 읽어면서 길어졌던 코드를 간결화 시킴
		FlatFileItemReader<TwoDto> flatFileItemReader = new FlatFileItemReader<>();
		flatFileItemReader.setLineMapper((line, lineNumber) -> {
			String [] lines = line.split("#");
			return new TwoDto(lines[0], lines[1]);
		});
		
		return flatFileItemReader;
	}
}
