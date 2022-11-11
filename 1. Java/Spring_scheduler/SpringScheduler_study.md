# 방법 2가지
    1. 어노테이션으로 간단하게 제어
    2. xml로 핸들링

# 사용
    내장되어 있는 spring task 기능을 사용해서 scheduler를 구현한다.

# 설정
    1. 스키마
    task schema를 dispatcher-servlet.xml에서 작업함
    beans 아래에 다음 추가
        xmlns:task="http://www.springframework.org/schema/task"
        xsi:schemaLocation=
        http://www.springframework.org/schema/task http://www.springframework.org/schema/task/spring-task.xsd"
        <task:annotation-driven />