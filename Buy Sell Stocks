n=int(input())
stock=list(map(int,input().split()))
l=len(stock)
i=0
max_profit=0
for i in range(l-1):
    max_val=max(stock[i+1:l])
    
    profit=max_val-stock[i]
    if profit>max_profit:
        max_profit=profit
print(max_profit)        
