// db에서 타입이 double이었을 때 가져오면 E로 지수가 표시됨
// 지수표시를 제거하고 숫자 그대로 보여주는 방법
// decimal : 10진법, 소수

// 1. double 타입의 숫자를 가져온 경우
BigDecimal test1 = new BigDecimal(2021061523295E11);
System.out.println(test1); // 202106152329500000518144

// 2. String 타입인 경우 : String -> Double 파싱을 거침
BigDecimal test2 = new BigDecimal(Double.parseDouble("2021061523295E11"));
System.out.println(test2); // 202106152329500000518144

// 2-2. BigDecimal -> String 변환
String str = test2.toString();