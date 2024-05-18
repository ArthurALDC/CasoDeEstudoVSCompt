class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
class listaP:
    def __init__(self):
        self.lista = []
    
    def inserir(self,produto,indice):
        if indice < 0 or produto > len(self.lista):
            print ("Posição inválida")
            return 
        self.lista.insert(indice,produto)
    
    def remover(self,indice):
        if indice < 0 or indice > len(self.lista):
            print("Não tem como remover por ser uma posição inválida")
            return
        del self.lista[indice]
        
    def localizar(self, produto):
        for i, p in enumerate(self.lista):
            if p == produto:
                return 1
        return -1
    
    def limpar(self):
        self.product = []



            