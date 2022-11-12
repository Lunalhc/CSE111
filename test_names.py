from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John","Wright")=="Wright;John"
    assert make_full_name("Lily","Smith")=="Smith;Lily"

    
def test_extract_family_name():
    assert extract_family_name("Wright; John")=="Wright"
    assert extract_family_name("Smith; Lily")=="Smith"


def test_extract_given_name():
    assert extract_given_name("Wright; John")=="John"
    assert extract_given_name("Smith; Lily")=="Lily"






pytest.main(["-v", "--tb=line", "-rN", __file__])
