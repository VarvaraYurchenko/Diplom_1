import pytest
from unittest.mock import Mock
from data import TEST_BUN, TEST_SAUCE, TEST_FILLING


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = TEST_BUN["name"]
    mock.get_price.return_value = TEST_BUN["price"]
    return mock


@pytest.fixture
def mock_sauce():
    mock = Mock()
    mock.get_type.return_value = TEST_SAUCE["type"]
    mock.get_name.return_value = TEST_SAUCE["name"]
    mock.get_price.return_value = TEST_SAUCE["price"]
    return mock


@pytest.fixture
def mock_filling():
    mock = Mock()
    mock.get_type.return_value = TEST_FILLING["type"]
    mock.get_name.return_value = TEST_FILLING["name"]
    mock.get_price.return_value = TEST_FILLING["price"]
    return mock