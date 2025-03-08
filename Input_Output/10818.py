import sys

a = int(input())

#nums = list(map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))

#MIN = nums[0]
#MAX = nums[0]

#for i in nums[1:]:
#    if i < MIN:
#        MIN = i
#    elif i > MAX:
#        MAX = i
        
print(min(nums), max(nums))