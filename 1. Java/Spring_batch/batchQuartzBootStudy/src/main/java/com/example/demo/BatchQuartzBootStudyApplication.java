package com.example.demo;

import org.springframework.batch.core.configuration.annotation.EnableBatchProcessing;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@EnableBatchProcessing // 배치 파일 인식
@SpringBootApplication
public class BatchQuartzBootStudyApplication {

	public static void main(String[] args) {
		SpringApplication.run(BatchQuartzBootStudyApplication.class, args);
	}
}
