# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
'''

class Ball:
    def __init__(self, color="unknown", circunf=0, material="unknown"):
        self.color = color
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input("Deseja mudar a cor atual {}? [s/n]".format(self.color))

        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.color = nova_cor
        else:
            print("Ok a cor continua {}".format(self.color))

    def mostraCor(self):
        print("\nA cor atual é {}".format(self.color))


def main():
    bola01 = Ball("azul", 5, "metal")

    while True:
        bola01.mostraCor()
        bola01.trocaCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola01.mostraCor()


main()

'''


'''Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''

'''
class Retangulo:
    def __init__(self,comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor_comprimento(self,novo_comprimento):
        self.comprimento = novo_comprimento

    def mudar_valor_largura(self, nova_largura):
        self.largura = nova_largura

    def retornar_valor_lados(self):
        print(f'{self.comprimento}cm, {self.largura}cm')

    def calcular_area(self):
        area = self.largura * self.comprimento
        print(f'{area}m quadrados')     #se retirar o comando print de dentro da função, as linhas que chamarem esta função deverão estar inseridas no comando print
        return area                     #precisei adicionar o return pois na f string da linha 53 resultava em um valor None


    def calcular_perimetro(self):
        perimetro = 2*self.largura + 2*self.comprimento
    #print(f'{perimetro}m')             #se retirar o comando print, as linhas com esta funçao deverão estar inseridas no comando print
        return perimetro                #precisei adicionar o return pois na f string da linha 53 resultava em um valor None


r1 = Retangulo(4,10)

print(r1.__dict__)
r1.retornar_valor_lados()
r1.calcular_area()                  #print(r1.calcular_area())
r1.calcular_perimetro()             #print (r1.calcular_perimetro())

r1.mudar_valor_comprimento(3)
r1.mudar_valor_largura(12)
print(r1.__dict__)
r1.retornar_valor_lados()
r1.calcular_area()                   #print(r1.calcular_area())
r1.calcular_perimetro()              #print (r1.calcular_perimetro())

x = float(input('selecione o comprimento do local:' ))
y = float(input('selecione a largura do local:' ))

local = Retangulo(x,y)

print (f'serão necessários {local.calcular_area()}m quadrado(s) de piso e {local.calcular_perimetro()}m de rodapés para suprir o local')

'''


'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.
'''
'''
class ContaCorrente:

    def __init__(self,numero_conta, nome_correntista,saldo=0):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self,valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo -= valor_saque
        return self.saldo

CC1 = ContaCorrente(250,'Yann Schmitt')

print (CC1.__dict__)

CC1.deposito(25)
print (CC1.__dict__)

CC1.saque(10)
print (CC1.__dict__)
'''
