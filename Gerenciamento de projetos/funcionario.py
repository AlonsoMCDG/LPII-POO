from funcionarioProjeto import FuncionarioProjeto

class Funcionario:
    def __init__(self, id: str, nome: str, cargo: str):
        self.id: str = id
        self.nome: str = nome
        self.cargo: str = cargo
        self.projetos: list[FuncionarioProjeto] = []
    
    
    def __str__(self):
        return f'{self.id} {self.nome}'