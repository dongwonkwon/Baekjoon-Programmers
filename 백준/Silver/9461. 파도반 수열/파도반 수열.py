import sys
input=sys.stdin.readline
T=int(input())
N=[int(input()) for _ in range(T)]
dp=[0]*101
dp[1]=1
dp[2]=1
dp[3]=1
for i in range(4,101):
    dp[i]=dp[i-2]+dp[i-3]

for i in N:
    print(dp[i])