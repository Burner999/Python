favourite_languages = {
	'jen': 'Python',
	'sarah': 'C',
	'Edward': 'Ruby',
	'Phil': 'Python'
}

friends = { 'jen' , 'Phil'}

print("Keys listing")
print("============\n")
for Name in (favourite_languages.keys()):
	print(Name.title())
print("\n")

print("Values listing")
print("==============\n")
for language in favourite_languages.values():
	print(language.title())
print("\n")

print("Unique Keys listing")
print("===================\n")
for language in set(favourite_languages.values()):
	print(language.title())
print("\n")

print("Sorted Keys listing")
print("===================\n")
for language in sorted(favourite_languages.keys()):
	print(language.title())
print("\n")

print("Unique and Sorted values listing")
print("===============================\n")
for language in set(sorted(favourite_languages.values())):
	print(language.title())
print("\n")

print("Example Keys and values listing")
print("===============================\n")
for Name, favlang in favourite_languages.items():
	print(Name.title() +"'s " + "favourite language is " + favlang + ".")
print("\n")

print("Example Keys and values listing")
print("===============================\n")
for Name in favourite_languages.keys():
	print(Name.title())
	if Name in friends:
		print("Hi " + Name.title() + " !" + " Have you thought of trying Nim instead of " + favourite_languages[Name].title() + "?")
print("\n")

