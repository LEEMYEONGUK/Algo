num1, num2 = map(int, input().split())

max_v = 0

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        if max_v < i:
            max_v = i

min_v = num1 * num2 / max_v

print(int(max_v))
print(int(min_v))
