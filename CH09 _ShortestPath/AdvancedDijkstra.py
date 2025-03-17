import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split()) #n개 노드 m개 간선
start=int(input()) #시작 노드 입력
graph_info=[[] for i in range(n+1)] #각 노드 정보 담기
distance=[INF]*(n+1) # 최단 거리 테이블 모두 무한으로 초기화

#모든 간선 정보 입력받기
for _ in range(m): 
    a,b,money=map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 money
    graph_info[a].append((b,money))
    
#다익스트라 알고리즘
def dijkstra(start):
    q=[]
    #시작 노드로 가는 최단경로는 0으로 설정하고 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    #큐가 비어있지 않다면
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

#다익스트라 알고리즘 수행
dijkstra(start)
for i in range(1,n+1):
     #도달 할 수 없는 경우 무한 출력
    if distance[i]==INF:
        print("INFINITY!")
    else:
        print(distance[i])