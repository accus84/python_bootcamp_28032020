#używane do argumentów
def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

#używane do keywords argumentów
def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

# parametr defaultowy
def my_function(country = "Norway"):
  print("I am from " + country)

my_function()
my_function("Sweden")
my_function("India")
my_function("Brazil")

# przekazywanie argumentów przez listę
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# zwracanie wartości przez return
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# komunikat pass - używane jeśli z jakiegoś powodu funckcja jest bez zawartości
def myfunction():
  pass

# rekurencja - wywoływanie funkcji w funkcji
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    # rekurencja zmniejsza za każdym razem k o 1
    # result = 3 + tri_recursion(3 - 1) = 3 + 3 = 6
    # result = 2 + tri_recursion(2 - 1) = 2 + 1 = 3
    # result = 1 + tri_recursion(1 - 1) = 1 + 0 = 1
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)

