#Napisz program z GUI do obliczania kosztów przejazdy na zadanym dystansie na podstawie spalania samochodu oraz ceny paliwa
#Skorzystaj z modułu tkinter

#spalanie liczone na 100km
#def koszt (dystans, spalanie, cena):
#    koszt = dystans * spalanie/100 * cena
#    return koszt


import tkinter
from tkinter import messagebox

def koszt():
    try:
        val_a = int(a_entry.get())      #dystans
        val_b = int(b_entry.get())      #spalanie
        val_c = int(c_entry.get())      #cena
        razem = val_a * val_b/100 * val_c
        wynik.configure(text=razem)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="dystans")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="spalanie (na 100km)")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

c_label = tkinter.Label(master=root, text="cena")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()

wynik_labl = tkinter.Label(master=root, text="Wynik:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()
submit = tkinter.Button(master=root, text="Policz", command=koszt)
submit.pack()
root.mainloop()