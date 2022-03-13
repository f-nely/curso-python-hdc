from random import choice
from palavras import palavras


# selecionando a palavra
def selecionar_palavra():
    palavra = choice(palavras)
    return palavra.upper()


# iniciar o jogo
def jogar(palavra):
    palavra_a_completar = '-' * len(palavra)
    advinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

    # boas vindas ao jogador
    print('Vamos jogar!')
    print(exibir_forca(tentativas))

    print(f'Esta é a palavra: {palavra_a_completar}')

    # enquanto o usuário não adivinhar e ainda houver tentativas
    while not advinhou and tentativas > 0:
        tentativa = str(input('Digite uma palavra ou letra para continuar: ')).upper()

        print(tentativa)


# status do jogo
def exibir_forca(tentativas):
    estagios = [  # Fim de jogo
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,
        # Falta 1 tentativa
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,
        # Faltam 2 tentativas
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,
        # Faltam 3 tentativas
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,
        # Faltam 4 tentativas
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,
        # Faltam 5 tentativas
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,
        # Estado inicial
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]

    return estagios[tentativas]


# iniciação do jogo e continuar jogando
def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)


iniciar()
