from random import randint
from rich import print
from time import sleep
from rich.prompt import Prompt
from pygame import mixer
import webbrowser  # para abrir links do bowser


def final():
    print ('\n[red]NÃO COMPRE ADOTE![red]\n')
    print_delay (f'''
    Segundo a OMS estima-se que só no Brasil existam mais de 30 milhões de animais abandonados, sendo cerca de 10 milhões de gatos e 20 milhões de cães. No mundo são cerca 200 milhões de animais. Como consta a pesquisa de 2020.

    ''')
    sleep(1)
    links = str(input("Deseja conhecer Ongs que ajudam a animais abandonados, ou Ongs para adoção? [S/N] ")).upper()[0]
    if links == 'S':
       webbrowser.open('https://nfpet.com.br/blog/2019/08/10-ongs-de-animal-para-voce-ajudar/')
       

def opcoes_padrao(relogio, personagem, acao):
    if acao == 1:
        comida = int(Prompt.ask(f'''
        '\nOnde {personagem.nome} vai procurar comida?:
        [blue]
        1- Nas sobras dos lixos.
        2- Tentar encontrar alguém para dar.
        [blue]
        
        '''))

        if comida == 1:
            personagem.muda_lugar("beco")
            sorteio_comida = randint(1,3)
            relogio.avanca_tempo(40)
            if sorteio_comida == 1:
                print(f'Hoje {personagem.nome} está com sorte! Apesar de ser no lixo conseguiu bastante sobrinhas')
                print()
                personagem.muda_fome(15)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
            elif sorteio_comida == 2:
                print(f'Hoje o dia não foi muito bom! {personagem.nome} teve que vasculhar em muitos lixos para conseguir comida, e algumas delas já não estavam muito boas...')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(5)
                personagem.muda_humor(5)
            else:
                print(f'Hoje {personagem.nome} está sem sorte! Apesar de procurar em muitos lixos ele(a) não conseguiu nada. Ouviu esse barulho...é a barriguinha do(a) nosso(a) amigo(a).')
                print()
                personagem.muda_energia(-10)
                personagem.muda_humor(-5)
                if relogio.dia >= 2:
                    print(f'{personagem.nome} ouve um barulho e tenta se esconder entre os lixos, em seguida sente uma mão lhe segurando, com cuidado uma mulher lhe pega no colo e fala baixinho: "calma amiguinho(a) agora está tudo bem, eu vou te proteger", e abraça {personagem.nome} carinhosamente, e segue em direção a saída do beco {personagem.nome} nem pode acreditar no que está acontecendo, agora ele sabe o que pode acontecer quando alguns cachorros "somem" das ruas. Eles podem sim, ter um final feliz e encontrar um lar. ')
                    sleep(1)
                    final()
                    exit()

        elif comida == 2:
            personagem.muda_lugar("parque")
            sorteio_comida = randint(1,3)
            relogio.avanca_tempo(180)
            if sorteio_comida == 1:
                print(f'Hoje {personagem.nome} está com sorte! Andando pela cidade ele(a) encontrou um parque onde tinha uma criança comendo um hamburguer, ela deixou cair muitos pedacinhos super saborosos... E ainda deixou todas as sobras da família para ele(a)... Há tempos ele(a) não comia tão bem.')
                print()
                personagem.muda_fome(20)
                personagem.muda_energia(15)
                personagem.muda_humor(10)
            elif sorteio_comida == 2:
                print(f'Hoje o dia não foi muito bom! {personagem.nome} teve que andar muito pela cidade para conseguir comida, quando já estava quase desistindo avistou uma senhora no parque que estava dando migalhas de pão para os pombos, ele(a) se aproximou e ficou fazendo aquela carinha de cachorro(a) pidão. Demorou para que sua presença fosse notada, mas a gentil senhora pegou da sua bolsa um pão e deu para nosso(a) amigo(a)')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
            else:
                print(f'Hoje {personagem.nome} acordou com o pé esquerdo! Apesar de procurar muito pela cidade ele(a) não conseguiu comida. Foi enxotado da frente de vários comércios, inclusive o dono do açougue jogou água nele(a) e o(a) chamou de vira-lata. Se não bastasse uma mulher passou apressada com celular e pisou em sua patinha. Coitado do nosso(a) amigo(a).')
                print()
                personagem.muda_energia(-10)
                personagem.muda_humor(-10)
    
    elif acao == 2:
        sorteio_amigo = randint(1,3)
        if sorteio_amigo == 1:
            print(f'Andando pelos becos {personagem.nome} encontra dois cachorros, Mel, uma poodle que foi abandona por ser considerada idosa, e Thor um jovem grande cachorro que foi abandonado depois que seus donas acharam que ele "cresceu demais". Sem hesitar {personagem.nome} chama seus amigos para brincar de pega - pega.... Agora seu rabinho esta balançando tão rápido, que parece que vai fazer ele(a) voar de tão feliz')
            print()
            relogio.avanca_tempo(40)
            personagem.muda_fome(10)
            personagem.muda_energia(15)
            personagem.muda_humor(15)
            personagem.muda_lugar("beco")
        elif sorteio_amigo == 2:
            personagem.muda_lugar("parque")
            print(f'Andando pela cidade {personagem.nome} encontra um parque, e acredita ser um ótimo lugar para encontrar um novo amigo. Lá ele vê uma mulher passeando com uma cachorrinha, e analisa se pode ou não se aproximar...."Humm pensando bem essa não é uma boa idéia, elas parecem ser muito metidas", pensa nosso(a) amigo(a). Enfim avista um casal com um cachorrinho jovem de porte médio, pelos reluzentes ao sol, ta aí a oportunidade. \n')
            dono = randint(1,2)
            if dono == 1:
                print(f'E não é que nosso(a) amigo(a) estava certo(a). {personagem.nome} se aproximou devagar e fez um novo amigo no parque, Bilu, um legítimo  boxer de alta linhagem, {personagem.nome} nem sabia o que ele estava falando sobre pedigree e sei lá mais o que, o que mais queria era aproveitar e continuar a brincar com a bola que Bilu havia emprestado. Não é todo dia que os donos deixam ele(a) se aproximar...')
                print()
                personagem.muda_fome(5)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                relogio.avanca_tempo(180)
                if relogio.dia >= 2:
                    print(f'{personagem.nome} continua a brincar quando sente uma mão lhe levantar,a dona do Bilu o pega carinhosamente no colo e segue em direção a saída do parque com Bilu os seguin do. {personagem.nome} nem pode acreditar no que está acontecendo, a dona de o abraça e diz "se prepara menino(a) que hoje você ganhou um família e um irmão atrapalhado". Bilu corre alegremente balançando o rabo, sabendo que agora vai ter alguém para brincar. {personagem.nome} nem acredita na sorte que teve hoje, e mal consegue conter seu rabo, que gira sem parar. ')
                    sleep(1)
                    final()
                    exit()
            else:
                print(f'{personagem.nome}, se aproxima devagar e fica esperando até que seja notado(a). Entretando quando a mulher o(a) vê leva um susto, e o homem começou a jogar pequenas pedras no(a) nosso(a) amigo(a), mandando ele(a) se afastar... {personagem.nome} foge o mais rápido do que pode ao som dos berros do homem o chamando de pulguento(a) e fedido(a). Pobre do(a) nosso(a) amigo(a), que apesar de tudo tenta ficar limpinho(a) se esfregando nas gramas dos quintais floridos das casas.')
                print()
                personagem.muda_energia(-5)
                personagem.muda_humor(-10)
                relogio.avanca_tempo(20)

        else:
            print(f'Hoje o mar não está para peixe, ou melhor para cachorros...{personagem.nome} procurou nos parques e nos portões das casas, mas não encontrou nenhum amigo... "Talvez seja melhor tentar mais tarde.Talvez ainda estejam dormindo", pensa nosso(a) amigo(a).')
            print()
            personagem.muda_fome(-5)
            personagem.muda_energia(-10)
            personagem.muda_humor(10)
            relogio.avanca_tempo(180)
            personagem.muda_lugar("jardim abandonado")

    elif acao == 3:
        print(f'{personagem.nome} está se sentindo um pouco cansado, talvez fosse bom procurar por um abrigo para descansar. As ruas podem ser perigosas e frias, se não conseguir um bom lugar para dormir pode ser muito difícil.\n')
        abrigo = randint(1,2)
        if abrigo == 1:
            print(f'{personagem.nome} já esta acostumado(a) a andar pelos becos a procura de abrigo, mas está cada vez mais difícil. Alguns valentões roubam os melhores lugares, e não é bom arrumar brigas na rua, porque se você se machucar ninguém ajuda. {personagem.nome} sempre se lembra de um velho amigo, Bandite, certe vez, ele não quis ceder seu abrigo e apanhou de dois valentões, ele ficou sem andar por dois dias, até que uma tia veio e o levou de carro, nunca mais se teve notícias do pobre Bandite. Mas hoje é o dia de sorte de nosso(a) amigo(a), ele encontra abriga debaixo de um velho trem abandonado, hoje ele vai poder ter um soninho tranquilo') 
            print()
            relogio.avanca_tempo(180)
            personagem.muda_energia(-10)
            personagem.muda_humor(15) 
            personagem.muda_lugar("trem abandonado")
        else:
            print(f'{personagem.nome} já esta acostumado(a) a andar pelos becos a procura de abrigo, mas esta noite em especial está mais difícil, os valentões do bairro vizinho estão por aqui, e com isso os melhores lugares ja estão ocupados."Talvez seja melhor tentar a sorte mais tarde", pensa nosso(a) amigo(a). Melhor não arrumar briga. "Tem dias que viver na rua não é fácil", pensa novamente. ')
            print()
            relogio.avanca_tempo(120)
            personagem.muda_energia(-15)
            personagem.muda_humor(-5)
            personagem.muda_lugar("beco")
            if relogio.dia >= 2:
                    print(f'{personagem.nome} ouve um barulho e tenta se esconder no beco, fica apavorado com a possibilidade de ser um dos valentões ou as crianças que ha alguns dias haviam jogado pedras nele, e  em seguida sente uma mão lhe segurando, o corpo de nosso amigo fica todo rígido. {personagem.nome} levanta e olha para quem o segura e vê um senhor morador de rua, que fala baixinho: "calma amiguinho(a) agora está tudo bem, vem comigo", e o abraça. {personagem.nome} ve bondade naqueles velhos olhos humildes e segue o velho para a saída do beco, eles vão em direção a ponte onde o velho tem uma pequena casa feita de madeira em direção, o velho lhe da um pouco de uma sobra de comida de uma marmita, que {personagem.nome} aceita de bom gosto, em seguida o homem entra e segurando algo pequeno nas mãos, qnd {personagem.nome} olha nem pode acreditar, é um pewueno filhote de gato, tão pretinho que nem dá para ver os olhos, o velho passa um pode para o gato de leite e toma tudo num instante. Notando o olhar intrigado de nosso amigo ele diz: "Resgatei essa aí do córrego, estava quase morrendo, e agora vive aqui comigo, igual a vc amiguinho(a). Agora seremos nós três a nossa família, iremos dividir tudo que temos e ficaremos bem." {personagem.nome} mal pode acreditar na sorte que esta tendo de encontrar alguém tão bom, e percebe qua as vezes quem menos tem é aquele que mais divide, e finalmente consegue relaxar e descansar. ')
                    sleep(1)
                    final()
                    exit()

    elif acao == 4:
        if relogio.horas >= 19:
            relogio. avanca_dia()
        else: 
            relogio.avanca_tempo(120)

        print(f'"Hoje o dia está preguiçoso", pensa nosso(a) amigo(a).Vou aproveitar e tirar um soninho soninho. Zzzzzzzz')
        print()
        personagem.muda_energia(20)
        personagem.muda_fome(-10)
        personagem.muda_frio(5)


