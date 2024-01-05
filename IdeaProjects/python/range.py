
for i in range(10):
    print(i)

for j in range(5, 10):
    print(j)

for k in range(5, 10, 2):
    print(k)

count = 0
num = 100
for i in range(1, num):
    if i % 2 == 0:
        count += 1
        print(f"{i}是偶数")

print(f"此次循环中有{count}个偶数")
