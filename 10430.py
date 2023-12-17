a,b,c = map(int, input().split(" "))

if not a < 2 or c >10000:
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)