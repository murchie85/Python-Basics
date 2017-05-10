magicNumber = 26

#loop thru 100 numbers
for n in range(101):
    if n is magicNumber:
        print(n, ' is the magic number')
        break  # stop looping when we hit magic number
    else:
        print(n) # prints this for every line because magic number loop not entered into