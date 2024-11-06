from praktikum.bun import Bun

class TestBun:

    """ Получение наименования """
    def test_get_correct_name(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_name() == 'Краторная булка N-200i'

    """ Получение прайса """
    def test_get_correct_price(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255
