# 3) Crie um sistema para gerencias projetos e 
# funcionários. O sistema deve permitir que:
#    -  Um funcionário participe de vários projetos.
#    -  Um projeto possa ter vários funcionários.
#    Os funcionários têm as seguintes características: 
# ID único, nome e cargo. Cada projeto tem: id do 
# projeto, nome e descrição. As informações sobre a 
# associação entre um funcionário e um projeto 
# incluem: o papel do funcionário no projeto (ex.: 
# "Desenvolvedor", "Gerente", "Designer") e a data de 
# início no projeto.
#    Implemente as seguiintes funcionalidades:
#    -  Crie métodos para adicionar funcionários e 
# projetos ao sistema.
#    -  Adicione funcionários a projetos, 
# especificando o papel e a data de início.
#    -  Liste todos os projetos em que um 
# funcionário está envolvido, junto com o papel 
# desempenhado e a data de início.
#    -  Liste todos os funcionários de um projeto, 
# incluindo seus cargos, papéis e datas de início
#    Permita remover a associação entre um funcionário
# e um projeto

from funcionario import Funcionario
from projeto import Projeto

if __name__ == '__main__':
    func1 = Funcionario('001-A', 'Alan Santana', 'CEO')
    func2 = Funcionario('102-J', 'Joaquim Augusto', 'QA')
    
    proj1 = Projeto('20250400013', 'Web Project', 'Desenvolvimento de uma aplicação para a Web')
    
    
    