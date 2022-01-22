# Eventcount /Sequencer

- 은행의 번호표와 비슷한 개념
- sequencer
  - 정수형 변수
  - 생성시 0으로 초기화, 감소하지 않음
  - 발생 사건들의 순서 유지
  - ticket() 연산으로만 접근 가능
- ticket(S)
  - 현재까지 ticket()연산이 호출 된 횟수를 반환
  - indivisible operation

### Eventcount

- Eventcount
  - 정수형 변수
  - 생성시 0으로 초기화, 감소하지 않음
  - 특정 사건의 발생 횟수를 기록
  - read(E), advance(E), await(E,v)연산으로만 접근 가능
- read(E)

  - 현재 Eventcount 값 반환

- advance(E)
  - E = E + 1
  - E를 기다리고 있는 프로세스를 깨움
- await(E, v)
  - v는 정수현 변수
  - if(E < v)이면 E에 연결된 큐에 프로세스 전달 및 스케쥴러 호출

### 상호배제 문제 해결

```java
v = ticket(S);
await(E, v);
// critical section
advance(E);
```

- S와 E는 처음에 0으로 초기화 되어 있다.
- `ticket(S)`를 호출하면 v는 0을 받고 S는 1 증가한다.
- await(0, 0)이기 때문에 대기하지 않고 바로 실행한다.
- advance(E)를 통해 E를 1 증가 시키고, E를 기다리고 있는 프로세스를 실행시킨다.
- 기다린 순서대로 실행된다. 랜덤으로 실행되던 semaphore와 다르고 starvation 문제를 해결한다.

### 생산자 소비자 문제

- Pticket, Cticket : sequencer - 번호표 뽑는 것이다.
- In, Out : eventcount - 직원이 순서 됐다고 알람 울려주는 것이다.
- buffer : size N 크기의 buffer
- 생산자 코드

```java
Message msg = new Message();
Int t = ticket(Pticket);
wait(In, t); // ticket wait 연산은 하나의 생산자만 연산을 하도록 하는 것이다.
await(Out, t - N + 1); //buffer의 빈공간이 날때까지 기다리는 것 N - t + Out >= 1 일 때 공간이 생긴다. 즉 Out이 t - N + 1 일 때 까지 기다려야 한다.
buffer[t % N] = msg;
advance(In);
```

- 소비자 코드

```java
Int u = ticket(Cticket);
wait(Out, u);
await(In, u + 1); //buffer의 내용물이 In - u >= 1일 때 있는 것이다.
Message msg = buffer[u % N];
advance(Out);
```
