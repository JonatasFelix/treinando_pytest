from .conexao_banco import ConexaoBanco

def criar_tabelas():
    conn = ConexaoBanco('banco.db')
    conn.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
            senha TEXT
        )
    ''')
    
    conn.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios_enderecos (
            id INTEGER PRIMARY KEY,
            usuario_id INTEGER,
            rua TEXT,
            cidade TEXT,
            estado TEXT,
            cep TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    
    conn.cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            preco REAL,
            descricao TEXT,
            quantidade INTEGER -- Adicionando o campo 'quantidade'
        )
    ''')
    
    produtos_ficticios = [
        ("Batom Matte Vermelho Intenso", 15.99, "Batom de longa duração com acabamento matte para lábios vibrantes.", 20),
        ("Paleta de Sombras Neutras", 29.99, "Paleta de sombras em tons neutros para criar looks versáteis e elegantes.", 15),
        ("Máscara de Cílios Alongadora", 12.50, "Máscara de cílios que proporciona alongamento e volume para um olhar marcante.", 25),
        ("Base Líquida de Cobertura Natural", 18.99, "Base líquida que oferece cobertura natural para uma pele impecável.", 30),
        ("Perfume Floral Suave", 34.99, "Perfume com fragrância floral suave e delicada.", 10),
        ("Esmalte Nude Clássico", 7.99, "Esmalte de cor nude elegante para unhas bem cuidadas.", 50),
        ("Pó Compacto com Efeito Matte", 14.50, "Pó compacto que controla a oleosidade e proporciona acabamento matte.", 20),
        ("Creme Hidratante Iluminador", 22.99, "Creme hidratante que proporciona luminosidade à pele, deixando-a radiante.", 18),
        ("Lápis de Olho à Prova d'Água", 9.50, "Lápis de olho de longa duração, resistente à água e de fácil aplicação.", 35),
        ("Kit de Pincéis Profissionais", 39.99, "Conjunto de pincéis de maquiagem profissionais para uma aplicação precisa e uniforme.", 12),
    ]
    conn.conn.commit()
    conn.fechar_conexao()
