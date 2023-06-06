from collections import defaultdict
A = []
B = []
pos = []
size = input().split()
for i in range(int(size[0])):
    a = input()
    A.append(a)
for i in range(int(size[1])):
    a = input()
    B.append(a)
for j in B:
    if j not in A:
        print('-1')
    else:
        for i in range(len(A)):
            if j==A[i]:
                pos.append(str(i+1))
        printable = ' '.join(pos)
        print(printable)
        pos = []
