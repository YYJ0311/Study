@Slf4j
@Configuration
@EnableBatchProcessing
public class ExampleJobConfig {

    @Autowired public JobBuilderFactory jobBuilderFactory;
    @Autowired public StepBuilderFactory stepBuilderFactory;
    @Bean
    public Job ExampleJob(){
        Job exampleJob = jobBuilderFactory.get("exampleJob")
            .start(startStep())
            .next(nextStep())
            .next(lastStep())
            .build();
        return exampleJob;
    }

    @Bean
    public Step startStep() { // step1
        return stepBuilderFactory.get("startStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("Start Step!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step nextStep(){ // step2
        return stepBuilderFactory.get("nextStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("Next Step!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step lastStep(){ // step3
        return stepBuilderFactory.get("lastStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("Last Step!!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }
}