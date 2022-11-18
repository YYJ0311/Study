# 리소스를 중심으로 API 설계
    클라이언트 내부 구조를 주소로 사용하지 않는다
        https://adventure-works.com/orders // Good
        https://adventure-works.com/create-order // Avoid

    요청을 최소화한다
        모든 웹 요청은 서버에 부하를 주기 때문에 많은 수의 작은 리소스(경로)를 보여주는 주소를 작성하는 것은 안 좋다.

https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design