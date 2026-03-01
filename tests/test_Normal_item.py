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


def _call(obj: Any, *names):
    for n in names:
        if hasattr(obj, n):
            fn = getattr(obj, n)
            return fn()
    raise AttributeError(f"None of the methods {names} found on object {obj}")


def test_crear_normal_item():
    if NormalItem is None:
        pytest.skip('NormalItem class not available in src.types')
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    name = _read(normal, 'getName', 'get_name', 'name')
    sell_in = _read(normal, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(normal, 'getQuality', 'get_quality', 'quality')
    assert "+5 Dexterity Vest" == name
    assert 10 == sell_in
    assert 20 == quality


def test_to_string():
    if NormalItem is None:
        pytest.skip('NormalItem class not available in src.types')
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    if hasattr(normal, 'toString'):
        print(normal.toString())
    else:
        print(str(normal))


def test_update_quality_normal_item():
    if NormalItem is None:
        pytest.skip('NormalItem class not available in src.types')
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    _call(normal, 'updateQuality', 'update_quality')
    sell_in = _read(normal, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(normal, 'getQuality', 'get_quality', 'quality')
    assert 9 == sell_in
    assert 19 == quality


def test_update_quality_normal_item_expired():
    if NormalItem is None:
        pytest.skip('NormalItem class not available in src.types')
    normal = NormalItem("+5 Dexterity Vest", 0, 20)
    _call(normal, 'updateQuality', 'update_quality')
    sell_in = _read(normal, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(normal, 'getQuality', 'get_quality', 'quality')
    assert -1 == sell_in
    assert 18 == quality


def test_quality_min_zero():
    if NormalItem is None:
        pytest.skip('NormalItem class not available in src.types')
    normal = NormalItem("+5 Dexterity Vest", 10, 0)
    _call(normal, 'updateQuality', 'update_quality')
    sell_in = _read(normal, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(normal, 'getQuality', 'get_quality', 'quality')
    assert 9 == sell_in
    assert 0 == quality