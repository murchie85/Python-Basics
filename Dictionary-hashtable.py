classmates = {'Mark': 'cool but smells', 'Susan': 'stuckup', 'David': 'thinks he is the best'}

print(classmates)
print(classmates['Susan'])
print(classmates['Mark'])
print(classmates['David'])

# k = key, mark susan etc, v = cool but smells etc
for k, v in classmates.items():
    print(k + ' ' + v)