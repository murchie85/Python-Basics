def health_calculator(age, apples_ate, cigs_smokes):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smokes *2)
    print(answer)



health_calculator(adams_data[0], adams_data[1], adams_data[2])

# ***********BETTER WAY***************
adams_data = [32, 30, 2]
susans_data = [22,32,22]
health_calculator(*adams_data)
health_calculator(*susans_data)