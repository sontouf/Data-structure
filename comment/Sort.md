# Sort Algorithm

`Selection Sort, Bubble Sort, Insertion Sort, Quick Sort, Heap Sort, Merge Sort, Radix Sort`
> 알고리즘 중 효율성에 영향도 많이 받고 상황에 맞는 정렬을 실행할 수 있다면 다른 알고리즘에도 크게 도움이 된다.


### Selection Sort
`O(N*2)`
> 가장 작은 것을 선택해서 앞으로 보내면서 정렬하자!

source code

```
1. 범위 내에 가장 작은 값을 찾고 맨 앞으로 보낸다.

2. 범위를 줄여가며 반복한다.
```

- Worst, Average, Best = O(N*2)

### Bubble Sort
`O(N*2)`
> 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내자
  
source code
   
```
  
```
- Worst, Average, Best = O(N*2)
- 연산을 반복할 떄마다 가장 큰 값이 맨 뒤로 간다.
- 자리를 바꾸는 연산이 더 많아서 실제 수행시간은 선택, 삽입 정렬보다 더 느리게 작동한다.

### Insertion Sort   
`O(N), O(N*2)`
> 데이터를 순서대로 뽑아 적절한 위치를 찾아 삽입하자!

source code
```

```
- Worst, Average = O(N*2)
- Best = O(N)
- 버블, 선택은 무조건 위치를 바꾸지만 삽입은 필요할 때만 위치를 바꾼다. 그래서 연산을 줄일 수 있다.
- 선택된 데이터 앞쪽은 다 정렬되어 있다고 가정하기 때문에 빠르게 작동할 수 있다.
- 어느정도 정렬되어 있는 경우 퀵 정렬보다도 빠르다.

### Quick Sort
`O(NlogN), O(N*2)`
> pivot을 기준으로 좌우로 정렬하자.

source code
```
1. 피벗을 기준으로 왼쪽을 작은 값, 오른쪽을 큰 값으로 배치한다.

2. 더 이상 집합을 나눌 수 없을 때까지 재귀적으로 실행된다.
``` 
- Best, Average = O(NlogN)
- Worst = O(N*2)
- 대표적인 빠른 정렬 알고리즘. 분할 정복 하는 알고리즘이다. 
- 재귀호출을 한다.
- 이미 정렬이 되어 있는 경우에는 분할 정복의 이점이 없어지고 의미없는 연산을 한다.

