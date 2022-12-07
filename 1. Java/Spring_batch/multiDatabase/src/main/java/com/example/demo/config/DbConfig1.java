package com.example.demo.config;

import javax.persistence.EntityManagerFactory;
import javax.sql.DataSource;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.jdbc.datasource.LazyConnectionDataSourceProxy;
import org.springframework.orm.jpa.JpaTransactionManager;
import org.springframework.orm.jpa.JpaVendorAdapter;
import org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;
import org.springframework.transaction.PlatformTransactionManager;

import com.google.common.collect.ImmutableMap;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

@Configuration
@ConfigurationProperties(prefix = "spring.db1.datasource") // application.yaml에서 설정한 datasource를 적용
@EnableJpaRepositories(
		entityManagerFactoryRef = "entityManagerFactory1",
		transactionManagerRef = "transactionManager1",
		basePackages = {"com.example.demo.domain.db1"})	// 위 datasource와 repository를 mapping하겠다는 의미
public class DbConfig1 extends HikariConfig {
    @Bean
    @Primary // main db라는 의미
    public DataSource dataSource1() {
        return new LazyConnectionDataSourceProxy(new HikariDataSource(this));
    }

    @Bean(name="entityManagerFactory1")
    @Primary
    public EntityManagerFactory entityManagerFactory1() {
        JpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();

        LocalContainerEntityManagerFactoryBean factory = new LocalContainerEntityManagerFactoryBean();
        factory.setDataSource(this.dataSource1());
        factory.setJpaVendorAdapter(vendorAdapter);
        factory.setJpaPropertyMap(ImmutableMap.of( // HibernateJpa 속성 정의(다른 프로젝트의 yaml 파일에서 hibernate 속성 설정한 것과 같음)
                "hibernate.hbm2ddl.auto", "update",
                "hibernate.dialect", "org.hibernate.dialect.MySQL5InnoDBDialect",
                "hibernate.show_sql", "true"
        ));

        factory.setPackagesToScan("com.example.demo.domain.db1"); // domain
        factory.setPersistenceUnitName("db1");
        factory.afterPropertiesSet();

        return factory.getObject();
    }

    @Bean
    @Primary
    public PlatformTransactionManager transactionManager1() {
        JpaTransactionManager tm = new JpaTransactionManager();
        tm.setEntityManagerFactory(entityManagerFactory1());
        return tm;
    }
}