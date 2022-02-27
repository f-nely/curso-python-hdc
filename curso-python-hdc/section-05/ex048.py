livros = {'Vidas Secas': 58, 'Capão do Pecado': 122, 'O Quinze': 114}

print(livros)
print(livros['Vidas Secas'])

for nome_livro, qtd_paginas in livros.items():
    print(f'O livro {nome_livro} tem {qtd_paginas} páginas.')
