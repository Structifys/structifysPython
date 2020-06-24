from insertion_sort import insertion_sort
import pytest

@pytest.mark.parametrize("array,expected",[([3,2,1],[1,2,3]), ([2,4,3],[2,3,4])])
def test_insertion_sort(array,expected):
    result = insertion_sort(array) 
    assert result == expected

