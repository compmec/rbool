import pytest

from rbool import Empty, Interval, SingleValue, Whole


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency()
def test_begin():
    pass


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_empty():
    empty1 = Empty()
    empty2 = Empty()
    assert id(empty1) == id(empty2)
    assert empty1 is empty2

    hash(empty1)


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_whole():
    whole1 = Whole()
    whole2 = Whole()
    assert id(whole1) == id(whole2)
    assert whole1 is whole2

    hash(whole1)


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_single():
    SingleValue(-10)
    SingleValue(0)
    SingleValue(10)

    SingleValue(-10.0)
    SingleValue(0.0)
    SingleValue(10.0)

    with pytest.raises(ValueError):
        SingleValue(float("-inf"))
    with pytest.raises(ValueError):
        SingleValue(float("inf"))

    hash(SingleValue(10))


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_interval():
    Interval(-10, 10)
    Interval(float("-inf"), 10)
    Interval(-10, float("inf"))
    with pytest.raises(ValueError):
        Interval(float("-inf"), float("inf"))

    hash(Interval(-10, 10))


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_disjoint():
    pass


@pytest.mark.order(12)
@pytest.mark.timeout(1)
@pytest.mark.dependency(
    depends=[
        "test_begin",
        "test_empty",
        "test_whole",
        "test_single",
        "test_interval",
        "test_disjoint",
    ]
)
def test_all():
    pass
