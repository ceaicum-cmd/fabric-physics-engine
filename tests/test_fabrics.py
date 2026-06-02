import pytest

from fabric_physics_engine import MaterialType, get_fabric_properties


def test_known_fabric_properties():
    silk = get_fabric_properties("silk")
    assert silk.material_type == MaterialType.SILK
    assert silk.sheen > 0.5


def test_unknown_fabric_raises_key_error():
    with pytest.raises(KeyError):
        get_fabric_properties("unknown")
