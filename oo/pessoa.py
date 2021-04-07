class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    chamas = Pessoa(nome='chamas')
    Rodrigo = Pessoa(chamas, nome='Rodrigo')
    print(Pessoa.cumprimentar(Rodrigo))
    print(id(Rodrigo))
    print(Rodrigo.cumprimentar())
    print(Rodrigo.nome)
    print(Rodrigo.idade)
    print(Rodrigo.filhos)
    for filho in Rodrigo.filhos:
        print(filho.nome)