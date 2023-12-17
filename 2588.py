a = int(input())
b = input()
b1,b2,b3 = map(int, list(b))

re1 = a*b3
re2 = a*b2
re3 = a*b1

result = re1 + re2*10 + re3*100

print(re1)
print(re2)
print(re3)
print(result)