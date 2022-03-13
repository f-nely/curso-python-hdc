from random import choice
from palavras import palavras


# selecionando a palavra
def selecionar_palavra():
    palavra = choice(palavras)
    return palavra.upper()


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


teste = selecionar_palavra()
print(teste)

teste_estagio = exibir_forca(2)
print(teste_estagio)
