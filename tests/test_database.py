from Diplom_1.database import Database
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        Dt=Database()
        assert (len(Dt.available_buns()), 3)
        assert (Dt.available_buns()[0].name, "black bun")
        assert (Dt.available_buns()[0].price, 100)
        assert (Dt.available_buns()[1].name, "white bun")
        assert (Dt.available_buns()[1].price, 200)
        assert (Dt.available_buns()[2].name, "red bun")
        assert (Dt.available_buns()[2].price, 300)
    def test_available_ingredients(self):
        Dt = Database()
        assert (len(Dt.available_ingredients()), 6)
        assert (Dt.available_ingredients()[0].type, INGREDIENT_TYPE_SAUCE)
        assert (Dt.available_ingredients()[0].name, "hot sauce")
        assert (Dt.available_ingredients()[0].price, 100 )
        assert (Dt.available_ingredients()[0].type, INGREDIENT_TYPE_SAUCE)
        assert (Dt.available_ingredients()[0].name, "sour cream")
        assert (Dt.available_ingredients()[0].price, 200)
        assert (Dt.available_ingredients()[0].type, INGREDIENT_TYPE_SAUCE)
        assert (Dt.available_ingredients()[0].name, "chili sauce")
        assert (Dt.available_ingredients()[0].price, 300)
        assert (Dt.available_ingredients()[0].type, INGREDIENT_TYPE_FILLING)
        assert (Dt.available_ingredients()[0].name, "cutlet")
        assert (Dt.available_ingredients()[0].price, 100)
        assert (Dt.available_ingredients()[0].type, INGREDIENT_TYPE_FILLING)
        assert (Dt.available_ingredients()[0].name, "dinosaur")
        assert (Dt.available_ingredients()[0].price, 200)
        assert (Dt.available_ingredients()[0].type, INGREDIENT_TYPE_FILLING)
        assert (Dt.available_ingredients()[0].name, "sausage")
        assert (Dt.available_ingredients()[0].price, 300)


