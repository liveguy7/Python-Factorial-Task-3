
def factorial(n):
  product = 1
  for i in range(n):
    product = product * (i+1)
  return product

u = input("Enter a value to find the Factorial of: ")
input = int(u)
fact = factorial(input)
print(fact)

