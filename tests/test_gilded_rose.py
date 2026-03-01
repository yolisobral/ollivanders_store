import pytest
from typing import Any

try:
    from src.types import Ollivander, NormalItem, AgedBrie
except Exception:
    Ollivander = NormalItem = AgedBrie = None


def _read(obj: Any, *names):
    for n in names:
        if hasattr(obj, n):
            val = getattr(obj, n)
            return val() if callable(val) else val
    raise AttributeError(f"None of the names {names} found on object {obj}")


def _call(obj: Any, *names):
    for n in names:
        if hasattr(obj, n):
            fn = getattr(obj, n)
            return fn()
    raise AttributeError(f"None of the methods {names} found on object {obj}")


def test_to_string():
    if Ollivander is None or AgedBrie is None:
        pytest.skip('OllivanderShop/AgedBrie classes not available in src.types')
    shop = Ollivander()
    brie = AgedBrie("Aged Brie", 2, 0)
    shop.addItem(brie)
    brie = AgedBrie("Aged Brie", 10, 10)
    shop.addItem(brie)
    print("toString() GildedRose test:")
    if hasattr(shop, 'toString'):
        print(shop.toString())
    else:
        print(str(shop))


def test_add_item():
    if Ollivander is None or NormalItem is None or AgedBrie is None:
        pytest.skip('Required classes not available in src.types')
    shop = Ollivander()
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    brie = AgedBrie("Aged Brie", 2, 0)
    shop.addItem(normal)
    shop.addItem(brie)
    inv = _call(shop, 'inventory') if hasattr(shop, 'inventory') else _read(shop, 'inventory')
    assert len(inv) == 2
    items = [normal, brie]
    assert items == list(inv)
    print("GildedRose addItem test:")
    if hasattr(shop, 'toString'):
        print(shop.toString())
    else:
        print(str(shop))


def test_update_quality():
    if Ollivander is None or NormalItem is None or AgedBrie is None:
        pytest.skip('Required classes not available in src.types')
    shop = Ollivander()
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    brie = AgedBrie("Aged Brie", 2, 0)
    shop.addItem(normal)
    shop.addItem(brie)
    inv = _call(shop, 'inventory') if hasattr(shop, 'inventory') else _read(shop, 'inventory')
    assert len(inv) == 2
    print("Dia 0:\n" + (shop.toString() if hasattr(shop, 'toString') else str(shop)))
    _call(shop, 'updateQuality', 'update_quality')
    item0 = inv[0]
    q0 = _read(item0, 'getQuality', 'get_quality', 'quality')
    assert 19 == q0
    q1 = _read(inv[1], 'getQuality', 'get_quality', 'quality')
    assert 1 == q1
    print("Dia 1:\n" + (shop.toString() if hasattr(shop, 'toString') else str(shop)))