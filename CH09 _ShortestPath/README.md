# 간단한 다익스트라 알고리즘

```python
     for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now_short=get_smallest_node() #선형적 탐색색
        visited[now_short]=True

        #현재 노드와 연결된 노드 확인
        for j in graph_info[now_short]:
            money=distance[now_short]+j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 것이 더 짧을 경우 갱신
            if money<distance[j[0]]:
                distance[j[0]]=money
```

- 시간 복잡도 : O(N^2)

# 개선된 다익스트라 알고리즘

- 시간 복잡도:O(ElogV)
- 최소 힙을 이용
- 튜플형식으로 (거리,노드위치) 이렇게 큐에 삽입된다.
- 우선순위 큐 이므로 거리를 기준으로 최소인게 먼저 pop되게 구성되어있음음

```python
  while q:
        #큐 꺼내기
        dist,now=heapq.heappop(q)
        #만약 현재 노드가 처리된 적 있는 노드라면 무시
        if distance[now]<dist: #큐의 비용이 현재노드의 비용보다 크면?
            continue
        #현재 노드와 연결된 인접한 노드 확인
        for i in graph_info[now]:
            cost=dist+i[1]
            #현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧은 경우
            if cost <distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

```
