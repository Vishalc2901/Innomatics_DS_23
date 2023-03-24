candies = list(map(int, input().split()))
extraCandies = int(input())

res = []
m = max(candies)
for i in candies:
    n = extraCandies + i

    if (n < m):
        res.append(False) 
        
    else:
        res.append(True)
            
print(res)