# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
for i in range(0,n):
    try:
        a = input().split()
        print(int(a[0])//int(a[1]))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
