##Pessoas

class Pessoas():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_info(self):
        return f"Nome: {self.nome}, E-mail: {self.email}, Senha: {self.senha}"
    
class Cliente(Pessoas):
    def __init__(self, nome, email, senha, carrinho):
        super().__init__(nome, email, senha)
        self.carrinho = carrinho

    def get_info(self):
        return f"{super().get_info()}, Seu carrinho: {self.carrinho}"    
    
class Dono(Pessoas):
    def __init__(self, nome, email, senha, estoque):
        super().__init__(nome, email, senha)
        self.estoque = estoque

    def get_info(self):
        return f"{super().get_info()}, Seu estoque: {self.estoque}"        
