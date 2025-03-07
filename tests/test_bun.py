from Diplom_1.bun import Bun
class TestBun:
    def tets_get_name(self, create_bun):
        Bun=create_bun
        assert Bun.get_name() == 'Краторная булка N-200i'

    def test_get_price(self, create_bun):
        Bun = create_bun
        assert Bun.get_price() == 1255
