def merge_the_tools(string, k):
    word_set = []
    pos_set = []
    temp = []
    used = []
    for j in range(k):
        pos_set.append(j)
    
    for i in range(len(string)):
        if i%k==0:
            for j in pos_set:
                temp.append(string[i+j])
            word_set.append(temp)
            temp = []
    for x in word_set:
        temp.append(x[0])
        used.append(x[0])
        for i in range(1,len(x)):
            if x[i] not in used:
                temp.append(x[i])
                used.append(x[i])
        ans = ''.join(temp)
        print(ans)
        used = []
        temp = []
            
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
