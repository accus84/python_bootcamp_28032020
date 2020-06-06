import tkinter

#bazowy obiekt
root = tkinter.Tk()

#labelki (zmienna a_label może być inna)
a_label = tkinter.Label(master=root, text = "zmienna a")    #poja się teks zmiena a
#pack układa elementy jeden po drugim, po labelce pakujemy
a_label.pack()
#teraz entry czyli wpisywanie coś w okienku (pojawi się pole)
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text = "zmienna a")    #poja się teks zmiena a
b_label.pack()
#b_entry = tkinter.Entry(master=root)
#b_entry.pack()

#to jest na samym końcu
root.mainloop()

print("Po mainloop")            #to się wykona po zamknięciu okienka
