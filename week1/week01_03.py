import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4 * a * c
if d < 0:
    sys.exit(0)
elif d == 0:
    x1 = x2 = -b / (2 * a * c)
    print(int(x1), int(x2), sep='\n')
else:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print(int(x1), int(x2), sep='\n')