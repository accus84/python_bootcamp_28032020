#Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli romb o wysokości 2X, np 2x
tablica = [" ", "/", "\\"]



#/\
#\/

# /\
#/  \
#\  /
# \/

n = 4
print(sep=" ",end=" ")
for i in range(n):

    for j in range(1,int((n/2))-i+3):
        print(sep=" ",end=" ")

    for k in range(1,i+2):

        print("*", end=" ")

    #print()

