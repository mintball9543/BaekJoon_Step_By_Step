h,m = map(int, input().split(" "))
tmep = 0
if m-45 < 0:
    temp = 45-m
    m = 60-temp
    if h == 0:
        h = 23
    else:
        h-=1
else:
    m-=45

print(h,m)