import sys
k = int(sys.argv[1])
for i in range(1, k + 1):
    print(" " * (k - i) + "#" * (i))