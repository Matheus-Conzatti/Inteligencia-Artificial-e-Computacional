from Pilha import *

class Vertice: 
    def __init__(self, rotulo): 
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def addAdjacente(self, adjacente):  
        self.adjacentes.append(adjacente)

    def mostraAdjacentes(self): 
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

class BuscaProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)

    def buscar(self):
        topo = self.pilha.verTopo()
        print('Topo: {}'.format(topo.rotulo))
        for adjacente in topo.adjacentes:
            print('Topo e {} ja visitada? {}'.format(topo.rotulo,adjacente.vertice.rotulo, adjacente.vertice.visitado))
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print('Empilhar {}'.format(adjacente.vertice.rotulo))
                self.buscar()
        print('Desempilhou: {}'.format(self.pilha.desempilhar().rotulo))
        print()

class Grafo:
    arad = Vertice('Arad')
    zerind = Vertice('Zerind')
    oradea = Vertice('Oradea')
    sibiu = Vertice('Sibiu')
    timisoara = Vertice('Timisoara')
    lugoj = Vertice('Lugoj')
    mehadia = Vertice('Mehadia')
    dobreta = Vertice('Dobreta')
    craiova = Vertice('Craiova')
    rimnicu = Vertice('Rimnicu')
    fagaras = Vertice('Fagaras')
    pitesti = Vertice('Pitesti')
    bucharest = Vertice('Bucharest')
    giurgiu = Vertice('Giurgiu')

    arad.addAdjacente(Adjacente(zerind, 75))
    arad.addAdjacente(Adjacente(sibiu, 140))
    arad.addAdjacente(Adjacente(timisoara, 118))

    zerind.addAdjacente(Adjacente(arad, 75))
    zerind.addAdjacente(Adjacente(oradea, 71))

    oradea.addAdjacente(Adjacente(zerind, 71))
    oradea.addAdjacente(Adjacente(sibiu, 151))

    sibiu.addAdjacente(Adjacente(oradea, 151))
    sibiu.addAdjacente(Adjacente(arad, 140))
    sibiu.addAdjacente(Adjacente(fagaras, 99))
    sibiu.addAdjacente(Adjacente(rimnicu, 80))

    timisoara.addAdjacente(Adjacente(arad, 118))
    timisoara.addAdjacente(Adjacente(lugoj, 111))

    lugoj.addAdjacente(Adjacente(timisoara, 111))
    lugoj.addAdjacente(Adjacente(mehadia, 70))

    mehadia.addAdjacente(Adjacente(lugoj, 70))
    mehadia.addAdjacente(Adjacente(dobreta, 75))

    dobreta.addAdjacente(Adjacente(mehadia, 75))
    dobreta.addAdjacente(Adjacente(craiova, 120))

    craiova.addAdjacente(Adjacente(dobreta, 120))
    craiova.addAdjacente(Adjacente(pitesti, 138))
    craiova.addAdjacente(Adjacente(rimnicu, 146))

    rimnicu.addAdjacente(Adjacente(craiova, 146))
    rimnicu.addAdjacente(Adjacente(sibiu, 80))
    rimnicu.addAdjacente(Adjacente(pitesti, 97))

    fagaras.addAdjacente(Adjacente(sibiu, 99))
    fagaras.addAdjacente(Adjacente(bucharest, 211))

    pitesti.addAdjacente(Adjacente(rimnicu, 97))
    pitesti.addAdjacente(Adjacente(craiova, 138))
    pitesti.addAdjacente(Adjacente(bucharest, 101))

    bucharest.addAdjacente(Adjacente(fagaras, 211))
    bucharest.addAdjacente(Adjacente(pitesti, 101))
    bucharest.addAdjacente(Adjacente(giurgiu, 90))

grafo = Grafo()
busca_profundidade = BuscaProfundidade(grafo.arad)
busca_profundidade.buscar()