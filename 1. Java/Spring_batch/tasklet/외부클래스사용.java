@Slf4j
public class BusinessTasklet implements Tasklet, StepExecutionListener {

    @Override
    @BeforeStep
    public void beforeStep(StepExecution stepExecution) {
        log.info("Before Step Start!");
    }

    @Override
    @AfterStep
    public ExitStatus afterStep(StepExecution stepExecution) {
        log.info("After Step Start!");
        return ExitStatus.COMPLETED;
    }

    @Override
    public RepeatStatus execute(StepContribution stepContribution, ChunkContext chunkContext) throws Exception {
        //비즈니스 로직
        for (int idx = 0; idx < 10; idx++) {
            log.info("[idx] = " + idx);
        }
        return RepeatStatus.FINISHED;
    }
}

@Slf4j
@Configuration
@EnableBatchProcessing
public class TaskletJobConfig{

    @Autowired public JobBuilderFactory jobBuilderFactory;
    @Autowired public StepBuilderFactory stepBuilderFactory;
    @Bean
    public Job TaskletJob(){
        Job customJob = jobBuilderFactory.get("taskletJob")
                .start(TaskStep())
                .build();
        return customJob;
    }

    @Bean
    public Step TaskStep(){
        return stepBuilderFactory.get("taskletStep")
                .tasklet(new BusinessTasklet())
                .build();
    }
}