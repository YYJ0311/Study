package com.example.demo.batch;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.FlatFileItemWriter;
import org.springframework.batch.item.file.builder.FlatFileItemWriterBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.FileSystemResource;

import com.example.demo.custom.CustomPassThroughLineAggregator;
import com.example.demo.dto.OneDto;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class TextJob2 {
	private final JobBuilderFactory jobBuilderFactory;
	private final StepBuilderFactory stepBuilderFactory;
	
	private int chunkSize = 5; // 10개씩 잘라서 배치를 처리(db 부하 줄이기 위해)
	
	@Bean
	public Job textJob2_batchBuild() {
		return jobBuilderFactory.get("textJob2")
				.start(textJob2_batchStep1())
				.build();
	}
	
	@Bean
	public Step textJob2_batchStep1() {
		return stepBuilderFactory.get("textJob2_batchStep1")
				.<OneDto, OneDto>chunk(chunkSize)
				.reader(textJob2_FileReader())
				.writer(textJob2_FileWriter())
				.build();
	}
	
	@Bean
	public FlatFileItemReader<OneDto> textJob2_FileReader(){
		FlatFileItemReader<OneDto> flatFileItemReader = new FlatFileItemReader<>();
		flatFileItemReader.setResource(new ClassPathResource("sample/textJob2_input.txt"));
		flatFileItemReader.setLineMapper(((line, lineNumber) -> new OneDto(lineNumber + "==" + line))); // 한 줄씩 읽음
		return flatFileItemReader;
	}
	
	@Bean
	public FlatFileItemWriter textJob2_FileWriter() {
		return new FlatFileItemWriterBuilder<OneDto>()
				.name("textJob2_FileWriter")
				.resource(new FileSystemResource("output/textJob2_input.txt"))
				.lineAggregator(new CustomPassThroughLineAggregator<>())
				.build();
	}
}
