def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
    
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solution(n, costs):
    parent=[0]*(n+1)
    result=0
    # 부모를 자기 자신으로 초기화
    for i in range(1,n+1):
        parent[i]=i
    
    costs.sort(key=lambda x:(x[2],x[0],x[1]))
    for edge in costs:
        a,b,cost = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result+=cost
            
    return result
    
    
    
    