# a jest słownikiem, jesli podamy print(a['waga'] to zwróci spod tego wartość,
# to nie dziala jak lista więc zawsze będzie ta sama wartość pod wagą czyli ostatnia wartość d['waga'] = 5

a = {'imie': 'Adam', 'waga': 2}
b = a
b['waga'] = 3
c = a
c['waga'] = 4
d = a
d['waga'] = 5

print(a['waga'])	#5 bo d['waga'] = 5
osoby = [a, b, c, d]	#wszędzie taka sama wartość bo odnosi się do słownika
print(a['waga'])	#5 bo d['waga'] = 5
s = 0
for o in osoby:
	s = s + o['waga']
print(s)



