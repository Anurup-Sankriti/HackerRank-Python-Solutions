if __name__ == '__main__':
    s = input()
    count = 0
    
    for i in range(len(s)):
        if s[i].isalnum() == True:
            count += 1 
    if count > 0: print(True)
    else: print(False)
    count = 0
    
    for i in range(len(s)):
        if s[i].isalpha() == True:
            count += 1 
    if count > 0: print(True)
    else: print(False)
    count = 0
    
    for i in range(len(s)):
        if s[i].isdigit() == True:
            count += 1 
    if count > 0: print(True)
    else: print(False) 
    count = 0
    for i in range(len(s)):
        if s[i].islower() == True:
            count += 1 
    if count > 0: print(True)
    else: print(False) 
    count = 0
    for i in range(len(s)):
        if s[i].isupper() == True:
            count += 1 
    if count > 0: print(True)
    else: print(False) 
