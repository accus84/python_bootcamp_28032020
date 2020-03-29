#Napisz program zliczający wystąpienie liczb dodatnich i ujemnych w liście
dodatnie = 0
ujemne  = 0
dane = [10, 20, -30, -500, 4, -220]
for i in dane:
    if i >= 0:
        dodatnie += 1
    else:
        ujemne += 1
    i += 1
print(f"W liście jest {dodatnie} liczb dodatnich i {ujemne} liczb ujemnych")
