import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()

    def fechar_conexao(self):
        self.conn.close()