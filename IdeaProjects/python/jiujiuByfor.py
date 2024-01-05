i = 1
for i in range(1, 10):
    j = 1
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}\t", end="")
    print()
