# 리소스를 중심으로 API 설계
    클라이언트 내부 구조를 주소로 사용하지 않는다
        https://adventure-works.com/orders // Good
        https://adventure-works.com/create-order // Avoid

    요청을 최소화한다
        모든 웹 요청은 서버에 부하를 주기 때문에 많은 수의 작은 리소스(경로)를 보여주는 주소를 작성하는 것은 안 좋다.

    동사보다 명사를 사용하자
        [POST] /updateuser/{userId} 또는 [GET] /getusers // BAD
        [PUT] /user/{userId} // Good

    언더바 대신 하이픈을 사용한다
        가독성을 위해 긴 Path를 표현하는 단어는 하이픈으로 구분하는 것이 좋다
        언더바 문자는 폰트에 따라서 가려지거나 숨겨져서 혼란을 야기할 수 있다.
        http://api.example.com/blogs/guy-levin/posts/this_is_my_first_post // BAD
        http://api.example.com/blogs/guy-levin/posts/this-is-my-first-post // GOOD

https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design