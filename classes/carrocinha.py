from random import randint
from time import sleep
from classes.PePaTe import PePaTe
from classes.dados import Dados

class Carrocinha:
    def carrocinha(self, relogio, personagem): #Pegando parametros relogio e personagem, para usar no main
        print(f'{personagem.nome} encontrou a carrocinha')
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
                print(f'{personagem.nome} depois de muito esforço conseguiu fugir da carrocinha, porém se sente muito cansado, decidiu se esconder e descansar até a situação se acalmar')
                personagem.muda_fome(20)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
                relogio.avanca_dia()
            elif sorteio_carrocinha == 2: #Cao não conseguiu fugir
                print(f'{personagem.nome} não conseguiu fugir, você pode tentar novamente, lembrando que se sua energia chegar a 0, GAME OVER!')
                adocao = randint(1,3) #Random para decidir se o cão foi doado
                while True:
                    print(f"{personagem.nome} tentou fugir com todas suas forças mas falhou!")
                    teste = str(input("Você deseja tentar fugir novamente [S/N]: ")).strip().upper()[0]
                    if teste == "S":    
                        pepate.jogopepate(personagem) #Jogo Pedra Papel e Tesoura atribuida a opção Fugir
                        if pepate.jogadaCao == True:
                            relogio.avanca_tempo(80)
                            print(f'{personagem.nome} depois de muito esforço conseguiu fugir da carrocinha, porém se sente muito cansado, decidiu se esconder e descansar até a situação se acalmar')
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            relogio.avanca_dia()
                            break
                    else:
                        print("Voce desistiu de fugir e foi levado pela carrocinha")
                        personagem.muda_lugar('carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-25)
                            personagem.muda_humor(-20)
                            personagem.muda_frio(-20)
                            relogio.avanca_tempo(720)
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao == 1:
                                print("Voce foi adotado")
                                break
                            else:
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-25)
                                personagem.muda_humor(-20)
                                personagem.muda_frio(-20)
                                relogio.avanca_tempo(720) #12h após sair da carrocinha 
                                break
        elif escolha == 2:#Escolha Esconder
            sorteio_carrocinha = randint(1,2) #Sorteia um número para validação
            if sorteio_carrocinha == 1:#Conseguiu se esconder
                relogio.avanca_tempo(80)
                print(f'{personagem.nome} conseguiu se esconder, porém se sente muito cansado, decidiu se esconder e descansar até a situação se acalmar')
                personagem.muda_fome(20)
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
                            print(f'{personagem.nome} depois de muito esforço conseguiu se esconder da carrocinha, porém se sente muito cansado, decidiu se esconder e descansar até a situação se acalmar')
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            break
                    else:
                        print("Voce tentou, tentou, tentou se esconder mas não conseguiu, desistiu e foi levado pela carrocinha")
                        personagem.muda_lugar('carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-25)
                            personagem.muda_humor(-20)
                            personagem.muda_frio(-20)
                            relogio.avanca_tempo(720) #12h após sair da carrocinha
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao == 1:
                                print("Voce foi adotado")
                                break
                            else:
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-25)
                                personagem.muda_humor(-20)
                                personagem.muda_frio(-20)
                                relogio.avanca_tempo(720)
                                break
