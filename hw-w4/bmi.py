def bmi_result(height, weight):
    BMI = weight / (height*2)
    #print(f"You BMI is {BMI}")

    if BMI <= 18.4:
        return "You are underweight."
    elif BMI <= 22.9:
        return "You are healthy."
    elif BMI <= 24.9:
        return "You are a little over weight."
    elif BMI <= 29.9:
        return "You are over weight level I."
    else:
        return "You are over weight level II."


# bmi_result()
