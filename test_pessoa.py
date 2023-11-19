from main import Pessoa


def test_get_ano_nascimento():
    p1 = Pessoa('Helder', 34)
    p2 = Pessoa('Kevin', 11)
    p3 = Pessoa('Taciane', 30)

    assert p1.get_ano_nascimento() == 1989  # objeto.metodo
    assert p2.get_ano_nascimento() == 2012
    assert p3.get_ano_nascimento() == 1993
