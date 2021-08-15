prompt = "This is a basic program, No funny buisness !"
prompt += "\nPlease enter your name: "
name = input(prompt)
print("Hello, " + name )
age = input("How old are you ? ")
age=int(age)
if (age >= 60):
	print("You're a senior")
elif (60 > age) and (age >= 40):
	print("You're middle aged")
elif (21 <= age) and (age < 40):
	print("You're an Adult")
elif  (age < 21):
	print("You're a minor")
