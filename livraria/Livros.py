##Livros

class Livros:
    def __init__(self, nome, autor, editora, ano):
        self.__nome = nome
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano
    def get_info(self):
        return f"Nome: {self.__nome}, Autor(a): {self.__autor}, Editora: {self.__editora}, Ano: {self.__ano}"
    def get_nome(self):
        return self.__nome
    def get_autor(self):
        return self.__autor
    def get_editora(self):
        return self.__editora
    def get_ano(self):
        return self.__ano


class Livro_fisico(Livros):
    def __init__(self, nome, autor, editora, ano, estado):
        super().__init__(nome, autor, editora, ano)
##estado novo ou usado
        self.__estado = estado
    def get_info(self):
        return f"Tipo: Livro Físico, {super().get_info()}, Estado: {self.__estado}" 
    def get_estado(self):
        return self.__estado
   

class Livro_online(Livros):
    def __init__(self, nome, autor, editora, ano):
        super().__init__(nome, autor, editora, ano)

    def get_info(self):
        return f"Tipo: E-Book, {super().get_info()}"
