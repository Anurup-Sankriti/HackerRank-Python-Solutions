# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
word = input()
letter = []
ans = []
for i in word:
    letter.append(i)
groups = itertools.groupby(word)
for key, group in groups:
    x = list(group)
    tup = (len(x), int(x[0]))
    ans.append(str(tup))
print(' '.join(ans))
