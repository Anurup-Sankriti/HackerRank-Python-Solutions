from collections import deque
comm = deque()
ans = deque()
n = int(input())
for i in range(n):
    a = input().split()
    comm.append(a)

for x in comm:
    if x[0] == 'append':
        ans.append(x[1])
    if x[0] == 'pop':
        ans.pop()
    if x[0] == 'popleft':
        ans.popleft()
    if x[0] == 'appendleft':
        ans.appendleft(x[1])
ans1 = ' '.join(ans)
print(ans1)
