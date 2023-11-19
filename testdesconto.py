from main2 import Produto

# Teste usando o pytest
def test_desconto():
    # Criando instâncias da classe Produto
    p1 = Produto('Creatina', 'R$20')
    p2 = Produto('Camiseta', 70)

    # Aplicando desconto e verificando se o preço foi ajustado corretamente
    p1.desconto(20)
    assert p1.preco == 16.0  # substitua conforme a lógica do método desconto

    p2.desconto(40)
    assert p2.preco == 42.0  # substitua conforme a lógica do método desconto


