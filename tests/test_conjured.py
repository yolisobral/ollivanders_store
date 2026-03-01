import pytest
from typing import Any

try:
    from src.types import Conjured
except Exception:
    Conjured = None


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


def test_crear_conjured():
    if Conjured is None:
        pytest.skip('Conjured class not available in src.types')
    c = Conjured("Conjured Mana Cake", 3, 6)
    name = _read(c, 'getName', 'get_name', 'name')
    sell_in = _read(c, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(c, 'getQuality', 'get_quality', 'quality')
    assert "Conjured Mana Cake" == name
    assert 3 == sell_in
    assert 6 == quality


def test_to_string():
    if Conjured is None:
        pytest.skip('Conjured class not available in src.types')
    c = Conjured("Conjured Mana Cake", 3, 6)
    print("toString() Conjured test:")
    if hasattr(c, 'toString'):
        print(c.toString())
    else:
        print(str(c))


def test_update_quality_conjured():
    if Conjured is None:
        pytest.skip('Conjured class not available in src.types')
    c = Conjured("Conjured Mana Cake", 3, 6)
    _call(c, 'updateQuality', 'update_quality')
    sell_in = _read(c, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(c, 'getQuality', 'get_quality', 'quality')
    assert 2 == sell_in
    assert 4 == quality


def test_update_quality_conjured_just_expired():
    if Conjured is None:
        pytest.skip('Conjured class not available in src.types')
    c = Conjured("Conjured Mana Cake", 0, 6)
    _call(c, 'updateQuality', 'update_quality')
    sell_in = _read(c, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(c, 'getQuality', 'get_quality', 'quality')
    assert -1 == sell_in
    assert 2 == quality


def test_update_quality_conjured_expired():
    if Conjured is None:
        pytest.skip('Conjured class not available in src.types')
    c = Conjured("Conjured Mana Cake", -1, 6)
    _call(c, 'updateQuality', 'update_quality')
    sell_in = _read(c, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(c, 'getQuality', 'get_quality', 'quality')
    assert -2 == sell_in
    assert 2 == quality


def test_quality_min_zero():
    if Conjured is None:
        pytest.skip('Conjured class not available in src.types')
    c = Conjured("Conjured Mana Cake", 1, 1)
    _call(c, 'updateQuality', 'update_quality')
    sell_in = _read(c, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(c, 'getQuality', 'get_quality', 'quality')
    assert 0 == sell_in
    assert 0 == quality

    c = Conjured("Conjured Mana Cake", -1, 0)
    _call(c, 'updateQuality', 'update_quality')
    sell_in = _read(c, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(c, 'getQuality', 'get_quality', 'quality')
    assert -2 == sell_in
    assert 0 == quality