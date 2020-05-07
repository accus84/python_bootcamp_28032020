#Napisz program który wyświetli teskt w dwóch liniach i zamieni litery

text = "HELLO STRANGER!"

i = 1
first = []
second = []
#text = text.replace(" ", "")
for letter in text:
    if i % 2 == 0:
        second.append(letter)   #do second trafia parzysty element
    else:
        first.append(letter)    #do first trafia nieparzysty element
    i += 1

if " " in first:                #jeśli w pierwszej liście jest pusty znak
    first.remove(" ")           #to usuń
if " " in second:               #jeśli w drugiej liście jest pusty znak
    second.remove(" ")          #to usuń

first_text = " ".join(first)    #łączenie wszystkich elementów odzielone pustym znakiem
second_text = " ".join(second)  #łączenie wszystkich elementów odzielone pustym znakiem

print(first_text)
print(second_text)

assert first_text == "H L O S R N E !"
assert second_text == "E L T A G R"
