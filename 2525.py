"""
h,m = map(int, input().split(" "))
s = int(input())
m+=s
while m >= 60:
    m -= 60
    h+=1
if h >= 24:
    h = h % 24

print(h,m)
"""

h,m = map(int, input().split(" "))
s = int(input())

print(h+(m+s)//60, (m+s)%60)