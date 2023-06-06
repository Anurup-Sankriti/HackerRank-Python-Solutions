# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(input())
country = []
for j in range(i):
    j = input()
    country.append(j)
country = list(set(country))
print(len(country))
    
