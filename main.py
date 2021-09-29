
"""

    1 - Defina uma lista vazia para armazenar os itens escolhidos pelo usuário - ok


    2 - Cada item escolhido pelo usuário deverá ser armazenado na lista para
    mostrar o que o usuário pode comer e quanto terá consumido ao final do
    programa - ok


    3 - Crie um loop que será executado até que não seja mais possível
    consumir alimentos (caso o usuário exceda em sua opção o limite diário:
    consumo < 0) envolvendo a exibição do cardápio e a solicitação do código do
    alimento para que o programa continue solicitando os alimentos.

"""

escolhas_usuario = []

opcoes = [
    10,
    7,
    3,
    21,
    77,
    80
    ]

alimentos = [
    'pizza',
    'batata frita',
    'café',
    'refrigerante',
    'feijoada',
    'lasanha'
    ]

calorias = [
    700,
    800,
    50,
    150,
    1300,
    900
    ]

escolhas = zip(opcoes, alimentos, calorias)

consumo = int(input('Digite o limite de consumo de calorias diário: '))

while consumo > 0:

    print('\n','' * 10, 'Esse é seu cardápio! Choose Wisely', '' * 10, '\n') 

    for opcao, alimento, caloria in escolhas:
        print(opcao, ' - ', alimento, ', caloria:', caloria)

    codigo = int(input('\nDigite o código do seu alimento: '))

    if codigo in opcoes:
        idx = opcoes.index(codigo)

        if calorias[idx] <= consumo:
            escolhas_usuario.append(idx)
            print('Sua escolha foi', alimentos[idx], '\nEsse alimento tem:', calorias[idx], 'calorias')
            consumo = consumo - calorias[idx]

            if consumo > 0:
                print('Você ainda pode consumir', consumo, 'calorias')
            
        else:
            print('Oh, você já comeu demais. Não acha não?')
            
    else:
        print('Não temos esse item no cardápio!')


print('acabou')