def get_gender(sex='unknown'): # this is default i.e. unknown
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()
get_gender('s')