import pytest

from unibool.numbs import Is, To


@pytest.mark.order(1)
@pytest.mark.timeout(1)
@pytest.mark.dependency()
def test_is():
    assert Is.real(1)
    assert Is.finite(1)
    assert Is.infinity(float("inf"))
    assert Is.rational(1)
    assert Is.integer(1)


@pytest.mark.order(1)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_is"])
def test_to():
    assert To.real(1) == 1
    assert To.real("1") == 1
    assert To.real("inf") == float("inf")
    assert To.finite(1) == 1
    assert To.integer(1) == 1
    assert To.integer("1") == 1
    assert To.rational(4, 2) == 2
    assert To.rational(3, 4) == 0.75
    assert To.rational(3, 4.0) == 0.75
    with pytest.raises(ValueError):
        To.finite("inf")


@pytest.mark.order(1)
@pytest.mark.timeout(1)
@pytest.mark.dependency(
    depends=[
        "test_constants",
        "test_numbers",
        "test_trigonometric",
    ]
)
def test_all():
    pass
