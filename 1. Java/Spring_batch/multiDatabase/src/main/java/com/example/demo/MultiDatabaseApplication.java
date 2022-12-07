package com.example.demo;

import org.springframework.batch.core.configuration.annotation.EnableBatchProcessing;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@EnableBatchProcessing
@SpringBootApplication
public class MultiDatabaseApplication {

	public static void main(String[] args) {
		SpringApplication.run(MultiDatabaseApplication.class, args);
	}
}