def print_delay(text, delay=0.01):
    for n in text:
        print(n, end='')
        sleep(delay)


def noite(personagem, relogio):
    """
     => função auxiliar - Noite

     => Faz: Dar opção de escolha após sair da carrocinha.
    """
    print('Você conseguiu fugir')

    print(
        f'São {str(relogio)}, do {relogio.dia}° dia, {personagem.nome} encontra-se em um {personagem.lugar}.')
    print(personagem)
    sleep(1)
    fase_noite = int(Prompt.ask('''
                           1 - Procurar comida
                           2 - Procurar abrigo
                           '''))

    if fase_noite == 1:
        comida_noite = randint(1, 3)

        if comida_noite == 1:
            print(f'{personagem.nome}, conseguiu comida de primeira.')
            print()
            personagem.muda_fome(15)
            personagem.muda_energia(15)
            personagem.muda_humor(10)
            personagem.muda_frio(-5)
            relogio.avanca_tempo(50)
        elif comida_noite == 2:
            print(f'{personagem.nome}, conseguiu comida de segunda vez.')
            print()
            personagem.muda_fome(10)
            personagem.muda_energia(10)
            personagem.muda_humor(5)
            personagem.muda_frio(-5)
            relogio.avanca_tempo(50)
        else:
            print(f'{personagem.nome}, não conseguiu comida.')
            print()
            personagem.muda_fome(-10)
            personagem.muda_energia(-10)
            personagem.muda_humor(-10)
            personagem.muda_frio(-5)
            relogio.avanca_tempo(50)
    elif fase_noite == 2:
        abrigo_noite = randint(1, 3)
        while True:
            if abrigo_noite == 1:
                print(f'{personagem.nome}, conseguiu abrigo de primeira.')
                print()
                personagem.muda_fome(-10)
                personagem.muda_energia(-25)
                personagem.muda_humor(-20)
                personagem.muda_frio(-20)
                relogio.avanca_tempo(50)
                break
            elif abrigo_noite == 2:
                print(f'{personagem.nome}, conseguiu abrigo de segunda vez.')
                print()
                personagem.muda_fome(15)
                personagem.muda_energia(15)
                personagem.muda_humor(10)
                personagem.muda_frio(-5)
                relogio.avanca_tempo(50)
                break
            else:
                print(f'{personagem.nome}, não conseguiu abrigo.')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                personagem.muda_frio(-5)
                relogio.avanca_tempo(50)

                opcao = input('''
                                Deseja continuar procurando ou dormir na rua [S/N]
                                ''').upper().split()[0]
                if opcao == 'S':
                    abrigo_noite = randint(1, 2)
                    if abrigo_noite == 1:
                        print('Você tentou e não conseguiu')
                        print()
                        personagem.muda_energia(-5)
                        personagem.muda_frio(-5)
                    else:
                        print('Você conseguiu achar um abrigo.')
                        print()
                        personagem.muda_fome(5)
                        personagem.muda_energia(15)
                        personagem.muda_humor(15)
                        personagem.muda_frio(5)
                        relogio.avanca_dia()
                        break
                else:
                    print('Você dormiu na rua.')
                    print()
                    personagem.muda_fome(-10)
                    personagem.muda_energia(-10)
                    personagem.muda_humor(-10)
                    personagem.muda_frio(-10)
                    relogio.avanca_dia()
                    break


