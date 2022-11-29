// startlimit : 해당 step 실패 이후 재시작 가능 횟수
// startlimit 이후 실행에서는 exception 발생

@Bean
@JobScope
public Step Step() throws Exception {
    return stepBuilderFactory.get("Step")
        .startLimit(3)
        .<Member,Member>chunk(10)
        .reader(reader(null))
        .processor(processor(null))
        .writer(writer(null))
        .build();
}