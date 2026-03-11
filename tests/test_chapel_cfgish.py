import pytest
from pathlib import Path
from chapel_printings import load_chapel_config


@pytest.fixture
def _builtin_cfg():
    cp_cfg = load_chapel_config()
    yield cp_cfg

def _test_cfgish():
    heredir = Path(__file__).resolve().parent

    tcfg_path = heredir / 'assets' / 'testing_cfgish.yml'
    tcfg = load_chapel_config(tcfg_path)
    return tcfg

@pytest.fixture
def _test_cfgish_fx():
    tcfg = _test_cfgish()
    yield tcfg

def test_builting_load():
    cp_cfg = load_chapel_config()
    assert cp_cfg is not None

def test_load_from_file():
    tcfg = _test_cfgish()
    assert tcfg is not None

def test_basic_layout_style(_builtin_cfg):
    assert hasattr(_builtin_cfg, "overall_style_version")
    assert "overall_style_version" in _builtin_cfg


def test_basic_layout_printer_geometry(_builtin_cfg):
    assert hasattr(_builtin_cfg, "printer_geometry")
    assert "printer_geometry" in _builtin_cfg


def test_printer_version(_test_cfgish_fx):
    assert _test_cfgish_fx.overall_style_version == 1

    
def test_printer_geometry(_test_cfgish_fx):
    assert 'M200V2' in _test_cfgish_fx.printer_geometry
    m2 = _test_cfgish_fx.printer_geometry['M200V2']
    assert m2.bed_wide__mm == 120
    assert m2.bed_deep__mm == 121
    assert m2.bed_height__mm == 122

# TODO:
# - neg cases for errors in file
