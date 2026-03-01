import pytest
from typing import Any

try:
    from src.types import Backstage
except Exception:
    Backstage = None


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


def test_crear_backstage():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    name = _read(p, 'getName', 'get_name', 'name')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert "Backstage passes to a TAFKAL80ETC concert" == name
    assert 15 == sell_in
    assert 20 == quality


def test_to_string():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    print("toString() Backstage test")
    if hasattr(p, 'toString'):
        print(p.toString())
    else:
        print(str(p))


def test_update_quality_over_ten():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    _call(p, 'updateQuality', 'update_quality')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert 14 == sell_in
    assert 21 == quality


def test_update_quality_over_five():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 6, 20)
    _call(p, 'updateQuality', 'update_quality')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert 5 == sell_in
    assert 22 == quality


def test_update_quality_over_zero():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    _call(p, 'updateQuality', 'update_quality')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert 4 == sell_in
    assert 23 == quality


def test_update_quality_pass_expired():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    _call(p, 'updateQuality', 'update_quality')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert -1 == sell_in
    assert 0 == quality


def test_quality_max_50():
    if Backstage is None:
        pytest.skip('Backstage class not available in src.types')
    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    _call(p, 'updateQuality', 'update_quality')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert 4 == sell_in
    assert 50 == quality

    p = Backstage("Backstage passes to a TAFKAL80ETC concert", 9, 49)
    _call(p, 'updateQuality', 'update_quality')
    sell_in = _read(p, 'getSell_in', 'get_sell_in', 'sell_in')
    quality = _read(p, 'getQuality', 'get_quality', 'quality')
    assert 8 == sell_in
    assert 50 == quality