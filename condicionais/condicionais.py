#if aninhado:
idade = 18
nome = "Bob"
if idade > 17:
    if nome == "Bob":
        print ("Ok Bob, you can go.")
    else:
        print("Sorry, you cant go.")

idade = 13
nome = "Bob"
if (idade >=13) and (nome =="Bob"):
    print("ok Bob, you can go")
    
idade = 12
nome = "Bob"
if (idade >=13) or (nome =="Bob"):
    print("ok Bob, you can go")
    

#elif:
dia = "Terça"
if dia =="Segunda":
    print("Hoje fará sol!")
elif dia =="Terça":
    print ("Hoje vai chover!")
else:
    print ("Sem previsão do tempo.")


    
#operadores lógicos:

#usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input ('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) !=1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, você precisa estudar mais.')


#Loop For
#Criando uma tupla e imprimindo cada um dos valores

tupla = (2,3,4)
for i in tupla:
    print(i)
    
    
    
#imprimindo os valores em intervalos (exclusive):
for contar in range(0,5):
    print(contar)


#imprimindo os valores pares (exclusive):
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 ==0:
        print (num)


#Listar números de um intervalo entre 0 e 101, com incremento em 2
for i in range(0,101,2):
    print(i)
    
for caracter in "Python é linda!":
    print (caracter)
    
    
    
    
#Loops Aninhados
for i in range(0,5): #para cada item dessa seleção, executar:
    for a in range(0,5): #executar isso
        print(a)



#Valores em lista com o loop for
lista1 = [32,53,85,10,15,17,19]
soma = 0
for i in lista1: #a cada item da lista, fazer 2 ações:
    double_i = i * 2 #multiplicar por 2 cada item dqa lista e gravar na variável.
    soma += double_i #variável soma será adicionada à variável double_i e armazenada em soma
    
print(soma)

#Contar os itens de uma lista
lista = [5,6,10,13,17]
count = 0
for item in lista:
    count += 1
print(count)


#Contar o número de colunas
lst = [[1,2,3], [3,4,5], [5,6,7]]
primeira_linha = lst [0]
count = 0
for column in primeira_linha:
    count = count + 1

print(count)


#Pesquisar em listas
listaA = [5,6,7,10,50]
for item in listaA: #loop através da lista
    if item ==5:
        print("Número encontrado na lista.")


#Listar as chaves de um dicionário
dict = {'k1':'Python', 'k2':'R', 'k3':'Scala'}
for item in dict:
    print(item) #o item aqui no caso é a chave
    
    
for k,v in dict.items(): #imprimir chave e valor do dicionário
    print (k,v)
    
    



#Loop While ( sempre verificar uma forma para que a condição deixe de ser verdadeira e saia do loop)

#imprimir os valores de 0 a 9
counter = 0
while counter < 10:
    print (counter)
    counter = counter + 1 #esta linha faz com que a instrução acima deixe de ser verdadeira




#tbm é possível usar a cláusula else para encerrar o loop while
x= 0

while x < 10: # enquanto esta < condição for verdadeira, executar as duas linhas abaixo.
    print ('O valor de x nesta iteração é: ', x)
    print (' x ainda é menor que 10, somando 1 a x')
    x+= 1
    
else:
    print ('Loop concluído!')






#pass, break , continue
counter = 0
while counter < 100:
    if counter == 25:
        break # para a execução do loop
    else:
        pass
    print(counter)
    counter = counter + 1
    

for verificador in "Python":
    if verificador == "h":
        continue
    print (verificador)


# while e for juntos
for i in range(2,30):
    j = 2
    counter = 0
    while j < i:
      if i % j == 0:
          counter = 1
          j = j + 1
      else:
          j = j + 1
          
    if counter == 0:
          print(str(i) + " é um número primo")
          counter = 0
    else:
          counter = 0
          
          
          

#range
for i in range (50,101,2): # o valor do meio é exclusivo, 100
    print(i)
    
for i in range (0,-20,-2):
    print(i)
    
    
lista = ['morango','banana','abacaxi','uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i]) # i é cada elemento do meu range
    


#TUDO EM PYTHON É UM OBJETO
type(range(0,3))














