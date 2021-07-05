from random import randint
from time import sleep
from classes.PePaTe import PePaTe
from classes.relogio import Relogio

class Carrocinha:
    def carrocinha(self, relogio, personagem):
        print(f'{personagem.nome} encontrou a carrocinha')
        pepate = PePaTe()
        dias = Relogio()
        escolha = int(input('''
        1 - Fugir
        2 - Esconder
        Escolha: '''))
        sorteio_carrocinha = randint(0,1)
        if escolha == 1:
            if sorteio_carrocinha == 0:
                relogio.avanca_tempo(80)
                print(f'{personagem.nome} depois de muito esforço conseguiu fugir da carrocinha, porém se sente muito cansado {relogio}')
                personagem.muda_fome(20)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
            elif sorteio_carrocinha == 1:
                print(f'{personagem.nome} não conseguiu fugir, você pode tentar novamente, lembrando que se sua energia chegar a 0, GAME OVER!')
                teste = str(input("Você deseja tentar fugir novamente [S/N]?")).strip().upper()[0]
                adocao = randint(1,3)
                while True:
                    if teste == "S":    
                        pepate.jogopepate()
                    if pepate.jogadaCao == True:
                        relogio.avanca_tempo(80)
                        print(f'{personagem.nome} depois de muito esforço conseguiu fugir da carrocinha, porém se sente muito cansado {relogio}')
                        personagem.muda_fome(-10)
                        personagem.muda_energia(-15)
                        personagem.muda_humor(-5)
                    else:
                        print("Voce desistiu de fugir e foi levado pela carrocinha")
                        if dias.dia == 1:
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-25)
                            personagem.muda_humor(-20)
                            relogio.avanca_tempo(720)
                        if dias.dia > 1:
                            if adocao == 1:
                                print("Voce foi adotado")
                            else:
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-25)
                                personagem.muda_humor(-20)
                                relogio.avanca_tempo(720)