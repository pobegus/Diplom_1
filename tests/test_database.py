from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:
    """ Уникальность названий булочек и ингредиентов """

    def test_unique_names_for_buns_and_ingredients(self):
        database = Database()
        buns = database.available_buns()
        ingredients = database.available_ingredients()

        bun_names = [bun.get_name() for bun in buns]
        ingredient_names = [ingredient.get_name() for ingredient in ingredients]

        assert len(bun_names) == len(set(bun_names)), "Булочки должны иметь уникальные названия"
        assert len(ingredient_names) == len(set(ingredient_names)), "Ингредиенты должны иметь уникальные названия"

    """ Получение доступных булочек """

    def test_get_available_buns(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == 3

    """ Получение доступных ингредиентов """

    def test_get_available_ingredients(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == 6

    """ Получение количества доступных соусов """

    def test_get_quantity_available_sauces(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauce) == 3

    """ Получение количества доступных начинок """

    def test_get_quantity_available_fillings(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(type_fillings) == 3

    """ Проверка цен на ингредиенты """

    def test_get_available_ingredients_prices(self):
        data_price = Database()
        ingredients = data_price.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price['hot sauce'] == 100


