from Arcevo import *
from Livros import *
from Pessoas import *
from flask import Flask, render_template

Livro1 = Livro_fisico("Nome1","Autor1","editora1",2000,"novo")
Livro2 = Livro_online("Nome2","Autor2","editora2",2000)
Livro3 = Livro_fisico("Nome3","Autor3","editora3",2000,"usado")
Livro4 = Livro_online("Nome4","Autor4","editora4",2000)

Pessoa1 = Cliente("Nome1", "email1","senha1",2)
Pessoa2 = Dono("Nome2","email2", "senha2", 4)

def exibir(objeto):
    print(objeto.get_info())


e = Estoque()

e.adicionar_livro(Livro1)
e.adicionar_livro(Livro3)
e.adicionar_livro(Livro2)   

def is_livro_fisico(livro):
    return isinstance(livro, Livro_fisico)

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('livraria.html', livros = e.lista_livros, is_livro_fisico = is_livro_fisico)

if __name__ == '__main__':
    app.run(debug = True)


#exibir(Livro1)
#exibir(Livro2)
#exibir(Livro3)
#exibir(Livro4)
#exibir(Pessoa1)
#exibir(Pessoa2)