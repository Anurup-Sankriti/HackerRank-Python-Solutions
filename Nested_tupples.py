if __name__ == '__main__':
    lr = []
    marks =[]
    names = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        a = [name,score]
        lr.append(a) 
    
    for i in range (0,len(lr)):
        marks.append(lr[i][1])
    marks = sorted(marks)
    
    for i in range(1,len(marks)):
        if marks[i] != marks[0]:
           sec_low = marks[i]
           break
    
    for i in range(0,len(lr)):
        if lr[i][1] == sec_low:
            names.append(lr[i][0])
    names = sorted(names)
    for i in range(0, len(names)):
        print(names[i])
