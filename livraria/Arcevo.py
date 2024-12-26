##Arcevo
from Livros import *

class Arcevo:
    def __init__(self):
       self.lista_livros = []
       
    def get_info(self, livro):
        self.__livro = livro
        if type(self.__livro) == Livro_fisico:
            b = Livro_fisico.get_info(self.__livro)
        else:
            b = Livro_online.get_info(self.__livro)
        return b  
    
    def adicionar_livro(self,livro):
        self.__livro = livro
        if type(self.__livro) == Livro_fisico:
            assert isinstance (self.__livro, Livro_fisico)
            self.lista_livros.append(livro)
        else:
            assert isinstance (self.__livro, Livro_online)
            self.lista_livros.append(livro)

    def remover_livro(self,livro):
        self.__livro = livro
        if type(self.__livro) == Livro_fisico:
            assert isinstance (self.__livro, Livro_fisico)
            self.lista_livros.remove(livro)
        else:
            assert isinstance (self.__livro, Livro_online)
            self.lista_livros.remove(livro)        

    def printLivros(self):
        for p in self.lista_livros:
            if type(p) == Livro_online:
                print(f"Nome: {p.get_nome()}, Autor(a): {p.get_autor()}, Editora: {p.get_editora()}, Ano: {p.get_ano()}") 
  ##              print(f"Nome: {p.get_nome()}, Autor(a): {p.get_autor()}, Editora: {p.get_editora()}, Ano: {p.get_ano()},Estado: {p.get_estado()}") 
            else:
   ##             print(f"Nome: {p.get_nome().__nome}, Autor(a): {p.get_autor().__autor}, Editora: {p.get_editora().__editora}, Ano: {p.get_ano().__ano}") 
                print(f"Nome: {p.get_nome()}, Autor(a): {p.get_autor()}, Editora: {p.get_editora()}, Ano: {p.get_ano()},Estado: {p.get_estado()}")   

class Carrinho(Arcevo):
    def __init__(self, estoque):
        self.__estoque = estoque
        super().__init__() 

    def adicionar_livro(self, livro):
        if livro in self.__estoque.lista_livros:  # Verifica se o livro está no estoque
            self.__estoque.remover_livro(livro)  # Remove do estoque
            super().adicionar_livro(livro)  # Adiciona no carrinho
        else:
            print(f"O livro '{livro.get_nome()}' não está disponível no estoque.")  # Caso o livro não exista no estoque
              

class Estoque(Arcevo):
    def __init__(self):
        super().__init__() 

    def adicionar_livro(self, livro):
        return super().adicionar_livro(livro) 

    def remover_livro(self, livro):
        return super().remover_livro(livro)          

#arcevo = Arcevo()

#arcevo.adicionar_livro(Livro1)
#arcevo.adicionar_livro(Livro2)
#arcevo.adicionar_livro(Livro3)
#arcevo.printLivros()
#arcevo.remover_livro(Livro2)
#arcevo.printLivros()


##e = Estoque()

#e.adicionar_livro(Livro1)
#e.adicionar_livro(Livro3)
#e.adicionar_livro(Livro2)

#e.printLivros()

#c = Carrinho(e)

#c.adicionar_livro(Livro2)

#c.printLivros()
#e.printLivros()

