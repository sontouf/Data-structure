# Tree

- 트리(tree) : 연결된 객체 간의 계층 관계를 나타내는 자료구조
- 트리는 사이클이 없는 그래프의 일종이다.
  - 사이클이 없는 연결그래프
  - 혹은 사이클이 없는 방향 그래프(DAG : Directed Acylic Graph)에 속한다.

## 트리와 관련된 용어들

![tree](https://user-images.githubusercontent.com/57662010/165738533-62e5ab9a-8dbc-403f-9654-7a43d3de49a3.jpg)

- 노드(node) : 트리의 구성요소이다.
- 간선(edge) : 노드를 연결한다.
- 루트(root) : 부모가 없는 노드이다.
  - 여기서는 `A`이다
- 서브트리(sub tree) : 하나의 노드와 그 노드의 자손들로 이루어진다.
  - `A` 의 서브트리는 총 3개로, `{B, E, F}, {C, G, H}, {D}`이다.
  - `B`의 서브트리는 총 2개로, `{E}, {F}` 이다.
- 단말 노드(terminal 혹은 leaf) : 자식이 없는 노드이다. 리프 노드라고도 한다.
  - 여기서는 `E, F, H, D`  이다.
- 내부 노드(internal) : 자식이 있는 노드이다. 비단말 노드라고도 한다.
  - 여기서는 `A, B, C, G`이다
- 형제(sibling) : 같은 부모를 가지는 노드들을 뜻한다.
  - `E`의 형제는 `F`이다.
- 노드의 레벨(level) : 트리에서 각 층의 번호이다.
  - 루트 노드의 레벨을 `0`이라 한다면, 노드의 레벨은 루트부터 해당 노드 사이의 간선의 개수와 같다.
    - 루트 `A` 의 레벨은 0, `B, C, D` 의 레벨은 1, `H`의 레벨은 3
- 트리의 높이 (height) : 트리의 최대 레벨이다.
  - 루트노드의 레벨이 0이면 여기서 `H`의 레벨은 3이다.
- 노드의 차수(degree) : 하나의 노드가 가지는 자식 노드의 개수이다.
  - 노드 `B`의 차수는 2이다.
- 포레스트(forest) : 트리의 집합이다.



## 트리의 특징

1. 트리는 `노드`와 `간선`으로 이루어져 있다.

2. 트리의 노드들은 `부모 - 자식` 이라는 계층 관계를 가진다.

   > 하나의 노드는 부모로서 0개 이상의 자식을 가질 수 있다.
   >
   > 하나의 노드는 루트를 제외하면 1개의 부모를 가진다.

3. 트리는 1개의 `루트` 노드와 `서브트리`들로 이루어져 있다.

4. 트리의 노드가 `n`개라면, 간선은 `n-1`개 이다.

## 트리의 종류

### 이진트리

`이진트리(binary tree)` 는 모든 노드의 최대 차수가 `2`인 트리이다.

- 높이가 `k (k >= 0)`이면, 최소 `k+1` 개의 노드와 최대 `2^(k+1) - 1` 개의 노드를 가진다.

![binary tree](https://user-images.githubusercontent.com/57662010/165749631-878aec28-9505-4b5c-961b-b94b3c3ead73.jpg)

> 예를 들어 이진트리의 높이가 2이면 최소 3개의 노드(왼쪽 트리) 와 최대 7개의 노드(오른쪽 트리)를 가진다.



### 이진트리의 종류

![binary tree의 종류](https://user-images.githubusercontent.com/57662010/165751483-67ffb51a-7a92-441f-916d-a388c5a8295f.jpg)

- 포화 이진 트리(perfect binary tree)
  - 주어진 높이에 대하여 최대 개수의 노드를 가진다.
    - 높이가 `k ( k >= 0)`이면 트리의 노드는 `2^(k+1)-1`개 이다.
- 완전 이진 트리(complete binary tree)
  - 노드가 왼쪽에서 오른쪽으로 채워져있다.
  - 마지막 레벨을 제외한 모든 레벨은 꽉 차 있어야 한다. 즉, 레벨이 `i (i >= 0)`이면 해당 레벨은 `2^i`개의 노드를 가진다.
- 편향 이진 트리 (skewed binary tree)
  - 주어진 높이에 대하여 최소 개수의 노드를 가진다.
    - 높이가 `k (k >= 0)`이면 트리의 노드는 `k+1`개이다.
- 정이진 트리(full binary tree)
  - 모든 노드가 자식 노드를 `0`개 또는 `2`개 가진다.



- B-Tree와 B+Tree

  >  B-Tree의 경우 한 노드가 두 개 이상의 자식 노드를 가지며 모든 노드에 데이터를 저장한다.
  >
  > B+Tree는 B-Tree 의 단점을 개선한 것으로, 단말 노드만 데이터를 저장한다. 단말 노드끼리 연결 리스트로 연결되어 있다.

  - B-Tree에 대하여 B+Tree의 장점과 단점은 무엇인가?

    > B+Tree는 단말 노드만 데이터를 저장하므로, 내부 노드가 더 많은 포인터를 저장할 수 있어 트리의 높이가 낮아지고 검색속도를 향상시킬 수 있다. 또한 테이블을 전체 탐색하는 경우 B-Tree는 단말 노드로 이루어진 연결 리스트를 선형 탐색하면 되지만, B+Tree는 모든 노드를 탐색해야 한다.
    >
    > 그래서 B+Tree는 부등호를 사용하여 순차적으로 데이터를 검색해야 하는 경우에 효율적이다. 하지만 B-Tree는 특정 키에 접근하려면 단말 노드까지 접근해야 한다.

## 이진 탐색트리

![binary search tree](https://user-images.githubusercontent.com/57662010/165755172-b7ce41e4-939d-41ea-919b-a02a10f543bc.jpg)

`이진 탐색 트리(binary search tree)`는 다음과 같은 특징을 가진다

- 모든 노드는 서로 다른 값을 가진다.
- 노드 `v`에 대하여, `v`의 자손들은 다음 특징을 만족한다.

> v의 왼쪽 자손 < v < v의 오른쪽 자손

- 정렬된 값들이 삽입될 때 다음과 같은 특징을 가진다.
  - 오름차순으로 노드를 삽입하면 `오른쪽 편향 이진 트리`가 된다.
  - 내림차순으로 노드를 삽입하면 `왼쪽 편향 이진 트리`가 된다.
  - 때문에 이 경우 노드의 탐색이 상당히 비효율적이다.

## 균형 트리와 비균형 트리

- 균형 트리 : `O(logn)` 시간에 삽입과 탐색을 할 수 있을 정도로 균형이 잘 잡힌 트리
  - ex) 레드-블랙 트리, AVL 트리
- 비균형 트리 : 균형 트리가 아닌 트리

## 이진 힙

- `이진 힙(binary heap)` 은 배열로 표현한 완전 이진 트리로, 우선순위 큐를 구현하여 `O(logn)` 의 시간 복잡도로 최대값 또는 최소값에 접근할 수 있도록 고안된 자료구조이다.

## 트라이

- `트라이(trie)`는 문자열 탐색에 사용하는 트리 기반의 자료구조로, 노드는 자신의 키값과 자식 노드의 배열을 프로퍼티로 가진다.

## 트리의 표현 방법

트리의 `인접 배열`과 `인집 리스트`를 사용하여 나타낼 수 있다.

## # 인접 배열

- 일차원 배열을 사용하면 `인덱스`로 `노드`를, `요소`로 `노드의 부모`를 나타낼 수 있다.

  ```
  tree[node] = parent
  ```

- 이차원 배열을 사용하면 이진 트리를 구현할 수 있다.

  - `인덱스`로 `노드`와 `자식의 방향`을, `요소`는 `자식`을 나타낸다.

  ```
  tree[node][0] = left
  tree[node][1] = right
  ```

## # 인접 리스트

- 파이썬의 딕셔너리를 사용하면 `키`는 `노드`를, `값`은 `자식의 리스트`를 나타낼 수 있다.

```python
tree = {}
tree[node] = [left, right]
```

- `collections.defaultdict`를 사용할 수도 있다.

```python
import collections

tree = collections.defaultdict(list)
tree[node].append(left)
tree[node].append(right)
```

## 트리 순회

트리 순회(tree traversals) : `이진 트리`에 대하여, 트리의 노드들을 중복 없이 모두 방문하는 것이다.

### 트리 순회의 종류

트리 순회에는 네가지 방법이 있다.

- 전위 순회(preorder traversal)
- 중위 순회(inorder traversal)
- 후위 순회(postorder traversal)
- 레벨 순회(level traversal)

### 준비

`인접 리스트`로 트리를 구현한다.

```python
tree = {}
tree[node] = [left, right]
```

### 전위 순회

- 전위 순회(preorder traversal) : `루트 -> 왼쪽 자손 -> 오른쪽 자손`

```python
def preorder(node) :
    left, right = tree[node]
    
    print(root)
    print(left)
    print(right)
```

### 중위 순회

- 중위 순회(inorder traversal) : `왼쪽 자손 -> 루트 -> 오른쪽 자손`

```python
def inorder(node) :
    left, right = tree[node]
    
    inorder(left)
    print(root)
    inorder(right)
```

### 후위 순회

- 후위 순회(postorder traversal) : `왼쪽 자손 -> 오른쪽 자손 -> 루트`

```python
def postorder(node) :
    left, right = tree[node]
    
    postorder(left)
    postorder(right)
     print(root)
```

### 레벨 순회

- 레벨 순회(level traversal) :  위에서부터 같은 레벨의 모든 노드를 왼쪽에서 오른쪽으로 방문한다. `BFS` 와 같다.

```python
def level_traversal(node) :
    queue = deque([node])
    
    while queue :
        cur = queue.popleft()
        
        left, right = tree[cur]
        queue.append(left)
        queue.append(right)
```

