#Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli romb o wysokości 2X, np.:

#>? 2
# /\
#/  \
#\  /
# \/

num = int(input("Podaj jakąś liczbę X: "))
#przy zalożeniu że podajemy num = 4
#wtedy
# linia[3] = ["/", " ", " ", " ", " ", " ", " ", "\"]
#   /\
#  /  \
# /    \
#/      \        a[0] = "/", a[1:7]= " ", a[7]="\"
rows = int(input("Enter The Number Of Rows: "))
columns = 2 * rows - 1
i = 0
while i < rows:
    j = 0
    while j < columns:
        if ((columns // 2) - i <= j <= (columns // 2) + i):
            print("*", end="")
        else:
            print(" ", end="")

        j += 1
    print(" ")
    i += 1

i = 0
while i < rows:
    j = 0
    while j < columns:
        if (i <= j <= columns - 1 - i):
            print("*", end="")
        else:
            print(" ", end="")

        j += 1
    print(" ")
    i += 1