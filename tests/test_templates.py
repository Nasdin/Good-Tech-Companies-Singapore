import pytest
from generate import (make_table_headers, _create_markdown_bullet_list, _get_data, _get_metadata, create_metadata)


@pytest.fixture
def metadata_fields():
    return 'career_page', 'strike_out', 'glassdoor__link', 'software_engineer__link'


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


@pytest.mark.parametrize("given_key,given_nested_data,expected", [
    ('AA', {'A': 1, 'AA': 2}, 2,),
    ('AA__BB', {'A': 1, 'AA': {'B': 3, 'BB': 4, 'BBB': 5}}, 4,),
    ('AA__BB__CC', {'A': 1, 'AA': {'B': 3, 'BB': {'C': 6, 'CC': 7, 'CCC': 8}, 'BBB': 5}}, 7,)
])
def test__get_data(given_key, given_nested_data, expected):
    actual = _get_data(given_key, given_nested_data)
    assert actual == expected


@pytest.mark.parametrize("given,expected", [
    ({'career_page': 'bla'},
     {'career_page': 'bla', 'strike_out': None, 'glassdoor__link': None, 'software_engineer__link': None}),

    ({'career_page': 'bla', 'extra_info': 123, 'extra_info2': 'ignore'},
     {'career_page': 'bla', 'strike_out': None, 'glassdoor__link': None, 'software_engineer__link': None}),

    ({'career_page': 'bla', 'extra_info2': 'ignore', 'strike_out': 2},
     {'career_page': 'bla', 'strike_out': 2, 'glassdoor__link': None, 'software_engineer__link': None}),

    ({'career_page': 'bla', 'extra_info': 123, 'strike_out': 1, 'glassdoor': {'link': 'abc'},
      'software_engineer': {'link': 'bcd', 'extra': 'ignore'}},
     {'career_page': 'bla', 'strike_out': 1, 'glassdoor__link': 'abc', 'software_engineer__link': 'bcd'}),

])
def test__get_metadata(given, expected, metadata_fields):
    actual = _get_metadata(given, metadata_fields)
    assert actual == create_metadata(**expected)
