num = int(input("Enter a number:"))
i = 1
while i <= num:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
