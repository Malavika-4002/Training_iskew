n=int(input())
l=[]
for i in range(n):
    shows=list(map(int,input().split()))
    l.append(shows)
l.sort(key=lambda x : x[1])
start=l[0][0]
end=l[0][1]
count=1
for s,e in l:
    if s>=end:
        count+=1
        end=e
print(count)        
