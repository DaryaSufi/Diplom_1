from Diplom_1.bun import Bun
class TestBun:
    def tets_get_name(self):
        BunForTest=Bun('Вкусная',15)
        assert BunForTest.get_name() == 'Вкусная'

    def test_get_price(self):
        BunForTest = Bun('Вкусная', 15)
        assert BunForTest.get_price() == 15
