from conexao_banco import conectar

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            senha TEXT
        )
    ''')

    conexao.commit()
    conexao.close()
    
    
if __name__ == "__main__":
    criar_tabelas()