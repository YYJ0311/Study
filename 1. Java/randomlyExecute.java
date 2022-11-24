...
if(new Random().nextBoolean()) { // 
    throw new RuntimeException("throw exception");
}
...

// Random().nextBoolean() : 랜덤하게 True / False 를 반환한다.
// 따라서 그 다음에 오는 코드를 랜덤하게 실행할 수 있다.