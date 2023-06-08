from itertools import permutations
my_list = list(input().split())
word = my_list[0]
word_list = []
for i in word:
    word_list.append(i)
size = int(my_list[1])
#print(word_list, size)
perm = list(permutations(word_list, size))
perm.sort()

for i in perm:
    print(''.join(i))
