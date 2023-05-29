if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lr = list(arr)
    
    lr.sort(reverse = True)
    
    for i in range(0,len(lr)):
        if lr[i]<lr[0] and lr[i] != lr[0]:
            print(lr[i])
            break
        #break
