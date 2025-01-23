# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# soma = n1+n2
# print(soma)

# birth = int(input("Digite o ano de seu nascimento: "))
# name = input("Digite seu nome: ")
# resultado = 2025 - birth 
# print(f"{name}, você fará {resultado} anos em 2025!")

# num = int(input("Digite um número: "))
# if num%2==0:
#     print("par")
# else:
#     print("impar")

# lista = []
# total = 0
# notas = int(input("Digite quantas notas gostaria de avaliar: "))
# for i in range(notas):
#     lista.append(float(input("Digite a nota: ")))
#     total+=1
# media = sum(lista)
# media = media/total
# if media >= 5:
#     print("Aprovado!")
# elif media >= 2.5:
#     print("Recuperação!")
# else:
#     print("Reprovado!")

# cont = 0
# num = int(input("Digite um número: "))
# while cont<=num:
#     print(cont)
#     cont+=1

# lista = []
# while True:
#     num = int(input("Digite um número: "))
#     if num<0:
#         break
#     else:
#         lista.append(num)
# resultado = max(lista)
# print(f"O maior número digitado foi: {resultado}")

# def inverter_string(string):
#     cont = 0
#     i = 1 
#     lista_normal = list(string)
#     tamanho = len(lista_normal)
#     while cont<tamanho:
#         lista_invertida.append(lista_normal[tamanho-i])
#         lista_normal.remove(lista_normal[tamanho-i])
#         cont+=1
#         i+=1
#     string = ""
#     string = string.join(lista_invertida)
#     print(string)

# lista_invertida = []
# word = input("Digite uma palavra: ")
# inverter_string(word)

# def contar_caracteres(word):
#     frequence = {}
#     lista = list(word)
#     for i in lista:
#         if i in frequence:
#             frequence[i]+=1
#         else:
#             frequence[i]=1
#     return frequence

# word = input("Digite uma palavra: ")
# result = contar_caracteres(word)
# print(result)

# def merge_sort(lista):
#     meio = int(len(lista)/2)
#     esquerda = lista[:meio]
#     direita = lista[meio:]
#     meio = int(len(esquerda)/2)

#     esquerda1 = esquerda[:meio]
#     esquerda2 = esquerda[meio:]
#     dupla_esquerda = sorted(esquerda1+esquerda2)

#     direita1 = direita[:meio]
#     direita2 = direita[meio:]
#     dupla_direita = sorted(direita1+direita2)

#     return sorted(dupla_direita+dupla_esquerda)

# lista = [100,20,300,30,60,80]
# resultado = merge_sort(lista)
# print(lista)
# print(resultado)


# def merge_sort(lista):
#     meio = int(len(lista)/2)
#     esquerda = lista[:meio]
#     direita = lista[meio:]

#     if lista<1:
#         return sorted(lista)
#     else:
#         esquerda = lista[:meio]
#         direita = lista[meio:]
#         merge_sort(lista)

# lista = [100,20,300,30,60,80]
# resultado = merge_sort(lista)
# print(resultado)

# def bubble_sort(lista):
#     for n in range(len(lista) - 1, 0, -1):
#         trocado = False
#         for i in range(n):
#             if lista[i] > lista[i + 1]:
#                 lista[i], lista[i + 1] = lista[i + 1], lista[i]
#                 trocado = True
#         if not trocado:
#             break

# lista = [1,10,23,515,76587,546,12,3,7,856,2345]
# print(f"Lista não ordenada: {lista}")
# bubble_sort(lista)
# print(f"Lista ordenada: {lista}")

def insertion_sort(lista):
    n = len(lista)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        chave = lista[i]
        a = i - 1
        while a >= 0 and chave < lista[a]:
            lista[a + 1] = lista[a]
            a -= 1
        lista[a + 1] = chave
  
lista = [1432, 12341, 112333, 5, 6]
insertion_sort(lista)
print(lista)

