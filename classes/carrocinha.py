from random import randint
from time import sleep
from classes.PePaTe import PePaTe
from classes.dados import Dados

class Carrocinha:
    # Pegando parametros relogio e personagem, para usar no main
    def carrocinha(self, relogio, personagem):
        print(f'Entre as ruas {personagem.nome} acaba se deparando com uma carrocinha')

        pepate = PePaTe()
        dado = Dados()
        escolha = int(input(''' 
        1 - Fugir
        2 - Esconder
        Escolha: ''')) #Escolha do usuario para as seguintes opções
        if escolha == 1: #Escolha Fugir
            sorteio_carrocinha = randint(1,2) #Sorteia um número para validação
            if sorteio_carrocinha == 1: #Cao conseguiu fugir
                relogio.avanca_tempo(80)
                print(f'{personagem.nome} corre apressado entre as ruas, fugindo do carro da carrocinha e daquele homem uniformizado que insiste em tentar laçar seu pescoço. Entre os becos encontra um lugar seguro e depois de uma longa perseguição se sente exausto e assustado.')
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                relogio.avanca_dia()
            elif sorteio_carrocinha == 2:  # Cao não conseguiu fugir
                print(
                    f'{personagem.nome} {personagem.nome} corre desesperadamente para se safar, passando correndo entre as pessoas que somente observam a cena, ele(a) implora ajuda, entretanto ninguém faz nada, somente observa a situação. Ele(a) corre para uma rua estreita na esperança de se esconder, entretanto não há saida e nosso amigo(a) é capturado pelo homem uniformizado')
                # Random para decidir se o cão foi doado
                adocao = randint(1, 3)
                while True:
                    print(
                        f"{personagem.nome} se debate desesperamente em vão. Entretanto agora você tem a chance de ajudar nosso amigo!!!")
                    teste = str(
                        input("Você quer ajudar a criar uma distração, para ajudar {personagem.nome} a tentar fugir novamente [S/N]: ")).strip().upper()[0]
                    if teste == "S":
                        print('Então jogue Jokenpo com o homem uniformizado e tente ajuda {personagem.nome}!')
                        # Jogo Pedra Papel e Tesoura atribuida a opção Fugir
                        pepate.jogopepate(personagem)
                        if pepate.jogadaCao == True:
                            relogio.avanca_tempo(80)
                            print(
                                f'Deu certo!!! Você conseguiu criar uma distração e ajudar{personagem.nome}. E agora nosso amigo foge o mais rápido do que pode. E agora precisa se esconder e se acalmar depois desse susto')
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            relogio.avanca_dia()
                            break
                    else:
                        print("As vezes nem com agilidade e malandragem das ruas é difícil conseguir fácil fugir, e infelizmente {personagem.nome} é levado para uma gaiola apertada.")
                        personagem.muda_lugar('carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-10)
                            personagem.muda_humor(-10)
                            personagem.muda_frio(-5)
                            relogio.avanca_tempo(720)
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao == 1:
                                print("Voce foi adotado")
                                break
                            else:
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-10)
                                personagem.muda_humor(-10)
                                personagem.muda_frio(-5)
                                relogio.avanca_tempo(720) #12h após sair da carrocinha 
                                break
        elif escolha == 2:#Escolha Esconder
            sorteio_carrocinha = randint(1,2) #Sorteia um número para validação
            if sorteio_carrocinha == 1:#Conseguiu se esconder
                relogio.avanca_tempo(80)
                print(f'{personagem.nome} conseguiu se esconder, porém se sente muito cansado, decidiu se esconder e descansar até a situação se acalmar')
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
            elif sorteio_carrocinha == 2: #Não conseguiu se esconder
                print(f'{personagem.nome} não conseguiu se esconder, você pode correr e tentar novamente, lembrando que se sua energia chegar a 0, GAME OVER!')
                adocao = randint(1,3)
                while True:
                    print(f"{personagem.nome} tentou se esconder em todos os lugares, mas falhou!")
                    teste = str(input("Você deseja tentar se esconder novamente [S/N]: ")).strip().upper()[0]
                    if teste == "S": 
                        dado.jogoDado(personagem)#Jogo do Dado atribuida a opção Esconder
                        if dado.caoDado == True:
                            relogio.avanca_tempo(80)
                            print(
                                f'{personagem.nome} depois de muito esforço conseguiu fugir da carrocinha, porém se sente muito cansado, decidiu se esconder e descansar até a situação se acalmar')
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            break
                    else:
                        print("Voce tentou, tentou, tentou se esconder mas não conseguiu, desistiu e foi levado pela carrocinha")
                        personagem.muda_lugar('carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-10)
                            personagem.muda_humor(-10)
                            personagem.muda_frio(-5)
                            relogio.avanca_tempo(720) #12h após sair da carrocinha
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao == 1:
                                print("Voce foi adotado")
                                break
                            else:
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-10)
                                personagem.muda_humor(-10)
                                personagem.muda_frio(-5)
                                relogio.avanca_tempo(720)
                                break
