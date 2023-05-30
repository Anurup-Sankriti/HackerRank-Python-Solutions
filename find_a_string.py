def count_substring(string, sub_string):
    count = 0
    temp = []
    temp_list = []
    length = len(sub_string)
    
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if i+length-1<len(string):
                
                for j in range(i,i+length):
                    temp.append(string[j])
                word = ''.join(temp)
                temp_list.append(word)
                temp = []
    for i in range(len(temp_list)):
        if temp_list[i] == sub_string:
            count += 1
                
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
