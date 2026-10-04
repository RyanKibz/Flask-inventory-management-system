from unittest.mock import patch, Mock
from cli import view_inventory, delete_item


@patch("cli.requests.get")
def test_view_inventory(mock_get, capsys):
    response = Mock()
    response.json.return_value = [{"id": 1, "product_name": "Milk"}]
    mock_get.return_value = response

    view_inventory()

    output = capsys.readouterr()
    assert "Milk" in output.out


@patch("cli.requests.delete")
@patch("builtins.input", return_value="1")
def test_delete_item(mock_input, mock_delete, capsys):
    response = Mock()
    response.json.return_value = {"message": "Item deleted"}
    mock_delete.return_value = response

    delete_item()

    output = capsys.readouterr()
    assert "Item deleted" in output.out