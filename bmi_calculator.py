Name = (input("What is your name?\n"))
print (Name)
question1 = int (input("How much do you weight in kg?\n"))
print (question1)
question2 = float (input("How tall are you in m?\n"))
print (question2)
bmi = question1 / question2 ** 2 
bmi_final = round(bmi, 1)
if bmi_final < 18.5:
    print(f"Your BMI is {bmi_final}, you are underweight.")
elif bmi_final <25:
    print(f"Your BMI is {bmi_final}, you have a normal weight.")
elif bmi_final <30:
    print(f"Your BMI is {bmi_final}, you are slighlty overweight.")
elif bmi_final <35:
    print(f"Your BMI is {bmi_final}, you are obese.")
else:
    print (f"Your BMI is {bmi_final}, you are clinically obese.")      



