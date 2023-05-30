import textwrap

def wrap(string, max_width):
    temp = []
    real_str = []
    final_list = []
    count = 0
    for i in range(len(string)):
        real_str.append(string[i])
    
    for i in range(len(real_str)):
        temp.append(string[i])
        count = count+1
        if count%max_width == 0:
            print_word = ''.join(temp)
            final_list.append(print_word)
            temp = []
    final = ''.join(temp)
    final_list.append(final)
    result = '\n'.join(final_list)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
