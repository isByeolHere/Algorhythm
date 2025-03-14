a, b = input().split()
a = int(a)
b = int(b)

assert a >= 1, "a는 1 이상이어야 합니다."
assert b <= 10000, "b는 10,000 이하이어야 합니다."

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)