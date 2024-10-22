def gather_info():
    height = float(int(input("What is your height? (inchers or meters) ")))
    weight = float(int(input("What is your weight? (pounds or kilograms) ")))
    system = input("Meteric or imperial units? ").lower().strip()

    return(height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the BMI
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        print(height)
        print(weight)
        print(system)
        bmi = calculate_bmi(weight, height, system)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        break
    else:
        print('Please put in a valid system')
