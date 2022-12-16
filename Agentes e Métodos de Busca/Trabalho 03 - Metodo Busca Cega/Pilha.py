import numpy as np

#Nome: Matheus Conzatti de Souza
#Turma: Engenharia de Computação

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1

        # Mudança do tipo de array
        self.__valores = np.empty(self.__capacidade, dtype=object)

    def cheia(self):
        if self.__topo == self.__capacidade - 1:  # Mostra o ultimo elemento que entrou na pilha
            return True
        else:
            return False

    def vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        # Verifica se a pilha está cheia, se a pilha não estiver cheia adiciona um elemento
        if self.cheia():
            print('A pilha esta cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        # Retorna o elemento que foi desempilhado
        if self.vazia():
            print('A pilha eta vazia')
            return None
        else:
            temp = self.__valores[self.__topo]
            self.__topo -= 1
            return temp

    def verTopo(self):
        if self.__topo != -1:  # Retorna o primerio elemento da pilha
            return self.__valores[self.__topo]
        else:
            return -1
