def health_calculator(age = 40, apples_ate = 0, cigs_smoked = 0):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked *2)
    print(answer)

browns_data = [30, 2, 1]

health_calculator(browns_data[0], browns_data[1], browns_data[2])
health_calculator(*browns_data)
health_calculator(browns_data[0], cigs_smoked= browns_data[2])
