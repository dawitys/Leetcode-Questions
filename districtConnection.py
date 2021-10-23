from collections import defaultdict

numbers = int(input())
neighbours = defaultdict(set)
n = input()
nums = [ int(c) for c in n.split(" ")]

for i in range(1,numbers+1):
    for j in range(1,numbers+1):
        if(i!= j and nums[i-1]!=nums[j-1]):
            neighbours[i].add(j)
            neighbours[j].add(i)

roads = set()

def dfs(n):
    if(n == len(nums)):
        roads.add(ne)
    for ne in neighbours[n]:
        if ne not in roads:
            dfs(ne)
            roads.add(ne)
dfs(1)
print(roads)