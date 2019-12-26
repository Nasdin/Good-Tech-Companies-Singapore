import pytest
from generate import make_table_headers, _create_markdown_bullet_list


@pytest.mark.parametrize("given,expected", [
    (['AAAA', 'BBB', 'CCC', 'DDDD'],
     "| AAAA | BBB | CCC | DDDD |\n|------|-----|-----|------|")
])
def test_make_table_headers(given, expected):
    actual = make_table_headers(given)
    assert actual == expected


@pytest.mark.parametrize("given,expected", [
    (['AAAA', 'BBB', 'CCC', ],
     "<ul> <li> AAAA </li> <li> BBB </li> <li> CCC </li> </ul>")
])
def test_create_markdown_bullet_list(given, expected):
    actual = _create_markdown_bullet_list(given)
    assert actual == expected
