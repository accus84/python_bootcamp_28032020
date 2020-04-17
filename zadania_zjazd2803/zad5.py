# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w ramce z gwiazdek

text = input("Wprowadź tekst: ")
lenght = len(text)

print("*"*lenght + "****")
print("*", text, "*")
print("*"*lenght + "****")