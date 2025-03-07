import pytest
from Diplom_1.burger import Burger
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock

class TestBurger:
    create_bun = ('Краторная булка N-200i', 1255)
    create_sauce  = (INGREDIENT_TYPE_SAUCE,'Соус Spicy-X', 90)
    create_filling = (INGREDIENT_TYPE_FILLING,'Мясо бессмертных моллюсков Protostomia', 1337)
    mock_bun = Mock()
    mock_bun.get.return_value = create_bun
    mock_sauce = Mock()
    mock_sauce.get.return_value = create_sauce
    mock_filling = Mock()
    mock_filling.get.return_value = create_filling
    def test_set_buns(self):
      BurgerForTest=Burger()
      BunForTest = self.mock_bun
      BurgerForTest.set_buns(BunForTest)
      assert BurgerForTest.bun == BunForTest
    @pytest.mark.parametrize(
    'ingridients', [
        mock_sauce,
        mock_filling
    ])
    def test_add_ingredient(self, ingridients):
        BurgerForTest = Burger()
        BurgerForTest.add_ingredient(ingridients)
        assert ingridients in BurgerForTest.ingredients
    def test_remove_ingredient(self):
        BurgerForTest = Burger()
        BurgerForTest.add_ingredient(self.mock_sauce)
        BurgerForTest.remove_ingredient(0)
        assert len(BurgerForTest.ingredients) == 0
    def test_move_ingredient(self):
       BurgerForTest = Burger()
       BurgerForTest.add_ingredient(self.mock_sauce)
       BurgerForTest.add_ingredient(self.mock_filling)
       BurgerForTest.move_ingredient(0,3)
       indexes = [index for index, _ in enumerate(BurgerForTest.ingredients)]
       assert indexes  == [1,3]

    def test_get_price(self, create_sauce, create_filling, create_bun):
        BurgerForTest = Burger()
        BurgerForTest.add_ingredient(create_sauce)
        BurgerForTest.add_ingredient(create_filling)
        BunForTest = create_bun
        BurgerForTest.set_buns(BunForTest)
        price = BurgerForTest.get_price()
        assert price == 2772
    def test_get_receipt(self, create_sauce, create_filling, create_bun, capsys):
        BurgerForTest = Burger()
        BurgerForTest.add_ingredient(create_sauce)
        BurgerForTest.add_ingredient(create_filling)
        BunForTest = create_bun
        BurgerForTest.set_buns(BunForTest)
        BurgerForTest.get_receipt()
        assert 'Краторная булка N-200i' in BurgerForTest.get_receipt()