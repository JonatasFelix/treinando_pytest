import pytest
from db.cria_tabelas import criar_tabelas
from db.conexao_banco import ConexaoBanco



@pytest.fixture(autouse=True)
def inicializar_servico():
    criar_tabelas()
    
@pytest.fixture(scope="module")
def conexao_banco():
    conn = ConexaoBanco('banco.db')
    yield conn
    conn.fechar_conexao()

from services import MinhaClasseUsuarios
