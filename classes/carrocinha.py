from random import randint
from time import sleep
from classes.PePaTe import PePaTe
from classes.dados import Dados
from auxiliar.funcoes_auxiliares import final
from auxiliar.funcoes_auxiliares import noite
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
                print(f'{personagem.nome} corre apressado(a) entre as ruas, fugindo do carro da carrocinha e daquele homem uniformizado que insiste em tentar laçar seu pescoço. Entre os becos encontra um lugar seguro atrás de umas caixas jogadas, depois dessa longa perseguição se sente exausto(a) e assustado(a).')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                print()
                personagem.muda_lugar("beco")
                relogio.avanca_dia()
            elif sorteio_carrocinha == 2:  # Cao não conseguiu fugir
                print(f'{personagem.nome} corre desesperadamente para se safar, passando correndo entre as pessoas que somente observam a cena, ele(a) implora ajuda, entretanto ninguém faz nada, somente observa a situação. Ele(a) corre para uma rua estreita na esperança de se esconder, entretanto não há saída e nosso(a) amigo(a) é capturado(a) pelo homem uniformizado')
                # Random para decidir se o cão foi doado
                adocao = randint(1, 5)
                while True:
                    print(
                        f"{personagem.nome} se debate desesperamente em vão. Entretanto agora você tem a chance de ajudar nosso(a) amigo(a)!!!")
                    teste = str(
                        input(f"\nVocê quer ajudar a criar uma distração, para ajudar {personagem.nome} a tentar fugir novamente [S/N]: ")).strip().upper()[0]
                    if teste == "S":
                        print(f'\nEntão jogue Jokenpo com o homem uniformizado e tente ajudar {personagem.nome}!')
                        # Jogo Pedra Papel e Tesoura atribuida a opção Fugir
                        pepate.jogopepate(personagem)
                        if pepate.jogadaCao == True:
                            relogio.avanca_tempo(80)
                            print(f'\nDeu certo!!! Você conseguiu criar uma distração e ajudar {personagem.nome}. E agora nosso(a) amigo(a) foge o mais rápido do que pode. Ele(a) precisa se esconder e se acalmar depois desse susto. Virando um quarteirão ele(a) encontra uma casebre abandonado e se esconde lá.')
                            print()
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            print()
                            personagem.muda_lugar("casebre abandonado")
                            relogio.avanca_dia()
                            break
                    else:
                        print(f"\nNem sempre com agilidade e malandragem das ruas é fácil conseguir fugir, apesar de muita luta, {personagem.nome} é levado(a) para uma gaiola apertada da carrocinha, cheio de medo chora assustado(a)")
                        personagem.muda_lugar('canto frio da carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            print()
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-10)
                            personagem.muda_humor(-10)
                            personagem.muda_frio(-5)
                            print()
                            relogio.avanca_tempo(720)
                            print(f'''\nAs horas se arrastam e {personagem.nome} não tem noção alguma de quanto tempo já está preso(a). O medo toma conta do seu coração, preso naquele lugar pequeno e frio ja não sabe o que pode fazer para fugir. Olha para os lados e vê gaiolas e mais gaiolas empilhadas cheias de cachorros de varias tamanhos, alguns velhos, outros doentes, mas também alguns pequenos filhotes que parecem ter meses de vida. {personagem.nome} vendo isso pensa, "Como pode existir um lugar tão triste como esse?" Os minutos continuam a passar se transformando em horas e mais horas, algumas vezes os homens uniformizados abrem as gaiolas para limpar as sujeiras e levar um pouco de ração seca, que nem se da vontade de comer, e é num desses momentos em que nosso(a) amigo(a) vê uma oportunidade para fugir... O homem uniformizado entra pela porta e a deixa encostada, vai limpando as gaiolas e colocando as comidas, quando tira o jornal sujo da gaiola e se vira para jogar no lixo, {personagem.nome} aproveita e pula de dentro da gaiola e corre para a porta a fora. Começa uma gritaria e correria atras, mas nosso(a) amigo(a) corre desesperamente em busca da liberdade, e se esconde em um beco escuro.''')
                            personagem.muda_lugar("beco escuro")
                            noite(personagem, relogio)
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao != 1:
                                print(f'\n{personagem.nome} fica preso(a) sem ter noção de quantas horas já se passaram, seu coração está acelerado, com muito medo e frio seu rabo se encontra baixo, ele(a) presta atenção a cada barulho com medo do que possa acontecer. Depois de algum tempo a porta se abre e outro homem uniformizado entra e lhe coloca um pote de ração seca, {personagem.nome} esta tão assuatado(a) que nem tem vontade de comer, mesmo porque a comida não tem cheiro bom, na verdade ela não tem cheiro de nada, e nosso(a) amigo(a) chora com medo ficar preso(a) ali para sempre.\n')
                                sleep(1)
                                print(f'\nMais algumas horas se passam, e aquele lugar começa a ficar mais frio e escuro, {personagem.nome} já não tem mais esperanças... E mais uma vez a porta é aberta e entra o homem uniformizado, mas desta vez seguido de um rapaz. Eles estão passando pelas gaiolas falando sobre a quanto tempo cada um dos cães estão presos, "Essa aqui já está a 4 semanas, esse outro aqui esta a 2 semanas mais ou menos, foram os donos que o deixaram aqui porque iam se mudar, esse outro encontramos vagando nas ruas, mas é bem velho", segue o homem uniformizado falando. O coração do nosso(a) amigo(a) perde totalmente a esperança, até que o jovem rapaz se aproxima de sua gaiola, "Hey menino(a) venha cá!". {personagem.nome} se encolhe ainda mais no canto, com medo do que possa acontecer, entretatando puxam a coleira dele(a), e nosso(a) amigo(a) ve um rosto familiar ali, lembra vagamente de uma visita que fez no centro onde ganhou uma coxinha incrível desse rapaz, essa lembrança vagou na memória de nosso(a) amiga(o) que nem percebeu que eles ja estavam fechando a porta e partindo, novamente tudo fica silencioso e frio....')
                                sleep(1)
                                print(f'''\nAlguns minutos se passam e novamente a porta se abre, {personagem.nome} sem nenhuma emoção é arrastado(a) para fora de sua jaula e é levado para fora da sala, vários olhinhos o acampanham até saída, e a porta se fecha. Quando {personagem.nome} abre os olhos esta numa sala clara e o mesmo rapaz que lhe deu a coxinha estava lá, pega sua coleira e diz "Eu sou Pedro e agora você será parte da minha família, estou de adotando, se prepare porque agora temos que lhe dar um novo nome". {personagem.nome} não consegue nem acreditar na sorte qaue esta tendo, fecha seus olhinhos e finalmente respira aliviado(a).''')
                                sleep(1)
                                final()
                                exit()
                            else:
                                print(f'''\n{personagem.nome} se ve preso(a) num lugar frio e escuro, apenas consegue distinguir formas de outros cachorros presos nas nas gaiolas vizinhas, seu coração está triste e pesado com a posibilidade de ter que ficar lá para toda a sua vida, não tem noção alguma de quanto tempo já ali, mas parece que longas horas já se passaram. {personagem.nome} percebe que sempre eles vem com colocar a comida e trocar os jornais e deixam a porta entreaberta, e com isso tem a ideia de fugir em algum momento de distração do homem uniformizado. A tarde essa oportunidade surge, o homem uniformizaso abre a gaiola e tira o jornal, quando se vira para jogar no e lixo nosso(a) amigo(a) pula para fora da gaiola apressado e corre para a porta. Enquanto isso o homem grita e xinga para ele(a) voltar, sem hesitar continua a correr, mas antes mesmo de passar pela segunda porta é pego(a) por um guarda, ele(a) continua se debatendo e acaba o fazendo escorregar e solta {personagem.nome} que corre rumo a liberdade, se escondendo o mais rápido possível em um beco.''')
                                print()
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-10)
                                personagem.muda_humor(-10)
                                personagem.muda_frio(-5)
                                print()
                                personagem.muda_lugar("beco úmido") 
                                relogio.avanca_tempo(720) #12h após sair da carrocinha 
                                noite(personagem, relogio)
                                break
                                
        elif escolha == 2:#Escolha Esconder
            sorteio_carrocinha = randint(1,2) #Sorteia um número para validação
            if sorteio_carrocinha == 1:#Conseguiu se esconder
                relogio.avanca_tempo(80)
                print(f'\n{personagem.nome} corre sem rumo entra as ruas, sem se atrever a olhar para tras, corre tanto que suas pernas estavam ja cansadas e tremendo, desesperado(a) procura um lugar seguro para que possa se esconder até a situação acalmar, entre os becos encontra um casebre abandonado com uma fresta quebrada na porta, e com esforço, rastejando consegue entrar e ficar seguro(a) até que a poeira abaixe.')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
                print()
                personagem.muda_lugar("casebre abandonado")
            elif sorteio_carrocinha == 2: #Não conseguiu se esconder
                print(f'{personagem.nome} corre assustado(a) entre os carros, desesperado(a) não tem ideia onde está e como pode se esconder. Mas logo atras estão os homens uniformizados o(a) perseguindo novamente e conseguem alcança-lo(a) antes de conseguir se esconder...\n''')
                sleep(1)
                adocao = randint(1,4)
                while True:
                    teste = str(input(f'Agora você tem a chance de ajudar nosso(a) amigo(a) a fugir, criando uma distração. Você deseja tentar ajudar {personagem.nome} a fugir para se esconder? [S/N]: ')).strip().upper()[0]
                    if teste == "S": 
                        print(f'Jogue dados com o homem uniformizado, se conseguir ganhar poderá ajudar {personagem.nome} a fugir')
                        dado.jogoDado(personagem)#Jogo do Dado atribuida a opção Esconder
                        if dado.caoDado == True:
                            relogio.avanca_tempo(80)
                            print(f'\nApós a sua distração, {personagem.nome} consegue fugir apressadamente entre os carros e depistar os homens uniformizados e ainda muito assustado(a) busca refugio entre os carros de um pátio abandonado.\n')
                            print()
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            print()
                            personagem.muda_lugar("pátio abandonado")
                            break
                    else:
                        print(f'\nApesar de tudo {personagem.nome} não consegue fugir da perseguição dos homens uniformizados e novamente é preso(a) na gaiola fria da carrocinha')
                        personagem.muda_lugar('canto frio da carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            print()
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-10)
                            personagem.muda_humor(-10)
                            personagem.muda_frio(-5)
                            print()
                            relogio.avanca_tempo(720) #12h após sair da carrocinha
                            print(f'''\nAs horas se arrastam e {personagem.nome} não tem noção alguma de quanto tempo já está preso(a). O medo toma conta do seu coração, preso(a) naquele lugar pequeno e frio ja não sabe o que pode fazer para fugir. Olha para os lados e ve gaiolas e mais gaiolas empilhadas cheias de cachorros de varias tamanhos, alguns velhos, outros doentes, mas também alguns pequenos filhotes que parecem ter meses de vida. {personagem.nome} vendo isso pensa, "Como pode existir um lugar tão triste como esse?" Os minutos continuam a passar se transformando em horas e mais horas, algumas vezes os homens uniformizados abrem as gaiolas para limpar as sujeiras e levar um pouco de ração seca, que nem se da vontade de comer, e é num desses momentos em que nosso(a) amigo(a) ve uma oportunidade para fugir... O homem uniformizado entra pela porta e a deixa encostada, vai limpando as gaiolas e colocando as comidas, quando tira o jornal sujo da gaiolo e se vira para jogar no lixo, {personagem.nome} aproveita e pula de dentro da gaiola e corre para a porta a fora. Começa uma gritaria e correria atras, mas nosso(a) amigo(a) corre desesperamente em busca da liberdade, e se esconde em um beco escuro.''')
                            personagem.muda_lugar("beco escuro")
                            noite(personagem, relogio)
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao != 1:
                                print(f'As horas se passam lentas, e {personagem.nome}, já não tem mais esperanças, muito menos em uma fuga e segue com o rabinho baixo de tamanha a tristeza que esta no seu coração. A claridade se dá somente quando a porta é aberta para troca dos jornais e entrega das comidas. {personagem.nome} olha a sua volta e ve pilhas de gaiolas com cachorros amontoados, triste e doentes, completamente sozinhos e sem esperança, o que o deixa ainda mais amargurado, sem saber o que fazer...')
                                print(f'{personagem.nome} percebe que algumas vezes aparecem pessoas que levam alguns desses cachorros, não entende muito bem, só sabe que eles nunca mais voltam, o que o(a) deixa ainda mais assustado(a).')
                                relogio.avanca_tempo(120) 
                                sleep(1)
                                print(f'Mais algum tempo passa e mais três pessoas entram nas salas, algumas tentam passar a mão nos cachorros pela gaiola outras chamam, "Pequeno vem aqui, totó olha aqui", {personagem.nome} não entende o que esta acontecendo. Uma menina se aproxima da gaiola e o(a) chama, "Vem aqui", um pouco receoso(a) {personagem.nome} se aproxima e cheira sua mão, mas a menina é puxada para longe da gaiola e a porta se fecha novamente. E de novo, nosso(a) amigo(a) se encontra sozinho(a) e triste.')
                                sleep(1)
                                print(f' Mais uma vez a porta se abre e uma pessoa uniformizada entra e leva {personagem.nome} para fora da sala, la ele(a) ve as pessoas que a pouco estavam olhando as gaiolas inclusive a menina que ele cheirou a mão, que corre em sua direção e o(a) abraça dizendo que agora é parte da família.')
                                sleep(1)
                                final()
                                exit()
                            else:
                                print(f'''\n{personagem.nome} se ve preso(a) num lugar frio e escuro, apenas consegue distinguir formas de outros cachorros presos nas nas gaiolas vizinhas, seu coração está triste e pesado com a posibilidade de ter que ficar lá para toda a sua vida, não tem noção alguma de quanto tempo já ali, mas parece que longas horas já se passaram. {personagem.nome} percebe que sempre eles vem com colocar a comida e trocar os jornais e deixam a porta entre aberta, e com isso tem a ideia de fugir em algum momento de distração do homem uniformizado. A tarde essa oportunidade surge, o homem uniformizaso abre a gaiola e tira o jornal, quando se vira para jogar no e lixo nosso(a) amigo(a) pula para fora da gaiola apressado e corre para a porta. Enquanto isso o homem grita e xinga para ele(a) voltar, sem hesitar continua a correr, mas antes mesmo de passar pela segunda porta é pego(a) por um guarda, ele(a) continua se debatendo e acaba o fazendo escorregar e solta {personagem.nome} que corre rumo a liberdade, se escondendo o mais rápido possível em um beco.''')
                                print()
                                personagem.muda_lugar("beco úmido") 
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-10)
                                personagem.muda_humor(-10)
                                personagem.muda_frio(-5)
                                print()
                                relogio.avanca_tempo(720)
                                noite(personagem, relogio)
                                break
