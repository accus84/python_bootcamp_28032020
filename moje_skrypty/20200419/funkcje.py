#wywołanie funkcji
#ta funkcja domyślnie nic nie zwraca, bo po print jest return None
def przywitanie():
    print("Hello world!")

przywitanie()

#funkcja z parametrem (argumentem)
def przywitanie(name):
    text = f"Hello {name}"
    print(text)
    return text

przywitanie("Artur")

#funkcja z parametrem domyślnym

def przywitanie(name = "Alan"):
    text = f"Hello {name}"
    print(text)
    return text
#teraz nie trzeba wstawiać parametru
przywitanie()
