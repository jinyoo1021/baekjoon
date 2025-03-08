a = int(input())

for i in range(a, 0, -1):
    print(" "*(a-i) + ("*" * (2*i-1)))
for k in range(2, a+1):
    print(" "*(a-k) + ("*" * (2*k-1)))