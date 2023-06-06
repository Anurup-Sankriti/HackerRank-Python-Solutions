# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input().split()
y = int(size[0])
x = int(size[1])
#print(x, y)

for j in range(y//2):
    print(('.|.'*(j*2+1)).center(x,'-'))
    left_count = j*2+1
    
print(('WELCOME').center(x,'-'))

for i in range(y//2):
    print(('.|.'*left_count).center(x,'-'))
    left_count -= 2
     
