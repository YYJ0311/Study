// 제네릭
    // 제네릭은 JDK 1.5에 등장
    
    // 제네릭 등장 이전, 컬렉션의 요소를 출력하는 메소드
void printCollection(Collection c){
    Iterator i = c.Iterator();
    for (k = 0; k < c.size(); k++) {
        System.out.println(i.next());
    }
}
    // 이렇게 사용하면 컬렉션의 요소들을 다루는 메소드들은 "타입이 보장되지 않아서" 다음과 같은 문제가 발생했다.
int sum(Collection c) {
    int sum = 0;
    Iterator i = c.iterator();
    for (k = 0; k < c.size(); k++) {
        sum += Integer.parseInt(i.next());
    }
    return sum;
}
    // 위 메소드는 String 처럼 다른 타입을 갖는 컬렉션도 호출이 가능하다. 컴파일 시점에는 문제가 없지만, 런타임 시점에 메소드를 호출하면 에러가 발생한다.
    // 그래서 타입을 지정하여 컴파일 시점에 안정성을 보장받을 수 있는 "제네릭"이 등장했다.
void sum(Collection<Integer> c) {
    int sum = 0;
    for (Integer e : c) {
        sum += e;
    }
    return sum;
}
    // 안정성을 보장받게 된 이후, 제네릭은 불공변(A는 B의 child이지만, T<A>는 T<B>의 child가 아님)이라서 모든 타입에서 공통적으로 사용되는 메소드를 만들 수 없다는 문제가 발생함.
static void printCollection(Collection<Object> c) {
    for (Object e : c) {
        System.out.println(e);
    }
}

public static void main(String[] args) {
    Collection<String> c = new ArrayList<>();
    c.add("hi");
    printCollection(c); // 컴파일 에러 : Collection<String>이 Conllection<Object>의 child가 아니기 때문
}
// 타입의 제한 때문에 실용성이 떨어지는 상황이 생기면서, 모든 타입을 대신할 수 있는 와일드 카드 타입<?>이 추가됨. 
// 따라서 위 메소드를 다음처럼 사용할 수 있다.
static void printCollection(Collection<? extends Number> c) { // 확장의 상한선을 Number로 정해놓은 상한 경계 와일드카드
    for (Number e : c) {
        System.out.println(e);
    }
}

public static void main(String[] args) {
    Collection<Integer> c = new ArrayList<>();
    c.add(123);
    printCollection(c); // Integer가 Number 클래스의 child 타입이라 사용 가능
}

// 하한 경계 와일드카드
<? super T> // ? 는 T이거나 T보다 부모 객체 타입이어야 함

// 와일드 카드는 any type이 아니라 정해지지 않은 unknown type이다. 이에 대한 문제점도 있는데 나중에 알아보자..