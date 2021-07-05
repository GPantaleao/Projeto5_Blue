from random import randint

def fase1(relogio, personagem, opcao_escolhida1):
    print(f'São {str(relogio)}, {personagem.nome} você está {personagem.lugar}.')
    print(personagem)

    if opcao_escolhida1 != 1:
        print('1- Procurar comida')
    if opcao_escolhida1 != 2:
        print('2- Procurar alguém para brincar')
    if opcao_escolhida1 != 3:
        print('3- Procurar um abrigo')
    if opcao_escolhida1 != 4:
        print('4- Voltar a dormir')
    print('5- Explorar a região')
    
    acao2 = input('Qual será sua próxima ação?')
    if acao2 == 5:
        sorteio_passeio = randint(1,3)
        relogio.avanca_tempo(50)  
        if sorteio_passeio == 1:
            personagem.muda_fome(20)
            personagem.muda_energia(-20)
            personagem.humor(-10)
            print('Você fez um passeio pelo parque, que não foi muito bom.Você encontrou um cachorro hostil.')
            cachorro_hostil = randint(1,2)
            if cachorro_hostil == 1:
                print('O cachorro correu atrás de você.')
            else:
                print('O cachorro tentou de morder, mas você escapou.') 
        elif sorteio_passeio == 2:
            shopping_passeio = randint(1,3)
            personagem.muda_fome(20)
            personagem.muda_energia(-20)
            personagem.humor(-10)
            print('Você passeiou no shopping e foi muito divertido. Você encontrou um pessoa legal.')
            if shopping_passeio == 1:
                print('Você encontrou uma pessoa que deu uma sobra, e um carinho na cabeça.')
            elif shopping_passeio == 2:
                print('Você encontrou uma pessoa que te deu uma bolinha, mas ela caiu no buraco e você ficou triste.')
            else:
                print('Você foi expulso pelo segurança.')
        else:
            personagem.muda_fome(10)
            personagem.muda_energia(-20)
            personagem.humor(20)
            print('Você encontro uma padaria e teve uma surpresa.')
            surpresa = randint(1,2)
            if surpresa == 1:
                print('O dono padaria te deu um pão.')
            else:
                print('O dono da padaria te um pão com mortadela.') 

    print(personagem)
