from funcionarioProjeto import FuncionarioProjeto

class Projeto:
    def __init__(self, id: str, nome: str, descricao: str):
        self.id: str = id
        self.nome: str = ' '.join(map(lambda x: x.capitalize(), nome.split()))
        self.descricao: str = descricao
        self.funcionarios: list[FuncionarioProjeto] = []
    
    def __str__(self):
        return f'{self.id} {self.nome}'