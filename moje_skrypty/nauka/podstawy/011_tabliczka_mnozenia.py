print("     ", end="")                  #printowanie w jednej linii pięciu pustych znaków zakończonych pustym znakiem zamiast znakiem nowej linii
for i in range(10):                     #...dzieki temu ta pętla wykona się w tej samej linii z printem
    print(f"{i:4}", end="")             #printuj i z odstępem 4, a ta pętla też kończy się bez znaku nowej linii więc też wykona się w tej samej

print()                                 #ten zank kończy to co było w jednej linii
print()                                 #a ten powoduje już, że jest pusta linia

for i in range(10):
    print(i, end="    ")                #wyprintowanie pierwszej kolumny 0,1,2,3,4,5,6,7,8,9 ale ponieważ każdy numerek nie kończy się znakiem nowej linii to kolejny print będzie się wykonywał dla każdego numerka w tej samej linii
    for j in range(10):                 #...czyli dla linii 0 wykona się 10 obrotów, dla 1 wykona się 10 obrotów, dla 2 wykona się 10 obrotów
        print(f"{i*j:4}", end="")       #które składają się z 0*0, 0*1, 0*2, 0*3 itd, 1*0, 1*1, 1*2, 1*3 itd, 2*0, 2*1, 2*2, 2*3 itd    i każdy taki obrót w tej samej linii co i
    print()

print()
