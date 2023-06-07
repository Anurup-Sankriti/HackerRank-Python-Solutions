import math
degree_symbol = '\u00b0'
ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 + bc**2)
ans = math.degrees(math.atan(ab/bc))
print(str(round(ans))+degree_symbol)
