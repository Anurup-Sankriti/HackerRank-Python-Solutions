from collections import Counter
n = int(input())
word = []
ans = []
for i in range (n):
    word.append(input().strip())

my_counter = Counter(word)
print(len(my_counter))

for prod, num in my_counter.items():
    ans.append(str(num))
print(' '.join(ans))
