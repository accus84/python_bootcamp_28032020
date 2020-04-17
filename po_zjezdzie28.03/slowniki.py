MLB_team = {
'Colorado' : 'Rockies',
'Boston'   : 'Red Sox',
'Minnesota': 'Twins',
'Milwaukee': 'Brewers',
'Seattle'  : 'Mariners'
}

print(MLB_team['Colorado'])

MLB_team = dict([           # można także zbudowac słowniki przez wbudowaną funkcję dict()
('Colorado', 'Rockies'),
('Boston', 'Red Sox'),
('Minnesota', 'Twins'),
('Milwaukee', 'Brewers'),
('Seattle', 'Mariners')
])

print(MLB_team['Colorado'])

# Słowniki można wyświetlać tak samo jak listy
print(MLB_team)
# Elementów słownika nie można indeksować
# print(MLB_team[0])     wyskoczy błąd
# Indeksuje się je przez wypisanie nazwy słownika
print(MLB_team['Boston'])
# Zmiana elementów słownika
MLB_team['Seattle'] = 'Seahawks'
print(MLB_team)
# Usuwanie elementów słownika
del MLB_team['Seattle']
print(MLB_team)

#Aby słownik działał najpierw trzeba go utworzyć
person = {}
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person['pets'])
print(person['pets']['dog'])