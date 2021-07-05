from random import randint
from time import sleep

class Dados:
    def __init__(self):
        self.caoDado = True

    def jogoDado(self, personagem):
#Listas para cada player, onde é atribuida o dicionario do respectivo player contendo o número do dado
        listap1 = []
        listap2 = []


        #Dicionario com as keys para cada player, onde é atribuido +1 a cada rodada, para verificar o player que mais venceu rodadas
        play = dict()
        play['Cao'] = 0
        play['Carrocinha'] = 0

        cao = dict()
        carrocinha = dict()

        print(f"\n\033[3;7m ==== VAMOS JOGAR OS DADOS PARA TENTAR SALVAR {personagem.nome.upper()} ===== \033[0;0m\n")
        print("\nJOGADORES PREPARADOS...", end=" "), print("VAMOS LÁ")
        sleep(1)
        cao = dict()
        carrocinha = dict()
        #=============================== PLAYER 1 ===========================================  
        print("\033[34;1;3m\nCÃO JOGOU O DADO\033[0;0m")
        sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")

        dado = randint(1,6) #Número aleatorio do dado

        print(f'\nO DADO CAIU NO NÚMERO {dado}')
        sleep(0.8)

        cao['Jogadas'] = dado
        listap1.append(cao['Jogadas']) #Lista do player 1 atribuindo o valor dado registrado no dicionario, e assim em diante nos proximos player (Foi feito em uma lista, para caso o programador queira ver o historico de jogadas dos player)

        #=============================== PLAYER 2 =========================================== 
        print("\033[35;1;3m\nCARROCINHA JOGOU O DADO\033[0;0m")
        sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" "), sleep(0.5), print("...", end=" ")

        dado = randint(1,6) #Novo número gerado pelo dado

        print(f'\nO DADO CAIU NO NÚMERO {dado}')
        sleep(0.8)

        carrocinha['Jogadas'] = dado
        listap2.append(carrocinha['Jogadas'])

    #Condição para verificar qual player venceu a rodada    
        if cao['Jogadas'] > carrocinha['Jogadas']:
            play['Cao'] += 1
        else:
            play['Carrocinha'] += 1

        #Condição que verifica qual player venceu mais rodadas, usando como parametro o dicionario de pontuação total
        if play['Cao'] > play['Carrocinha'] or play['Cao'] == play['Carrocinha']:
            self.caoDado = True
        else:
            self.caoDado = False
