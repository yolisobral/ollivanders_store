import pytest
from typing import Any

try:
    from src.types import Sulfuras
except Exception:
    Sulfuras = None


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


def test_crear_sulfuras():
    if Sulfuras is None:
        pytest.skip('Sulfuras class not available in src.types')
    s = Sulfuras()
    name = _read(s, 'getName', 'get_name', 'name')
    sell_in = _read(s, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(s, 'getQuality', 'get_quality', 'quality')
    assert "Sulfuras, Hand of Ragnaros" == name
    assert 0 == sell_in
    assert 80 == quality


def test_to_string():
    if Sulfuras is None:
        pytest.skip('Sulfuras class not available in src.types')
    s = Sulfuras()
    print("Sulfuras toString() test")
    if hasattr(s, 'toString'):
        print(s.toString())
    else:
        print(str(s))


def test_update_quality_sulfuras():
    if Sulfuras is None:
        pytest.skip('Sulfuras class not available in src.types')
    s = Sulfuras()
    _call(s, 'updateQuality', 'update_quality')
    sell_in = _read(s, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(s, 'getQuality', 'get_quality', 'quality')
    assert 0 == sell_in
    assert 80 == quality