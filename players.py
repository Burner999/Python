all_players = ['Adam' , 'Omar' , 'Risa' , 'Zoya' , 'Kate']
print("First 3 names are:")
print("------------------")
for name in all_players[:3]:
	print(name)

print("\nNew players are:")
print("----------------")	
for name in all_players[-2:]:
	print(name)

print("\nAll players are:")
print("----------------")
for name in all_players[:(len(all_players))]:
	print(name)

old_players = all_players[:2]
print("\nOld players are:")
print("----------------")
for name in old_players[-2:]:
	print(name)
