# Napisz program który zamieni cyfry na formę obrazkową

digit = (
"""
 *
* * 
* *
 * 
""",
"""
  *
 **
* *
  *
""",
"""
***
 *
*
***
""",
"""
***
  *
***
***  
""",
"""
  *
 **
***
  * 
""",
"""
***
* *
  *
***
""",
"""
***
*
***
***
""",
"""
***
  *
 *
*
""",
"""
***
***
***
***
""",
"""
***
***
***
  *
"""
)

choose = int(input("Wprowadź dowolną cyfrę: "))
if choose == 0:
    print(digit[0])
elif choose == 1:
    print(digit[1])
elif choose == 2:
    print(digit[2])
elif choose == 3:
    print(digit[3])
elif choose == 4:
    print(digit[4])
elif choose == 5:
    print(digit[5])
elif choose == 6:
    print(digit[6])
elif choose == 7:
    print(digit[7])
elif choose == 8:
    print(digit[8])
elif choose == 9:
    print(digit[9])
else:
    print("Nieprawidłowy wybór")