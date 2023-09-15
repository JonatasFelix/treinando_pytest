from services.MinhaClasseUsuarios import MinhaClasseUsuarios

nome_usuario = 'João'
email_usuario = 'joao@email.com'
    
def test_adicionar_usuario(conexao_banco):
    usuarios = MinhaClasseUsuarios()
    
    # act
    novo_usuario = usuarios.adicionar_usuario(nome_usuario, email_usuario)
    print('novo_usuario', novo_usuario[0])
    lista_usuarios = usuarios.obter_usuarios()
    usuarios.fechar_conexao()
    
    
    # assert
    assert novo_usuario[1] == nome_usuario
    assert novo_usuario[2] == email_usuario
    assert novo_usuario in lista_usuarios
    

    # EXCLUIR O USUÁRIO CRIADO - BOA PRÁTICA - LIMPAR O BANCO DE DADOS APÓS O TESTE
    conexao_banco.cursor.execute("DELETE FROM usuarios WHERE id = ?", (novo_usuario[0],))
    conexao_banco.conn.commit()
    
    
def test_consultar_usuarios(conexao_banco):
    usuarios = MinhaClasseUsuarios()

    # act
    novo_usuario = usuarios.adicionar_usuario(nome_usuario, email_usuario)
    lista_usuarios = usuarios.obter_usuarios()
    usuarios.fechar_conexao()
    
    # assert
    assert novo_usuario in lista_usuarios
    
    # EXCLUIR O USUÁRIO CRIADO - BOA PRÁTICA - LIMPAR O BANCO DE DADOS APÓS O TESTE
    conexao_banco.cursor.execute("DELETE FROM usuarios WHERE id = ?", (novo_usuario[0],))
    conexao_banco.conn.commit()
    
    
def test_adicionar_endereco(conexao_banco):
    usuarios = MinhaClasseUsuarios()

    # act
    novo_usuario = usuarios.adicionar_usuario(nome_usuario, email_usuario)
    usuarios.adicionar_endereco(novo_usuario[0], 'Rua 1', 'Cidade 1', 'Estado 1', '11111111')
    id_do_usuario = novo_usuario[0]
    novo_endereco = usuarios.obter_enderecos(id_do_usuario)
    usuarios.fechar_conexao()

    # assert
    assert novo_endereco[1] == id_do_usuario
    assert novo_endereco[2] == 'Rua 1'
    assert novo_endereco[3] == 'Cidade 1'
    assert novo_endereco[4] == 'Estado 1'
    assert novo_endereco[5] == '11111111'
    
    # EXCLUIR O USUÁRIO CRIADO - BOA PRÁTICA - LIMPAR O BANCO DE DADOS APÓS O TESTE
    conexao_banco.cursor.execute("DELETE FROM usuarios_enderecos WHERE id = ?", (novo_endereco[0],))
    conexao_banco.cursor.execute("DELETE FROM usuarios WHERE id = ?", (novo_usuario[0],))
    conexao_banco.conn.commit()

    
    