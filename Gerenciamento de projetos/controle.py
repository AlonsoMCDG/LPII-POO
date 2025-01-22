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
    
    def listar_projetos(self):
        print('Projetos ativos:')
        for projeto in self.projetos:
            print(projeto)
    
    def listar_funcionarios(self):
        print('Funcionários cadastrados:')
        for funcionario in self.funcionarios:
            print(funcionario)
    