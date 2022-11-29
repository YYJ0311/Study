// MethodInvokingAdapter 사용하여 구현
@Slf4j
public class CustomService {
    public void businessLogic() {
        //비즈니스 로직
        for(int idx = 0; idx < 10; idx ++){
            log.info("[idx] = " + idx);
        }
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
            .tasklet(myTasklet()).build();
    }

    @Bean
    public CustomService service() {
        return new CustomService ();
    }

    @Bean
    public MethodInvokingTaskletAdapter myTasklet() {
        MethodInvokingTaskletAdapter adapter = new MethodInvokingTaskletAdapter();

        adapter.setTargetObject(service());
        adapter.setTargetMethod("businessLogic");

        return adapter;
    }
}