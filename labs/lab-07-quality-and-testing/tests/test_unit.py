import pytest
from app.main import Item

def test_valid_item_model():
    item = Item(id=1, name="Widget", price=19.99)
    assert item.id == 1
    assert item.name == "Widget"
    assert item.price == 19.99

def test_invalid_price():
    with pytest.raises(ValueError):
        Item(id=2, name="Free Stuff", price=-5.00)
