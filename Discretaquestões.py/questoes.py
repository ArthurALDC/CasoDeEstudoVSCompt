# 1 Questão
def imprimir_naturais(n):
  if n > 0:
      imprimir_naturais(n - 1)
      print(n)

# 2 Questão
def contagem_digitos(n):
  if n < 10:
    return 1 # 1 digito 
  else:
    return 1 + (contagem_digitos(n // 10)) #Vai contar 1 por 1 usando a virgula

# 3 Questão
def maior_elemento(arranjo):
    if len(arranjo) == 0:
         print("Não tem elementos")
         return 
    
    if len(arranjo) == 1:
        return arranjo[0]
    else:
        # Vai cortando a lista até chegar no primeiro indice 
        ultimo_elemento = maior_elemento(arranjo[1:]) #slice a partir do primeiro indice
        if arranjo[0] > ultimo_elemento:
            return arranjo[0]
        else:
            return ultimo_elemento  

# 4 Questão: o MMC pode ser calculado junto com MDC por que ambos tem relação 
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b) # Enquanto resto não for 0 a função será chamada de novo

def mmc(a, b):
    return abs(a * b) // mdc(a, b) # Relação de Euclides

# 5 Questão (Sequencia de Hailstone)
# 1. Começo com um número inteiro positivo como ponto de partida.
# 2. Se o número for par divide por 2
# 3. Se o número for ímpar, multiplique-o por 3 e some 1.
# continuo repetindo até que o número chegue a 1.
def hailstone(n):
    print(n)  # Imprime o número atual
    if n == 1:
        return print("Acabou a sequencia")  
    elif n % 2 == 0:
        return hailstone(n // 2)  #2 
    else:
        return hailstone((3 *n )+ 1)  #3

while True:
    print("Escolha uma opção:")
    print("0 - Encerra")


    questao = int(input("Digite o número da questão: "))
    if questao == 0:
        break

    if questao == 1:
     imprimir_naturais(50)

    elif questao == 2:
        
        n = int(input("Digite um número para contar seus dígitos: "))
        resultado = contagem_digitos(n)
        print(f"O número possui {resultado} dígitos.")
               
    elif questao == 3:
        arranjo = []
        n = int(input("Quantos elementos tem a lista? "))
        for i in range(n):
            elemento = int(input(f"Digite o elemento {i + 1}: "))
            arranjo.append(elemento)
        resultado = maior_elemento(arranjo)
        print(f"O maior elemento é {resultado}")
 
    elif questao == 4:
        num1 = int(input("Digite o primeiro inteiro: "))
        num2 = int(input("Digite o segundo inteiro: "))
        resultado = mmc(num1, num2)
        print(f"O MMC de {num1} e {num2} é {resultado}")
 
    elif questao == 5:
        numero_inicial = int(input("Digite um número inteiro positivo para a Sequência de Hailstone: "))
        print("Sequência de Hailstone:")
        hailstone(numero_inicial)
    else:
        print("Escolha '1', '2', '3', '4' ou '5' ")