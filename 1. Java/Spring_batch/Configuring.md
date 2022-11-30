# Configuring a Job
    @Bean
    public Job footballJob() {
        return this.jobBuilderFactory.get("footballJob")
                        .start(playerLoad())
                        .next(gameLoad())
                        .next(playerSummarization())
                        .build();
    }
    위 job은 3개의 step instance로 구성됨

# Restartability
    특정 JobInstance에 JobExecution 이 이미 있는 경우 job의 실행은 restart로 인식된다. setRestartable를 통해 restart를 막을 수도 있다.

    Job job = new SimpleJob();
    job.setRestartable(false);

    JobParameters jobParameters = new JobParameters();

    JobExecution firstExecution = jobRepository.createJobExecution(job, jobParameters);
    jobRepository.saveOrUpdate(firstExecution);

    try {
        jobRepository.createJobExecution(job, jobParameters);
        fail();
    }
    catch (JobRestartException e) {
        // expected
    }

    이렇게 하면 이미 실행됐던 job이 재시작될 경우 JobRestartException로 보낸다.

# 성공과 실패
    job의 성공과 실패 결과를 얻을 수 있음
    public void afterJob(JobExecution jobExecution){
        if (jobExecution.getStatus() == BatchStatus.COMPLETED ) {
            //job success
        }
        else if (jobExecution.getStatus() == BatchStatus.FAILED) {
            //job failure
        }
    }

# JobParametersValidator
    매겨변수에 대한 유효성 검사
    매개변수를 사용하여 작업이 시작됨을 확인해야 하는 경우에 사용
    
    @Bean
    public Job job1() {
        return this.jobBuilderFactory.get("job1")
                        .validator(parametersValidator())
                        ...
                        .build();
    }