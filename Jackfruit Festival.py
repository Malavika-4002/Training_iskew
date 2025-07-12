n,d=list(map(int,input().split()))
j=list(map(int,input().split()))
j.sort()
s=0
for i in range(d):
    s+=max(j)
    j.remove(max(j))
print(s)    
    
