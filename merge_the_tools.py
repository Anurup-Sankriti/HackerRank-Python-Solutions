def merge_the_tools(string, k):
    # your code goes here
    count = 0
    temp = []
    lr = []
    for i in range(0,len(string)):
        temp.append(string[i])
        count = count+1
        if count%k == 0:
            lr.append(temp)
            temp = []
    
    for i in range(0,len(lr)):
        temp = lr[i]
        my_string = ''.join(temp)
        
        
        unique_chars = []
        seen_chars = set()

        for char in my_string:
            if char not in seen_chars:
                unique_chars.append(char)
                seen_chars.add(char)

        result = "".join(unique_chars)
        print(result)
        unique_chars = []
        seen_chars = set()
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
