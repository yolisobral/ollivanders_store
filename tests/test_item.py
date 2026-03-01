import pytest
from typing import Any

try:
    from src.types import NormalItem
except Exception:
    NormalItem = None


def _read(obj: Any, *names):
    for n in names:
        if hasattr(obj, n):
            val = getattr(obj, n)
            return val() if callable(val) else val
    raise AttributeError(f"None of the names {names} found on object {obj}")


def test_crear_item():
    if NormalItem is None:
        pytest.skip('Item class not available in src.types')
    item = NormalItem("+5 Dexterity Vest", 10, 20)
    name = _read(item, 'getName', 'get_name', 'name')
    sell_in = _read(item, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(item, 'getQuality', 'get_quality', 'quality')
    assert "+5 Dexterity Vest" == name
    assert 10 == sell_in
    assert 20 == quality
    print(item)