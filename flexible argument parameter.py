def add_number(*stat):
    total = 0
    for a in stat:
        total += a # basically expands the stats depending on the how many ints
    print(total)

add_number(3)
add_number(6,3,12)
add_number(11,223,1412)