# definções de efeitos sonoros para cada evento


def cachorro_chorando():
    """
     => função mixer pygame - sound fx - Cachorro Chorando

     => Faz tocar o som do cahorro chorando
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/Cachorrochorando.mp3')
    mixer.music.play(start=2)


def caes_carrocinha():
    """
     => função mixer pygame - sound fx - Caes na Carrocinha

     => Faz tocar o som de Caes na Carrocinha
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/CaesCarrocinha.mp3')
    mixer.music.play(start=2)


def cao_correndo1():
    """
     => função mixer pygame - sound fx - Caes correndo 1

     => Faz tocar o som de Cão correndo (Opção 1)
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/Caocorrendo.mp3')
    mixer.music.play(start=2)


def cao_correndo2():
    """
     => função mixer pygame - sound fx - Cão Correndo 2

     => Faz tocar o som de Cão Correndo (Opção 2)
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/Caocorrendo2.mp3')
    mixer.music.play(start=2)


def cao_hostil():
    """
     => função mixer pygame - sound fx - Cão Hostil

     => Faz tocar o som de Caes na Carrocinha
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/CaoHostil.mp3')
    mixer.music.play(start=2)


def comendo():
    """
     => função mixer pygame - sound fx - Cão Comendo

     => Faz tocar o som de Cão Comendo
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/Comendo.mp3')
    mixer.music.play(start=2)


def correntes_carrocinha():
    """
     => função mixer pygame - sound fx - Correntes da Cachorrocinha

     => Faz tocar o som de Correntes da Carrocinha
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/CorrentesCarrocinha.mp3')
    mixer.music.play(start=1)


def outros_caes():
    """
     => função mixer pygame - sound fx - Outros Cães

     => Faz tocar o som de Outros Cães
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/CaesCarrocinha.mp3')
    mixer.music.play(start=20)


def latido():
    """
     função mixer pygame - sound fx - Latido

     Faz tocar o som de Latido
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/latido.mp3')
    mixer.music.play(loops=2)


def musica_incial():
    """
     função mixer pygame - sound fx - Musica Inicial

     Faz tocar o som de inicio do jogo
    """
    mixer.init()
    mixer.music.load('./auxiliar/sounds/wi.mp3')
    mixer.music.play()
