
from auxiliar.funcoes_auxiliares import opcoes_padrao
from random import randint
from classes.carrocinha import Carrocinha
from rich import print
from time import sleep
from rich.prompt import Prompt #Pra mudar a cor no input
     
def fase1(relogio, personagem):
    print(f'São {str(relogio)}, do {relogio.dia}° dia, {personagem.nome} encontra-se em um {personagem.lugar}.')
    print(personagem)
    sleep(1)

    acao1 = int(Prompt.ask(f'''
    O que {personagem.nome} vai fazer?
    [blue]
    1- Procurar comida
    2- Procurar alguém para brincar
    3- Procurar um abrigo
    4- Voltar a dormir
    [/blue]
    '''))

    while acao1 not in [1,2,3,4]:
        print('Opção inválida.')
        acao1 = int(Prompt.ask(f'''
    O que {personagem.nome} vai fazer?
    [blue]
    1- Procurar comida
    2- Procurar alguém para brincar
    3- Procurar um abrigo
    4- Voltar a dormir
    [/blue]
    '''))
    
    opcoes_padrao(relogio, personagem, acao1)
    sleep(1)
    fase2(relogio, personagem, acao1)
    

def fase2(relogio, personagem, opcao_escolhida1):
    print(f'São {str(relogio)}, {personagem.nome} você está em um {personagem.lugar}.')
    print(personagem)
    carrocinha = Carrocinha()
    if opcao_escolhida1 != 1:
        print('[blue]1- Procurar comida[/blue]')
    if opcao_escolhida1 != 2:
        print('[blue]2- Procurar alguém para brincar[/blue]')
    if opcao_escolhida1 != 3:
        print('[blue]3- Procurar um abrigo[/blue]')
    if opcao_escolhida1 != 4:
        print('[blue]4- Voltar a dormir[/blue]')
    print('[blue]5- Explorar a região[/blue]')
    
    acao2 = int(input('\nQual será sua próxima ação?\n'))
    opcoes_padrao(relogio, personagem, acao2)
    if acao2 == 5:
        sorteio_passeio = randint(1,3)
        relogio.avanca_tempo(50)  
        if sorteio_passeio == 1:
            personagem.muda_lugar("parque")
            print(f'"Uma volta no parque sempre é uma boa ideia", pensa {personagem.nome}...')
            cachorro_hostil = randint(1,3)
            if cachorro_hostil == 1:
                personagem.muda_fome(-5)
                personagem.muda_energia(-5)
                personagem.muda_humor(10)
                print(f'Esses passeios no parque são produtivos, pois {personagem.nome} consegue se alongar, correr e se divertir, mesmo sozinho(a). Às vezes ele(a) se aproxima de pessoas que dão algum petisco, ou até mesmo carinhos, outras o(a) espantam, ou se afastam assustadas. Mas observando as famílias com seus filhos e pets ele(a) ainda consegue ter esperança no fundo do coração de um dia ter alguém para coçar sua barriga e leva-lo(a) para um lar.')
            elif cachorro_hostil == 2:
                personagem.muda_fome(-5)
                personagem.muda_energia(-10)
                personagem.muda_humor(-10)
                print(f'{personagem.nome} adora parques, fica correndo entre os arbustos e se esfregando na grama ele(a) brinca feliz, e acaba até se esquecendo da vida, e da tristeza de sempre estar sozinho(a). E no meio de tanta diversão não nota a presença de um cachorro hostil que o(a) observava, e que sem ao menos dizer uma palavra corre para atacar {personagem.nome}, que consegue se desvencilhar e corre para se esconder nos arbustos.') 
            else:
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(-10)
                print(f'Esses passeios no parque são produtivos, pois {personagem.nome} sempre consegue umas migalhas das pessoas que estão fazendo piquenique, além de conseguir revirar os lixos e pegar as sobras, exceto quando os guardas o(a) expulsam antes. Mas dessa vez deu certo, já de barriguinha levemente cheia, ele(a) decide voltar para encontarar um lugar para descansar, entretanto uma carrocinha o(a) avistou e começou a persegui-lo(a)')
                carrocinha.carrocinha(relogio, personagem)
        elif sorteio_passeio == 2:
            personagem.muda_lugar("shopping")
            shopping_passeio = randint(1,3)
            print(f'Talvez pudesse ir para a zona sul da cidade para conhecer, pois dizem que são granfinos quem vivem lá. "Talvez eu consiga algum petisco delicioso", pensa {personagem.nome}.')
            if shopping_passeio == 1:
                personagem.muda_fome(20)
                personagem.muda_energia(15)
                personagem.muda_humor(10)
                print(f'Saindo dos becos escuros, ele(a) se dirige para o centro. Prédios altos, carros e muito barulho. Na esquina ele(a) avista um prédio muito grande e com um delicioso cheiro e corre naquela direção. Aquele seria o famoso Shopping, ele(a) tenta de todas as formas entrar, entretanto é barrado pelos seguranças, e resolve somente ficar sentado admirando a grandeza daquele lugar. Até que um rapaz se aproxima e faz um afago em sua cabeça, isso deixa {personagem.nome} muito feliz, ele(a) fica mais uns minutos e resolve voltar, hoje já ganhou um carinho, pensa nosso amigo com a barriga ja roncando, mas quando ele está em retirada o rapaz que lhe fez uma afago volta e lhe da uma coxinha. Realmente foi um dia de sorte. {personagem.nome} nunca tinha comido algo tão maravilhoso.')
            elif shopping_passeio == 2:
                personagem.muda_fome(-5)
                personagem.muda_energia(-5)
                personagem.muda_humor(10)
                print(f'Entre as ruas movimentadas da cidade {personagem.nome} se assusta coma quantidade de carros que encontra, e acaba quase sendo atropelado(a), não é fácil caminhar entre tantos carros e pessoas. Entretanto {personagem.nome} avista um grande prédio onde lê a palavra "Shopping", sem ter ideia do que é ele(a) se aproxima e logo é barrado(a) pelos seguranças. Mas perto da porta uma família está parada brincando com bolas e nosso(a) amigo(a) se distrai com a cena. Uma das bolas cai perto dele e no mesmo momento a família entra num carro e deixam a bola para trás. {personagem.nome} se aproxima e pega a bola, joga para o alto e volta a pegar novamente, brincando feliz, com seu rabo em ritmo frenético. Entretanto em uma das jogadas a bola cai e sai rolando para longe e acaba entrando no bueiro, infelizmete não se tem nada o que nosso(a) amigo(a) possa fazer para recupera-la. "Mas a brincadeira foi boa, foi um dia de sorte", pensa nosso(a) amigo(a). ')
            else:
                personagem.muda_fome(15)
                personagem.muda_energia(-20)
                personagem.muda_humor(-15)
                print(f'{personagem.nome} corre em sentido ao centro na expectativa de explorar outros lugares, parendo entre uma moita e outra para fazer xixi ele(a) chega a um grandioso prédio onde de cara é barrado por seguranças, dizem que ele não pode entrar no Shopping, e {personagem.nome} não tem nem ideia do que eles estão falando, "O que será esse tal de shopping?" pensa nosso(a) amigo(a). Entretanto mal dá tempo de admirar, pois os seguranças o espantam para a rua e bem nessa hora aparece a carrocinha.')
                carrocinha.carrocinha(relogio, personagem)
                relogio.avanca_dia()
        else:
            personagem.muda_lugar("padaria")
            personagem.muda_fome(10)
            personagem.muda_energia(-20)
            personagem.muda_humor(20)
            print(f'"Padaria é uma boa", pensa {personagem.nome} com agua na boca somente com a recordação de um dia que ganhou um pãozinho recheado.')
            surpresa = randint(1,3)
            if surpresa == 1:
                personagem.muda_fome(20)
                personagem.muda_energia(10)
                personagem.muda_humor(20)
                personagem.muda_frio(20)
                print(f'{personagem.nome} corre na padaria na expectativa de ganhar alguma coisa para comer, qualquer coisa é bem vinda, pois as vezes ele(a) fica dias sem comer, então precisa aproveitar todas as oportunidades. Chegando lá seu antigo amigo padeiro o vê, e entra fechando a porta, "Talvez hoje ele esteja de mal humor, ou se esqueceu de mim?", pensa nosso(a) amigo(a). Mas um minuto depois o gentil padeiro aparece com um delicioso pão com mortadela e enrola um pano no pescoço do nosso(a) amigo(a), o gentil padeiro disse que era um cachecol para mante-lo aquecido. {personagem.nome} come num piscar de olhos e parte todo feliz e agradecido(a)')
            elif surpresa == 2:
                personagem.muda_fome(-20)
                personagem.muda_energia(-10)
                personagem.muda_humor(20)
                print(f'{personagem.nome} sabe alguns lugares para conseguir comida, ainda existem pessoas gentis que o(a) alimentam às vezes, mas existe épocas que fica dias sem comer, tendo que tomar água dos córregos, ou a água com sabão que as pessoas lavam o quintal e fica parada nas ruas. "Talvez hoje eu tenha sorte e ganhe um petisco gostoso", pensa nosso(a) amigo(a) enquanto corre para a padaria. Quando chega lá encontra o velho padeiro que esta na janela, e como te costume joga uns petisquinhos de frios para {personagem.nome} que agora parte feliz e com a barriguinha cheia. Entretanto ao virar a esquina ele ve a carrocinha que começa a persegui- lo(a)') 
                carrocinha.carrocinha(relogio, personagem)
            else:
                print(f'{personagem.nome} corre para a Padaria em busca de alguns petiscos, parando só para fazer xixi em algumas moitas para dizer que passou por lá, mas quando chega na padaria a porta está fechada, e está cheio de gente. Ele(a) tenta se aproximar mas as pessoas gritam com ele(a) e o mandam sair."Infelizmente hoje não é um dia de tanta sorte," pensa nosso(a) amigo(a).')
                
    fase1(relogio, personagem)
        
        





    