n = int(input())
for i in range(1,n+1):
    print("*" * i + " " * 2*(n-i) + "*" * i)
for k in range(1, n):
    print("*" * (n-k) + " " * 2*k + "*" * (n-k))