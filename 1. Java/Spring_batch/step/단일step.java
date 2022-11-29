@Slf4j
@Configuration
@EnableBatchProcessing
public class ExampleJobConfig {

    @Autowired public JobBuilderFactory jobBuilderFactory;
    @Autowired public StepBuilderFactory stepBuilderFactory;
    @Bean
    public Job ExampleJob(){
        Job exampleJob = jobBuilderFactory.get("exampleJob")
            .start(Step()) // 이름이 Step인 step 실행
            .build();
        return exampleJob;
    }

    @Bean
    public Step Step() {
        return stepBuilderFactory.get("step")
            .tasklet((contribution, chunkContext) -> {
                log.info("Step!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }
}