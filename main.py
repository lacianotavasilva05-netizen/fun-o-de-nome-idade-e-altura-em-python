nome = input('Qual é o seu nome? ')

# A função input() retorna uma string (texto), então precisamos converter a idade para um número "inteiro" usando o int().
idade = int(input('Quantos anos você tem? '))

# A função input() retorna uma string (texto), então precisamos converter a altura para um número "flutuante"/"decimais ou fracionários" usando o float().
altura = float(input('Qual é a sua altura em metros? '))

print(f'Meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros.')