#define idade de maioridade
maioridade = 18

#pergunta e define nome
nome = input('Digite seu nome: ')

#Pede para que insira o primeiro valor, registrando-o em uma variavel
valor_pergunta1 = input('Digite sua idade: ')

#Converte a primeira variavel (valor_pergunta1) em um número inteiro
valor1 = int(valor_pergunta1)

#Verifica se os valores declarados acima são iguais e se um é maior que o outro
if valor1 >= maioridade:
    print(f'Olá {nome}, você é maior de idade')
elif valor1 < maioridade:
    print(f'Olá {nome}, você é menor de idade')
else:
    print(f'erro')