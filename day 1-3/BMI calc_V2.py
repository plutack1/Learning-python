height = float(input("Enter your height in m:\n"))
weight = int(input("Enter your weight in kg:\n"))
bmi_value = round(float(weight/height **2),1)
if bmi_value < 18.5:
    print("your BMI is", bmi_value, ". You are underweight")
elif bmi_value < 25:
    print("your BMI is", bmi_value, ". You have a normal weight")
elif bmi_value < 30:
    print("your BMI is", bmi_value, ". You are overweight")
elif bmi_value < 35:
    print("your BMI is", bmi_value, ". You are obese")
else:
    print("your BMI is", bmi_value, ". You are clinically obese")



