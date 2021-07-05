
from auxiliar.funcoes_auxiliares import opcoes_padrao
from random import randint
from classes.carrocinha import Carrocinha
    
def fase1(relogio, personagem):
    print(f'São {str(relogio)}, {personagem.nome}, dia {relogio.dia} acordou num {personagem.lugar}.')
    print(personagem)

    acao1 = int(input(f'''O que {personagem.nome} vai fazer? 

    1- Procurar comida
    2- Procurar alguém para brincar
    3- Procurar um abrigo
    4- Voltar a dormir
    '''))

    while acao1 not in [1,2,3,4]:
        print('Opção inválida.')
        acao1 = int(input(f'''O que {personagem.nome} vai fazer? 

    1- Procurar comida
    2- Procurar alguém para brincar
    3- Procurar um abrigo
    4- Voltar a dormir
    '''))
    opcoes_padrao(relogio, personagem, acao1)
    print(personagem)
    fase2(relogio, personagem, acao1)

def fase2(relogio, personagem, opcao_escolhida1):
    print(f'São {str(relogio)}, {personagem.nome} você está {personagem.lugar}.')
    print(personagem)
    carrocinha = Carrocinha()
    if opcao_escolhida1 != 1:
        print('1- Procurar comida')
    if opcao_escolhida1 != 2:
        print('2- Procurar alguém para brincar')
    if opcao_escolhida1 != 3:
        print('3- Procurar um abrigo')
    if opcao_escolhida1 != 4:
        print('4- Voltar a dormir')
    print('5- Explorar a região')
    
    acao2 = int(input('Qual será sua próxima ação?\n'))
    opcoes_padrao(relogio, personagem, acao2)
    if acao2 == 5:
        sorteio_passeio = randint(1,3)
        relogio.avanca_tempo(50)  
        if sorteio_passeio == 1:
            personagem.muda_fome(20)
            personagem.muda_energia(-20)
            personagem.muda_humor(-10)
            print('Você fez um passeio pelo parque, que não foi muito bom.Você encontrou um cachorro hostil.')
            cachorro_hostil = randint(1,3)
            if cachorro_hostil == 1:
                print('O cachorro correu atrás de você.')
            elif cachorro_hostil == 2:
                print('O cachorro tentou de morder, mas você escapou.') 
            else:
                carrocinha.carrocinha(relogio, personagem)
                relogio.avanca_dia()
        elif sorteio_passeio == 2:
            shopping_passeio = randint(1,3)
            personagem.muda_fome(20)
            personagem.muda_energia(-20)
            personagem.muda_humor(-10)
            print('Você passeiou no shopping e foi muito divertido. Você encontrou um pessoa legal.')
            if shopping_passeio == 1:
                print('Você encontrou uma pessoa que deu uma sobra, e um carinho na cabeça.')
            elif shopping_passeio == 2:
                print('Você encontrou uma pessoa que te deu uma bolinha, mas ela caiu no buraco e você ficou triste.')
            else:
                print('Você foi expulso pelo segurança.')
                carrocinha.carrocinha(relogio, personagem)
                relogio.avanca_dia()
        else:
            personagem.muda_fome(10)
            personagem.muda_energia(-20)
            personagem.muda_humor(20)
            print('Você encontro uma padaria e teve uma surpresa.')
            surpresa = randint(1,3)
            if surpresa == 1:
                print('O dono padaria te deu um pão.')
            elif surpresa == 2:
                print('O dono da padaria te um pão com mortadela.') 
            else:
                carrocinha.carrocinha(relogio, personagem)
                relogio.avanca_dia()

    fase1(relogio, personagem)
        
        





    