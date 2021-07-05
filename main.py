
from classes.personagemCao import Personagem
from classes.relogio import Relogio
from fases.introducao import Introducao
from fases.fases import fase1

if __name__ == '__main__':
    intro = Introducao()
    # intro.executar()   NÃO ESQUECER DE TIRAR DEPOIS
    relogio = Relogio()
    nome = input('Digite o nome do seu cão amigo(a): ')
    personagem = Personagem(nome)
    fase1(relogio, personagem)

