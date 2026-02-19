def factorial(n):
    if n<=1:
       return 1
    return n * factorial(n-1)
print(factorial(5))
#Otra forma 
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado
print(factorial(5))
def fibonacci(n):#no funciona o se demora bastante con numeros grandes
    if n<=1:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(7))    
