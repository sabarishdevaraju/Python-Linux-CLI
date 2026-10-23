
import sys

L = -1
R = 1
T = 0
listitem = sys.argv[1:]
a = "".join(listitem)
final = 0
for i in a:
    if i == "L":
        final = final -1
    elif i == "R":
        final = final + 1
    elif i == "T":
        final = final + 0


print(final)
    