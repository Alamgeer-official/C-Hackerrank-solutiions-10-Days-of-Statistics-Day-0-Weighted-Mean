n=int(input())
X=list(map(int,input().split()))
W=list(map(int,input().split()))
total=0
for i in range(n):
    total+=X[i]*W[i]

print(round(total/float(sum(W)),1)) 
