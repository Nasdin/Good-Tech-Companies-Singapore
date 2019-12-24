import pytest
from generate import make_table_headers


@pytest.mark.parametrize("given,expected", [
    (['AAAA', 'BBB', 'CCC', 'DDDD'],
     "| AAAA | BBB | CCC | DDDD |" + '\n' + "|----|---|---|------------------------------|")
])
def test_make_table_headers(given, expected):
    actual = make_table_headers(given)
    assert actual == expected
