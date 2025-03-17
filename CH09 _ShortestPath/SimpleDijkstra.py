import sys
input=sys.stdin.readline
INF = int(1e9)

#노드의 갯수,간선 갯수
n,m=map(int,input().split())
#시작 노드
start=int(input())
#각 노드에 연결되어있는 노드 정보를 담는 리스트
graph_info=[[] for i in range(n+1)] #노드갯수
#방문여부 리스트
visited=[False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

#간선 정보 입력받기
for _ in range(m):
    a,b,value=map(int,input().split()) #a에서 b로 가는 데에 쓰이는 비용 value
    graph_info[a].append((b,value))

#방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환하기
def get_smallest_node():
    min_value=INF
    index=0 #최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]: #최소 거리이고 방문하지 않았다면
                min_value=distance[i]
                index=i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]=True
    
    for j in graph_info[start]:
        distance[j[0]]=j[1]
    
    #시작 노드를 제외하고 전체 n-1개 노드에 대해서 반복
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
                
#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 갈 최단 거리 출력
for i in range(1,n+1):
    #도달 할 수 없는 경우 무한 출력
    if distance[i]==INF:
        print("INFINITY!")
    else:
        print(distance[i])