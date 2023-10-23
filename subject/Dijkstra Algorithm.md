# Dijkstra Algorithm

- 다익스트라 알고리즘은
  - 단일 시작점 최단 경로 알고리즘이다. 시작 정점에서부터 다른 정점들까지의 최단 거리를 구한다.
  - 그리디 알고리즘에 속한다. 항상 노드 주변의 최단 경로만을 택한다
  - 노드 주변을 탐색할 때 BFS 를 사용한다.



## 다익스트라 알고리즘의 동작

W(u, v)는 u 에서 v 로 가는 경로의 가중치를, D(u)는 시작 정점 s 에서 v로 가는 최단 거리이다. 처음에는 모든 D(u)가 무한대로 초기화된다.

1. 초기화하기 : 시작정점이 s이므로 D(s)는 0으로 초기화한다.
2. 방문할 정점 구하기 : 아직 방문하지 않은 정점 중 D(u)가 가장 짧은 u 를 선택하여 방문한다. ( 최초로는 D(S)가 0으로 가장 작으므로 s 를 방문하게 된다. )
3. 완화하기 : 현재 방문한 정점 u 의 인접 정점 중, 아직 방문하지 않은 정점 v에 대하여 D(u) + W(u, v) 가 D(v) 보다 작다면 D(v)를 D(u) + W(u, v) 로 갱신한다. ( 인접 정점의 최단 거리 정보를 갱신하는 것을 완화한다고 한다.)
4. 방문할 정점이 없을 때까지 2번부터 반복한다.



## 우선순위 큐로 동작하는 다익스트라 알고리즘

우선순위 큐로 최소 힙으로 정점 v에 대하여 최단경로 D(v)를 기준으로 정렬된다.

1. 초기화하기:
   1. 시작 정점이 S이므로 D(S) 를 0으로 초기화한다.
   2. 우선순위 큐 PQ에 (D(S), S) 를 넣는다.
2. 방문할 정점 구하기 : PQ에서 (D(u), u)를 꺼낸다. 최초에 PQ에는 요소가 (D(s), s) 밖에 없으므로, S에 방문하게 된다.
3. 완화하기 : 현재 방문한 정점 u 의 인접 정점 중, 아직 방문하지 않은 정점 v에 대하여 D(u) + W(u, v)가 D(v) 보다 작다면
   1. D(v) 를 D(u) + W(u, v)로 갱신한다.
   2. PQ 에 (D(u) ,u )를 넣는다.
4. PQ 가 빌 때까지 2번부터 반복한다.



## 우선순위 큐로 구현한 다익스트라 알고리즘

- 초기화하기

  ```python
  distance = [INF] * N
  
  distance[start] = 0
  queue: List[Tuple[int, int]] = [(distance[start], start)]
  ```

  - 탐색 전이므로 distances 의 모든 요소를 INF 로 초기화한다.
  - 시작 정점 start 에 대하여, distance[start] 는 0으로 초기화한다.
  - 우선순위 큐에 (D(start), start) 를 넣는다.

- 방문할 정점 구하기

  ```python
  cur_dist, cur = heappop(queue)
  ```

  - 우선 순위 큐에서 cur 과 현재까지 계산한 cur 까지의 최단 경로 cur_dist 를 꺼낸다.

- 완화하기

  ```python
  for nxt, weight in graph[cur].items():
      nxt_dist = cur_dist + weight
      
      if nxt_dist < distances[nxt]
      	distances[nxt] = nxt_dist
          heappush(queue, (nxt_dist, nxt))
          
  ```

  - 현재 방문 정점 cur 의 인접 정점 nxt 에 대하여, cur 부터 nxt 까지의 가중치 weight 를 구한다.
  - cur_dist + weight 가 distance[nxt] 보다 작다면 distance[nxt] 를 갱신한다. 그리고 우선순위 큐에 (distance[nxt] , nxt) 를 넣는다.



```python
# N: 그래프 내 정점의 개수
# INF: 양의 무한대
# graph: 인접 리스트로 구현
# graph = {}
# graph[u] = { v: 가중치 }

def dijkstra(start: int) -> List[int]:
	distances = [INF] * N

	distances[start] = 0
	queue: List[Tuple[int, int]] = [(distances[start], start)]

	while queue:
		cur_dist, cur = heapq.heappop(queue)

		if distances[cur] < cur_dist:
			continue

		for nxt, weight in graph[cur].items():
			nxt_dist = cur_dist + weight

			if nxt_dist < distances[nxt]:
				distances[nxt] = nxt_dist
				heapq.heappush(queue, (nxt_dist, nxt))

	return distances
```

## 다익스트라 알고리즘의 시간 복잡도

정점의 개수를 v , 간선의 개수를 E 라고 하자.

### 우선순위 큐를 사용하지 않은 경우

- 모든 정즘은 한 번씩 방문되므로 모든 간선은 한 번씩 검사된다.  그러므로 O(E)
- 각각의 정점에 대하여 인접 정점이 어떤 정점인지 검사한다. 그러므로 O(v^2)
- 따라서 우선순이 큐를 사용하지 않은 경우 O(V^2 + E)

### 우선순위 큐를 사용한 경우

- 모든 정점은 한 번씩 방문되므로 모든 간선은 한 번씩 검사된다. 그러므로 O(E)

- 최악의 경우 우선순위 큐에는 O(E)만큼 원소가 추가된다. 우선순위 큐에 삽입/삭제하는 연산은 O(logE)이다.

  그러므로 O(E) * O(logE) = O(ElogE)

- 이때 E는 V^2 보다 작으므로, O(logE) = O(logV)라고 할 수 있다.

- 따라서 우선순위 큐를 사용하는 경우 O(E * logV)





## 언제 우선순위 큐를 사용하는 것이 효율적인가?

시간 복잡도에 따라

- 정점의 개수가 많다면 우선순위 큐를 사용한다.
- 간선의 개수가 많다면 우선순위 큐를 사용하지 않는다.



## 다익스트라와 음수 간선이 있는 그래프

다익스트라를 사용한다고 해서 음수 간선이 있는 그래프에 대해 모든 경우 최단 경로를 구하지 못하는 것은 아니다. 다만 항상 최단 경로를 구할 수 있다고 보장하지 못한다.

음수간선이 있는 그래프에 최단경로를 구하고자 한다면 벨만포드알고리즘을 사용하도록 한다

