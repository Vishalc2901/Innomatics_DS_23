nums = list(map(int, input().split()))
s=[]
for i in range(len(nums)):
    s.append(sum(nums[:i+1]))

for j in s:
    print(j, end=" ")
