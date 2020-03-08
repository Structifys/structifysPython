import pytest
from binary_search import binary_search

@pytest.mark.parametrize("array,target,expected",[([2,3,4,5],4,2), ([2,3,4], 2,0)])
def test_binary_search(array,target,expected):
    result = binary_search(target,array) 
    print(target,array,result)
    assert result == expected
