from collections import namedtuple
N = int(input())
colm_names = input().split()
student = namedtuple('Student',colm_names)
students = []
for i in range(N):
    students.append(student(*input().split()))
print (sum(list(map(lambda x: float(x.MARKS),students)))/len(students))
