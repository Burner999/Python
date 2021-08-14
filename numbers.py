print(range(10))
print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,2)))
for seq in range(10):
	print(seq)

squares1 = [value **2 for value in range(1,10)]
squares2 = [value **2 for value in range(1,10,2)]
squares3 = [value **2 for value in range(0,10,2)]
squares4 = [value **2 for value in range(2,10,2)]
print(squares1)
print(squares2)
print(squares3)
print(squares4)

for numbers in range(1,20):
	print(numbers)

print(list(range(1,1000001)))
print(min(list(range(1,1000001))))
print(max(list(range(1,1000001))))
print(sum(list(range(1,1000001))))

odd_numbers = [odd + 2 for odd in range(-1,19,2)]
print(odd_numbers)

odd_range = list(range(1,20,2))
odd_numbers = 0
odd_gen = []
for odd in odd_range:
	odd_gen.append(odd)
	odd_numbers = odd_numbers + odd
	print(odd_numbers)

print(list(odd_gen))

mult3 = []
for val in range(3,31):
	mod3 = val % 3
	if mod3 == 0:
		mult3.append(val)
		val + 1
	if mod3 != 0:
		val +1
print(list(mult3))

#cube = []
cube = range(1,11)
for i in range(0,(len(cube))):
	cube_val = (cube[i] **3)
	print("cube of " + str(cube[i]) + " is " + str(cube_val))

cube = [cube_val **3 for cube_val in range(1,11)]
print(cube)
print(cube[0:5])
print(cube[5:10])
print(cube[:10])
print(cube[:5])
print(cube[5:])
print(cube[:5] + cube[5:])
print(cube[-5:])
print(cube[-10:])