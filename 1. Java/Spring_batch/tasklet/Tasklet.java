@Slf4j
@EnableBatchProcessing
@Configuration
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
            .tasklet((contribution, chunkContext) ->{

                //비즈니스 로직
                for(int idx = 0; idx < 10; idx ++){
                    log.info("[idx] = " + idx);
                }

                return RepeatStatus.FINISHED;
            }).build();
    }
}