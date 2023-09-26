# Queue
`FIFO`

> 가장 빨리 들어온 데이터가 먼저 나가는 `선입선출`의 구조를 가진다.

## 큐의 연산
- `is_empty()` : 큐이 비어있는지 검사한다.
- `enqueue(queue, data)` : 큐에 요소를 추가한다.
- `dequeue(queue)` : 큐에서 가장 아래에 있는 요소를 꺼내어 반환한다.
- `peak(queue)` : 큐에서 가장 아래에 있는 요소를 (삭제없이) 반환하다.

## 큐의 구현
큐은 `연결리스트`로 구현할 수 있다.

source code
```python
from typing import Optional, TypeVar

T = TypeVar('T')

class ListNode:
    def __init__(self, val: T, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, item: T):
        node = ListNode(item, self.top)
        
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def dequeue(self) -> Optional[T]:
        if self.is_empty():
            return None

        val = self.front.val
        self.front = self.front.next

        return val

    def peek(self) -> Option[T]:
        return None if self.is_empty else self.front.val
```

## 큐의 시간 복잡도
| 연산         | 시간 복잡도 | 설명                                                         |
| ------------ | ----------- | ------------------------------------------------------------ |
| enqueue()    | O(1)        | `front`으로 가장 위에 있는 요소를 가리키므로 상수 시간에 삽입 연산이 가능하다. |
| dequeue()    | O(1)        | `rear`으로 가장 위에 있는 요소를 가리키므로 상수 시간에 삭제 연산이 가능하다. |
| peek()       | O(1)        | `front`으로 가장 위에 있는 가리키므로 상수 시간에 접근할 수 있다. |
| search(item) | O(n)        | 연결 리스트로 구현되었으므로 상수 시간에 요소를 탐색할 수 없다. |

백준 9012번 괄호검사

## 파이썬과 큐

파이썬의 `리스트`는 큐 연산을 지원한다.

| 연산               | 시간복잡도 | 설명                                                         |
| ------------------ | ---------- | ------------------------------------------------------------ |
| append(item)       | O(1)       | 가장 뒤에 요소를 삽입하므로 상수 시간에 삽입 연산이 가능하다. |
| pop(0)             | O(n)       | 삭제된 요소 이후에 있는 요소들을 한 칸씩 앞으로 당겨주어야 한다. |
| queue[0]           | O(1)       | 인덱스로 요소에 접근하므로 가장 에 있는 요소에 상수 시간에 접근할 수 있다. |
| find(i) / index(i) | O(n)       | 배열의 모든 요소를 탐색해야 한다.                            |



## 파이썬과 덱

자료구조 `덱(deque)` 은 front 와 rear 에서 삽입, 삭제 연산이 상수 시간에 가능한 자료구조이다.

파이썬의 collections.deque 으로 큐의 연산을 O(1) 의 시간 복잡도로 사용할 수 있다.

```python
from collections import deque
```



| 연산            | 시간 복잡도 | 설명                                               |
| --------------- | ----------- | -------------------------------------------------- |
| deque.popleft() | O(1)        | 가장 앞에 있는 요소를 상수  시간에 삭제할 수 있다. |

