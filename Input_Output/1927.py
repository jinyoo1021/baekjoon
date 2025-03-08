m, d = map(int, input().split())

a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day = 0

for i in range(0, m-1):
    day += a[i]
    
print(b[(day+d)%7])