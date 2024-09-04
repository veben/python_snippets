import pytest
from solution import Solution


@pytest.fixture(scope="session")
def solution() -> Solution:
    return Solution()


def test_value_error(solution):
    colors = [1, 1]
    with pytest.raises(ValueError):
        solution.number_of_alternating_groups(colors)


def test_single_color(solution):
    colors = [1, 1, 1]
    expected = 0
    result = solution.number_of_alternating_groups(colors)
    assert result == expected


def test_alternating_colors(solution):
    colors = [0, 1, 0, 0, 1]
    expected = 3
    result = solution.number_of_alternating_groups(colors)
    assert result == expected
