import pytest
from inversions import count_inversions


@pytest.mark.parametrize("array,count", [
    ([], 0),
    ([1], 0),
    ([1,1], 0),
    ([1,2], 0),
    ([2,1], 1),
    ([1,2,3], 0),
    ([2,1,3], 1),
    ([3,1,2], 2),
    ([3,2,1], 3),
    ([1,3,2], 1),
    ([1,1,1], 0),
    ([2,1,1], 2),
    ([2,1,2], 1),
    ([2,2,1], 2),
    ([1,2,1], 1),
    ([1,2,3,4], 0),
    ([1,3,2,4], 1),
    ([1,4,2,3], 2),
    ([1,4,3,2], 3),
    ([4,1,3,2], 4),
    ([4,3,1,2], 5),
    ([4,3,2,1], 6)
])
def test_count_inversions(array, count):

    assert count_inversions(array) == count
