import sys

string = sys.argv[1]

ans = 0

for ch in string: 
    ans += int(ch) - int('0')

print(ans)
