## 메서드란?

- 문장들을 묶어놓은 것.

```java
static void printArr(int[] numArr){
    for(int i = 0; i < 10; i++){
        System.out.printf("%d", numArr[i]);
    }
    System.out.println();
}
```

- 중복되는 로직을 메서드로 묶어 중복을 제거할 수 있다.
- 값(입력)을 받아서 처리하고, 결과를 반환(출력)

```java
int add(int x, int y){
    return x + y;
}
```

- 반환타입은 int, 메서드 이름은 add, 매개변수는 x, y이다.
- 클래스 안에 있는 함수를 메서드라 한다. 함수는 클래스 독립적이다.

## 메서드의 장점

- 코드의 중복을 줄일 수 있다.
- 코드의 관리가 쉽다. -> 여러 곳에서 사용하던 로직을 메서드로 만들면 메서드만 관리하면 된다.
- 코드를 재사용할 수 있다.
- 코드가 간결해서 이해하기 쉬워진다.

## 메서드의 작성

- 반복적으로 수행되는 여러 문장을 메서드로 작성
- 하나의 메서드는 한 가지 기능만 수행하도록 작성

  ### 지역변수

  - 지역변수(lv) : 메서드 내에 선언된 변수
    ```java
    int add(int x, int y){
        int result = x + y;
        return result;
    }
    int multiply(int x, int y){
        int result = x * y;
        return result;
    }
    ```
  - x, y, result는 모두 지역변수이다.
  - add와 multiply 메서드는 각각 x, y, result라는 지역변수를 가진다.

## 메서드의 호출

- 메서드이름(값1, 값2, ...) 방식으로 호출한다.
- void는 return할 게 없을 때 사용한다.

```java
class Ex6{
    public static void main(String args[]){
        MyMath mm = new MyMath();
        long result1 = mm.add(5L, 3L); //8이 들어간다.
    }
}

class MyMath{
    long add(long a, long b){
        return a + b;
    }
}
```

- add의 파라미터로 5, 3을 넣어줘도 괜찮다.
- 메서드는 return 이후에 실행중인 메서드를 종료하고 호출한 곳으로 되돌아간다.
- 반환타입이 void 이면 return문을 생략할 수 있다. void가 아니면 반드시 반환타입으로 값을 return 해줘야 한다.

```java
int max(int a, int b){
    if(a > b) return a;
}
```

- 위와 같은 예제는 b가 더 클 때 return 문이 없는 것과 마찬가지이다. 그러므로 에러가 난다. 아래와 같이 바꿔줘야 한다.

```java
int max(int a, int b){
    if(a > b) return a;
    else return b;
}
```

- 반환타입이 int일 때 int로 자동형변환 될 수 있는 타입들(char, byte, short)도 return 할 수 있다.
