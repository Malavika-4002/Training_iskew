n=int(input())

day=list(map(int,input().split()))

night=list(map(int,input().split()))
x=int(input())
night.sort(reverse=True)


r=0
for i in range(n):
    t=day[i]+night[i]
    if t>x:
        r+=(t-x)*100

print(r)    
