#QUESTAO 1
numero = input("Digite um numero de cinco digitos: ")
if len(numero) == 5 and numero.isdigit():
    
   digitos_separados = "   ".join(numero)
   print(digitos_separados)
else:
   print("Por favor, insira um numero valido de cinco digitos.")

#QUESTAO 2
def calcular_quadrado(n):
    soma = 0
    impar = 1
    for _ in range(n):
        soma += impar
        impar += 2  

    return soma


n = int(input("Digite um numero natural: "))

if n >= 0:
    resultado = calcular_quadrado(n)
    print(f"O quadrado de {n} é {resultado}.")
else:
    print("Por favor, insira um numero natural valido (n >= 0).")

#QUESTAO 3
def suc(n):
    return n + 1

def pred(n):
    return n - 1

def soma_recursiva(a, b):
    if b == 0:
        return a  
    else:
        return soma_recursiva(suc(a), pred(b))  

# Exemplo de uso
a = 5
b = 3
resultado = soma_recursiva(a, b)
print(f"A soma de {a} e {b} é {resultado}.")

#QUESTAO 4

def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        # move o disco diretamente para o destino
        print(f"Mova o disco 1 de {origem} para {destino}.")
    else:
        #  Move n-1 discos de origem para auxiliar
        hanoi(n - 1, origem, auxiliar, destino)
        
        #  Move o maior disco de origem para destino
        print(f"Mova o disco {n} de {origem} para {destino}.")
        
        #  Move n-1 discos de auxiliar para destino
        hanoi(n - 1, auxiliar, destino, origem)

# Exemplo de uso
n = int(input("Digite o número de discos: "))
hanoi(n, 'A', 'C', 'B')  # A: origem, C: destino, B: auxiliar