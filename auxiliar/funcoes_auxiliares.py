from random import randint

def opcoes_padrao(relogio, personagem, acao):
    if acao == 1:
        comida = int(input(f'''Onde {personagem.nome} vai procurar comida
        
        1- Nas sobras dos lixos.
        2- Tentar encontrar alguém para dar.
        '''))

        if comida == 1:
            sorteio_comida = randint(1,3)
            relogio.avanca_tempo(40)
            if sorteio_comida == 1:
                personagem.muda_fome(20)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
                print(f'Hoje {personagem.nome} está com sorte! Apesar de ser no lixo conseguiu bastante sobrinhas')
            elif sorteio_comida == 2:
                personagem.muda_fome(10)
                personagem.muda_energia(5)
                personagem.muda_humor(5)
                print(f'Hoje o dia não foi muito bom! {personagem.nome} teve que vasculhar em muitos lixos para conseguir comida, e algumas delas já não estavam muito boas...')
            else:
                personagem.muda_energia(-20)
                personagem.muda_humor(-5)
                print(f'Hoje {personagem.nome} está sem sorte! Apesar de procurar em muitos lixos ele não conseguiu nada. Ouviu esse barulho...é a barriguinha do nosso amigo.')

        elif comida == 2:
            sorteio_comida = randint(1,3)
            relogio.avanca_tempo(60)
            if sorteio_comida == 1:
                personagem.muda_fome(30)
                personagem.muda_energia(20)
                personagem.muda_humor(10)
                print(f'Hoje {personagem.nome} está com sorte! Andando pela cidade ele encontrou um parque onde tinha uma criança comendo um hamburguer, ela deixou cair muitos pedacinhos super saborosos... E ainda deixou todas as sobras da família para ele... Há tempos ele não comia tão bem.')
            elif sorteio_comida == 2:
                personagem.muda_fome(20)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
                print(f'Hoje o dia não foi muito bom! {personagem.nome} teve que andar muito pela cidade para conseguir comida, quando já estava quase desistindo avistou uma senhora no parque que estava dando migalhas de pão para os pombos, ele se aproximou e ficou fazendo aquela carinha de cachorro pidão. Demorou para que sua presença fosse notada, mas a gentil senhora pegou da sua bolsa um pão e deu para nosso amigo')
            else:
                personagem.muda_energia(-20)
                personagem.muda_humor(-10)
                print(f'Hoje {personagem.nome} acordou com o pé esquerdo! Apesar de procurar muito pela cidade ele não conseguiu comida. Foi enxotado da frente de vários comércios, inclusive o dono do açougue jogou água nele e o chamou de vira-lata. Se não bastasse uma mulher passou apressada com celular e pisou em sua patinha. Coitado do nosso amigo.')
    
    elif acao == 2:
        sorteio_amigo = randint(1,3)
        if sorteio_amigo == 1:
            relogio.avanca_tempo(40)
            personagem.muda_fome(-5)
            personagem.muda_energia(-10)
            personagem.muda_humor(20)
            print(f'Andando pelos becos {personagem.nome} encontra dois cachorros, Mel, uma poodle que foi abandona por ser considerada idosa, e Thor um jovem grande cachorro que foi abandonado depois que seus donas acharam que ele "cresceu demais". Sem hesitar {personagem.nome} chama seus amigos para brincar de pega - pega.... Agora seu rabinho esta balançando tão rápido, que parece que vai fazer ele voar de tão feliz')
        elif sorteio_amigo == 2:
            print(f'Andando pela cidade {personagem.nome} encontra um parque, e acredita ser um ótimo lugar para encontrar um novo amigo. Lá ele vê uma mulher passeando com uma cachorrinha, e analisa se pode ou não se aproximar...."Humm pensando bem essa não é uma boa idéia, elas parecem ser muito metidas", pensa nosso amigo. Enfim avista um casal com um cachorrinho jovem de porte médio, pelos reluzentes ao sol, ta aí a oportunidade. \n')
            dono = randint (1,2)
            if dono == 1:
                relogio.avanca_tempo(30)
                personagem.muda_fome(-5)
                personagem.muda_energia(-10)
                personagem.muda_humor(20)
                print(f'E não é que nosso amigo estava certo. {personagem.nome} se aproximou devagar e fez um novo amigo no parque, Bilu, um legítimo  boxer de alta linhagem, {personagem.nome} nem sabia o que ele estava falando sobre pedigree e sei lá mais o que, o que mais queria era aproveitar e continuar a brincar com a bola que Bilu havia emprestado. Não é todo dia que os donos deixam ele se aproximar...')
            else:
                relogio.avanca_tempo(20)
                personagem.muda_energia(-5)
                personagem.muda_humor(-25)
                print(f'{personagem.nome}, se aproxima devagar e fica esperando até que seja notado. Entretando quando a mulher o vê leva um susto, e o homem começou a jogar pequenas pedras no nosso amigo, mandando ele se afastar...{personagem.nome} foge o mais rápido do que pode ao som dos berros do homem o chamando de pulguento e fedido. Pobre do nosso amiga, que apesar de tudo tenta ficar limpinho se esfregando nas gramas dos quintais floridos das casas.')

        else:
            relogio.avanca_tempo(20)
            personagem.muda_fome(-5)
            personagem.muda_energia(-10)
            personagem.muda_humor(10)
            print(f'Hoje o mar não está para peixe, ou melhor para cachorros...{personagem.nome} procurou nos parques e nos portões das casas, mas não encontrou nenhum amigo... "Talvez seja melhor tentar mais tarde.Talvez ainda estejam dormindo", pensa nosso amigo.')

    elif acao == 3:
        print(f'{personagem.nome} está se sentindo um pouco cansado, talvez fosse bom procurar por um abrigo para descansar. As ruas podem ser perigosas e frias, se não conseguir um bom lugar para dormir pode ser muito difícil.\n')
        abrigo = randint(1,2)
        if abrigo == 1:
            relogio.avanca_tempo(40)
            personagem.muda_energia(-10)
            personagem.muda_humor(15) 
            print(f'{personagem.nome} já esta acostumado a andar pelos becos a procura de abrigo, mas está cada vez mais difícil. Alguns valentões roubam os melhores lugares, e não é bom arrumar brigas na rua, porque se você se machucar ninguém ajuda. {personagem.nome} sempre se lembra de um velho amigo, Bandite, certe vez, ele não quis ceder seu abrigo e apanhou de dois valentões, ele ficou sem andar por dois dias, até que uma tia veio e o levou de carro, nunca mais se teve notícias do pobre Bandite. Mas hoje é o dia de sorte de nosso amigo, ele encontra abriga debaixo de um velho trem abandonado, hoje ele vai poder ter um soninho tranquilo')   
        else:
            relogio.avanca_tempo(40)
            personagem.muda_energia(-15)
            personagem.muda_humor(-5) 
            print(f'{personagem.nome} já esta acostumado a andar pelos becos a procura de abrigo, mas esta noite em especial está mais difícil, os valentões do bairro vizinho estão por aqui, e com isso os melhores lugares ja estão ocupados."Talvez seja melhor tentar a sorte  mais tarde", pensa nosso amigo. Melhor não arrumar briga. "Tem dias que viver na rua não é fácil", pensa novamente. ')

    elif acao == 4:
        relogio.avanca_tempo(40)
        personagem.muda_energia(30)
        personagem.muda_fome(-20) 
        print(f'"Hoje o dia está preguiçoso", pensa nosso amigo.Talvez fosse melhor estender mais esse soninho. Zzzzzzzz')