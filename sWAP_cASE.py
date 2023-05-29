def swap_case(s):
    ans = ""
    for i in range(0,len(s)):
        #print(s[i].upper())
        check_l = s[i].islower()
        #print(type(s[i]))
        if check_l == True:
            a = s[i].upper()
            ans = ans+a
            #print(s[i],'lower')
        else:
            
            b = s[i].lower()
            ans = ans + b
            #print(s[i],'no')
                
    return ans
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
