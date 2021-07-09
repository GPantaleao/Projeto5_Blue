from classes.carrocinha import Carrocinha

def validar_input(opcao_digitada, opcoes_validas, relogio, personagem):
    if opcao_digitada not in opcoes_validas:
        print(' Você pensou que podia fugir digitando uma opção inválida')
        Carrocinha().carrocinha(relogio,personagem)