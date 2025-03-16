import pytest
from Diplom_1.ingredient import Ingredient
from Diplom_1.bun import Bun
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
@pytest.fixture()
def create_sauce():
    sauce=Ingredient(INGREDIENT_TYPE_SAUCE,'Соус Spicy-X', 90)
    return sauce

@pytest.fixture()
def create_filling():
    filling=Ingredient(INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337)
    return filling

@pytest.fixture()
def create_bun():
    bun=Bun('Краторная булка N-200i', 1255)
    return bun



