package com.example.demo.batch;

import javax.annotation.Resource;
import javax.persistence.EntityManagerFactory;
import javax.sql.DataSource;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.JobScope;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepScope;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.database.JdbcBatchItemWriter;
import org.springframework.batch.item.database.JpaPagingItemReader;
import org.springframework.batch.item.database.builder.JdbcBatchItemWriterBuilder;
import org.springframework.batch.item.database.builder.JpaPagingItemReaderBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.example.demo.domain.db1.Dept1;
import com.example.demo.domain.db2.Dept2;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Configuration
@RequiredArgsConstructor
public class JpaPageJob2 {
	@Autowired
	private final JobBuilderFactory jobBuilderFactory;
	@Autowired
	private final StepBuilderFactory stepBuilderFactory;
	
	@Resource(name="entityManagerFactory1") // DbConfig1에서의 EntityManagerFactory명
	private EntityManagerFactory entityManagerFactory1;
	
	@Resource(name="dataSource2")
	private DataSource dataSource2;
	
	private int chunkSize = 10;
	
	@Bean
	public Job jpaPageJob2_batchBuild() {
		return jobBuilderFactory.get("JpaPageJob2")
				.start(jpaPageJob2_batchStep1())
				.build();
	}
	
	@Bean
	@JobScope
	public Step jpaPageJob2_batchStep1() {
		return stepBuilderFactory.get("JpaPageJob1_Step")
				.<Dept1, Dept2>chunk(chunkSize) // dept1 -> dept2
				.reader(jpaPageJob2_dbItemReader())
				.processor(jpaPageJob2_processor())
				.writer(jdbcBatchItemWriter())
				.build();
	}
	
    @Bean
    @StepScope
    public JpaPagingItemReader<Dept1> jpaPageJob2_dbItemReader() {
        return new JpaPagingItemReaderBuilder<Dept1>()
                .name("JpaPageJob1_Reader")
                .entityManagerFactory(entityManagerFactory1)
                .pageSize(chunkSize)
                .queryString("SELECT d FROM Dept1 d order by deptno asc")
                .build();
    }

    @Bean
    @StepScope
    public ItemProcessor<Dept1, Dept2> jpaPageJob2_processor() {
//    	return dept1 -> new Dept2(dept1.getDeptno(), "NEW_" + dept1.getDname(), "NEW_" + dept1.getLoc()); 
        return dept1 -> { // 짝수만 결과물을 얻을 수 있게 수정
            if(dept1.getDeptno() % 2 == 0){
                return new Dept2(dept1.getDeptno(), "NEW_" + dept1.getDname(), "NEW_" + dept1.getLoc());
            }
            return null;
        };
    }

    /**
    @Bean
    @StepScope
    public JpaItemWriter<Dept2> jpaPageJob2_dbItemWriter() {
        JpaItemWriter<Dept2> jpaItemWriter = new JpaItemWriter<>();
        jpaItemWriter.setEntityManagerFactory(entityManagerFactory2);
        return jpaItemWriter;
    }
    **/
    @Bean
    public JdbcBatchItemWriter<Dept2> jdbcBatchItemWriter() {
        return new JdbcBatchItemWriterBuilder<Dept2>() // JDBC Writer 사용
                .dataSource(dataSource2) // dataSource2를 mapping
                .sql("insert into dept2(deptno, dname, loc) values (:deptno, :dname, :loc)")
                .beanMapped()
                .build();
    }
}