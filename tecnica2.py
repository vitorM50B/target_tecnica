# sequência fibonacci = cada termo é a soma dos dois anteriores > 1, 1, 2, 3, 5, 8, 13, 21 etc


# parâmetros a,b = números fibonnaci
# enquanto b, n
# calcular fibonacci anterior
def is_fibonacci(n):
    print(f"Checking Fibonacci for {n}...")  # line para debug
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

numero = int(input("Digite um número: "))
print(f"Você digitou: {numero}")  # line p/ debugging

if is_fibonacci(numero):
    print(f"{numero} pertence à sequência Fibonacci.")
else:
    print(f"{numero} não pertence à sequência Fibonacci.")
