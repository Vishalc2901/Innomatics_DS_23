nums = list(map(int, input().split()))
n = int(input())

x = nums[:n]
y = nums[n:]
sol = []
for i in range(n):
    sol.append(x[i])
    sol.append(y[i])

print(sol)

# for j in sol:
#     print(j, end=" ")