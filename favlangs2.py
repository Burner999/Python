favourite_languages = {
	'jen': ['Python','Ruby'],
	'sarah': ['C','Delphi'],
	'Edward': ['Ruby','C#'],
	'Phil': ['Python','Java'],
	'3abood': ['Niyakeh']
}

for name, languages in favourite_languages.items():
		if len(languages) >1:
			print("\n" + name.title() + "'s favourite languages are:" )
			for language in languages:
				print("\t" + language.title())

		else:
			print("\n" + name.title() + "'s favourite language is:" )
			for language in languages:
				print("\t" + language.title())
		
	
