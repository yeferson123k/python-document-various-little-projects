def BMI():
	weight = float(input("Enter your weight in kg: "))
	height = float(input("Enter your height in cm: "))

	BMI = weight / (height/100)**2

	print(f"Your BMI is {BMI}")

	if BMI <= 18.4:
		print("You are underweight")
	elif BMI <= 24.9:
		print("You are Healthy")
	elif BMI <= 29.9:
		print("You are overweight")
	elif BMI <= 34.9:
		print("You are severely overweight")
	elif BMI <= 39.9:
		print("You are obese")
	else:
		print("You are severly obese")
	return BMI

BMI()


