a = int(input())

for i in range(1, a+1):
    print(("*" * i).rjust(a))
    
for k in range(a-1, 0, -1):
    print(("*" * k).rjust(a))
    