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
                .on("FAILED") //startStep의 ExitStatus가 FAILED일 경우
                .to(failOverStep()) //failOver Step을 실행
                .on("*") //failOver Step의 결과와 상관없이
                .to(writeStep()) //write Step을 실행
                .on("*") //write Step의 결과와 상관없이
                .end() //Flow를 종료

            .from(startStep()) //startStep이 FAILED가 아니고
                .on("COMPLETED") //COMPLETED일 경우
                .to(processStep()) //process Step을 실행
                .on("*") //process Step의 결과와 상관없이
                .to(writeStep()) // write Step을 실행
                .on("*") //wrtie Step의 결과와 상관없이
                .end() //Flow를 종료

            .from(startStep()) //startStep의 결과가 FAILED, COMPLETED가 아닌
                .on("*") //모든 경우
                .to(writeStep()) //write Step을 실행
                .on("*") //write Step의 결과와 상관없이
                .end() //Flow를 종료
            .end()
            .build();

        return exampleJob;
    }

    @Bean
    public Step startStep() {
        return stepBuilderFactory.get("startStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("Start Step!");

                String result = "COMPLETED";
                //String result = "FAIL";
                //String result = "UNKNOWN";

                //Flow에서 on은 RepeatStatus가 아닌 ExitStatus를 바라본다.
                if(result.equals("COMPLETED")) 
                    contribution.setExitStatus(ExitStatus.COMPLETED);
                else if(result.equals("FAIL"))  
                    contribution.setExitStatus(ExitStatus.FAILED);
                else if(result.equals("UNKNOWN"))  
                    contribution.setExitStatus(ExitStatus.UNKNOWN);

                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step failOverStep(){
        return stepBuilderFactory.get("nextStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("FailOver Step!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step processStep(){
        return stepBuilderFactory.get("processStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("Process Step!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step writeStep(){
        return stepBuilderFactory.get("writeStep")
            .tasklet((contribution, chunkContext) -> {
                log.info("Write Step!");
                return RepeatStatus.FINISHED;
            })
            .build();
    }
}