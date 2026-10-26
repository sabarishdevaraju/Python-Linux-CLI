
import sys

args = sys.argv[1]
final = 0
for i in args:
    if i == "L":
        final = final -1
    elif i == "R":
        final = final + 1
    elif i == "T":
        final = 0

print(final)
    