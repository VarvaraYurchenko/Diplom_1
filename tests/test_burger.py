import pytest
from unittest.mock import Mock

from praktikum.burger import Burger

from data import TEST_BUN, TEST_SAUCE, TEST_FILLING, PRICE_TEST_CASE


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize("ingredient_type", [TEST_SAUCE["type"], TEST_FILLING["type"]])
    def test_add_ingredient(self, ingredient_type, mock_ingredients):
        burger = Burger()
        ingredient = mock_ingredients[ingredient_type]

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_filling]

    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    @pytest.mark.parametrize(
        "bun_price, ing1_price, ing2_price, expected_price",
        PRICE_TEST_CASE
    )
    def test_get_price(self, bun_price, ing1_price, ing2_price, expected_price, mock_bun):
        mock_bun.get_price.return_value = bun_price

        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = ing1_price

        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = ing2_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_receipt = (
            f"(==== {TEST_BUN['name']} ====)\n"
            f"= {TEST_SAUCE['type'].lower()} {TEST_SAUCE['name']} =\n"
            f"= {TEST_FILLING['type'].lower()} {TEST_FILLING['name']} =\n"
            f"(==== {TEST_BUN['name']} ====)\n"
            f"\n"
            f"Price: {burger.get_price()}"
        )

        assert burger.get_receipt() == expected_receipt
