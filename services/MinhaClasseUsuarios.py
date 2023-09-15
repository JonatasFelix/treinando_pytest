from db.conexao_banco import ConexaoBanco

class MinhaClasseUsuarios:
    def __init__(self):
        self.conn = ConexaoBanco('banco.db')

    def adicionar_usuario(self, nome, email):
        self.conn.cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        self.conn.conn.commit()
        # retorna o usuário criado com todos os dados
        self.conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?", (self.conn.cursor.lastrowid,))
        return self.conn.cursor.fetchone()

    def obter_usuarios(self):
        self.conn.cursor.execute("SELECT * FROM usuarios")
        return self.conn.cursor.fetchall()

    def fechar_conexao(self):
        self.conn.fechar_conexao()
        
    def adicionar_endereco(self, usuario_id, rua, cidade, estado, cep):
        self.conn.cursor.execute("INSERT INTO usuarios_enderecos (usuario_id, rua, cidade, estado, cep) VALUES (?, ?, ?, ?, ?)", (usuario_id, rua, cidade, estado, cep))
        self.conn.conn.commit()
        
        self.conn.cursor.execute("SELECT * FROM usuarios_enderecos WHERE id = ?", (self.conn.cursor.lastrowid,))
        return self.conn.cursor.fetchone()
        
    def obter_enderecos(self, usuario_id):
        self.conn.cursor.execute("SELECT * FROM usuarios_enderecos WHERE usuario_id = ?", (usuario_id,))
        return self.conn.cursor.fetchone()