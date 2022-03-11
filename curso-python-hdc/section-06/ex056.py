def dados_pessoais(nome, idade, profissao, func):
    return func(nome, idade, profissao)


def exibe_dados(nome, idade, profissao):
    return f'{nome} tem {idade} anos e sua profissão é {profissao}'


print(dados_pessoais('Matheus', 29, 'Programador', exibe_dados))
