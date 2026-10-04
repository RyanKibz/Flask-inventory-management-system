from unittest.mock import patch, Mock
from external_api import find_product


@patch("external_api.requests.get")
def test_find_product(mock_get):
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Milk",
            "brands": "Test Brand",
            "ingredients_text": "Milk"
        }
    }
    mock_get.return_value = response

    product = find_product("123456")

    assert product["product_name"] == "Test Milk"
    assert product["brand"] == "Test Brand"
    assert product["barcode"] == "123456"