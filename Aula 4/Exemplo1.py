import os

os.system('cls')

# profissao = 'administrador'
# localidade = 'São Gonçalo'
# funcionario = 'Funcionário Privado'
# compra = float(input('Informe valor da compra :'))

# if profissao == 'professor' and localidade == 'Rio de Janeiro':
#     print('Desconto')
# else:
#     print('Sem desconto')


# if profissao == 'professor' or localidade == 'Rio de Janeiro':
#     print('Desconto')
# else:
#     print('Sem desconto')    


# if profissao == 'professor' and localidade == 'Rio de Janeiro' or funcionario == 'Funcionário Público' or compra >= 300:
#     print('Desconto')
# else:
#     print('Sem desconto')

# idade = 15

# if not (idade >= 18):
#     print('Menor Idade')
# else:
#     print('Maior Idade')

# luz_acesa = False

# if not luz_acesa:
#     print('Aceso')
# else:
#     print('Apagado')

# n = int(input('Informe um número :'))

# if not (10 <= n <= 50):
#     print('Intervalo')
# else:
#     print('Fora')

resposta = input('Informe o gênero. Sendo "M" para masculino e "F" para feminino :').upper()

if resposta != '':
    genero = resposta[0]
    if genero == 'M':
        print('Masculino')
    elif genero == 'F':
        print('Feminino')
    else:
        print('Esta opção não é válida. Digite novamente')
else:
    print('O campo não pode ficar em branco!')
