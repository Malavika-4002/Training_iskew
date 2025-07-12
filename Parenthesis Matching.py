s=input()
stack=[]
l=len(s)
for i in range(l):
    if s[i]=='{':
        stack.append(s[i])
    elif s[i]=='}' and stack!=[]:
        stack.pop()
    else:
        stack.append(s[i])
if stack==[]:
    print("Matching")
else:
    print("Not Matching")
        
        
        
