arr=[10,20,30,40,50,60]
r=2
j=0
temparr=[]
for i in range(r):
    temparr.append(arr[i])
for i in range(0,len(arr)-r,1):
    arr[i]=arr[i+r]
for i in range (len(arr)-r,len(arr),1):
    arr[i]=temparr[j]
    j+=1
print(arr)
    
