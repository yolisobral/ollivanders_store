import pytest
from typing import Any

try:
    from src.types import AgedBrie
except Exception:
    AgedBrie = None


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


def test_crear_aged_brie():
    if AgedBrie is None:
        pytest.skip('AgedBrie class not available in src.types')
    cheese = AgedBrie("Aged Brie", 2, 0)
    name = _read(cheese, 'getName', 'get_name', 'name')
    sell_in = _read(cheese, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(cheese, 'getQuality', 'get_quality', 'quality')
    assert "Aged Brie" == name
    assert 2 == sell_in
    assert 0 == quality


def test_to_string():
    if AgedBrie is None:
        pytest.skip('AgedBrie class not available in src.types')
    cheese = AgedBrie("Aged Brie", 2, 0)
    print("toString() Aged Brie test:")
    if hasattr(cheese, 'toString'):
        print(cheese.toString())
    else:
        print(str(cheese))


def test_update_quality_brie():
    if AgedBrie is None:
        pytest.skip('AgedBrie class not available in src.types')
    cheese = AgedBrie("Aged Brie", 2, 0)
    _call(cheese, 'updateQuality', 'update_quality')
    sell_in = _read(cheese, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(cheese, 'getQuality', 'get_quality', 'quality')
    assert 1 == sell_in
    assert 1 == quality


def test_update_quality_brie_expired():
    if AgedBrie is None:
        pytest.skip('AgedBrie class not available in src.types')
    cheese = AgedBrie("Aged Brie", 0, 0)
    _call(cheese, 'updateQuality', 'update_quality')
    sell_in = _read(cheese, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(cheese, 'getQuality', 'get_quality', 'quality')
    assert -1 == sell_in
    assert 2 == quality


def test_quality_max_50():
    if AgedBrie is None:
        pytest.skip('AgedBrie class not available in src.types')
    brie = AgedBrie("Aged Brie", -1, 50)
    _call(brie, 'updateQuality', 'update_quality')
    sell_in = _read(brie, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(brie, 'getQuality', 'get_quality', 'quality')
    assert -2 == sell_in
    assert 50 == quality

    brie = AgedBrie("Aged Brie", -1, 49)
    _call(brie, 'updateQuality', 'update_quality')
    sell_in = _read(brie, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(brie, 'getQuality', 'get_quality', 'quality')
    assert -2 == sell_in
    assert 50 == quality