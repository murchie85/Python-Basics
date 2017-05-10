numbersTaken = [2, 5, 12, 33, 17]

print('here are the numbers still available')

for n in range (1, 20): # 1 t0 19
    if n in numbersTaken:
        continue #skip the line after
    print(n)

    