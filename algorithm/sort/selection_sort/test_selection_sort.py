import pytest
from  selection_sort import selection_sort

@pytest.mark.parametrize("test_input,expected", [([3,2,4], [2,3,4]), ([333,44,5,6], [5,6,44,333]), ([32,4,2,1], [1,2,4,32])])
def test_selection_sort_success(test_input,expected):
    result = selection_sort(test_input)
    assert result == expected
