times=int(input())
for i in range(times):
    count=0
    distances=list(map(int,input().split()))
    for d in distances:
        if d > distances[0]:
            count+=1
    print(count)