from projeto import Projeto
from funcionario import Funcionario

class Controle:
    def __init__(self):
        self.funcionarios: list[Funcionario] = []
        self.projetos: list[Projeto] = []
    
    def novo_funcionario(self, id: str, nome: str, cargo: str):
        self.funcionarios.append(Funcionario(id, nome, cargo))
    
    def novo_projeto(self, id: str, nome: str, descricao: str = 'Sem descrição.'):
        self.projetos.append(Projeto(id, nome, descricao))
    