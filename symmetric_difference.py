
m = int(input())
M = input().split()
n = int(input())
N = input().split()
result = []
#print(M,N)
for i in M:
    if i not in N:
        result.append(int(i))
for i in N:
    if i not in M:
        result.append(int(i))
        result = list(set(result))
result.sort()

#print(result)
for i in result:
    print(i)

