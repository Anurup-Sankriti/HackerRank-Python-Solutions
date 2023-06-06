# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
money = 0
shoe_count = int(input())
shoe_size = input().split()
shoe_counter = Counter(shoe_size)
customer_num = int(input())
for i in range(customer_num):
    buy = input().split()
    for s_size, num_available in shoe_counter.items():
        if buy[0] == s_size:  #check availability of size
            if num_available > 0: #check amount availability
                money+=int(buy[1])
                shoe_counter[s_size] = num_available - 1
print(money)
