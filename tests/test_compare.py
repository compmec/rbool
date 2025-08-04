import pytest

from rbool import Empty, Interval, SingleValue, Whole
from rbool.numbs import NEGINF, POSINF


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(
    depends=[
        "tests/test_build.py::test_all",
        "tests/test_convert.py::test_all",
    ],
    scope="session",
)
def test_begin():
    pass


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_empty():
    empty = Empty()

    assert empty == empty
    assert empty == {}
    assert empty == r"{}"


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_whole():
    whole = Whole()

    assert whole == whole
    assert whole == (float("-inf"), float("inf"))
    assert whole == (float("-inf"), POSINF)
    assert whole == (NEGINF, float("inf"))
    assert whole == (NEGINF, POSINF)
    assert whole == [float("-inf"), float("inf")]
    assert whole == [float("-inf"), POSINF]
    assert whole == [NEGINF, float("inf")]
    assert whole == [NEGINF, POSINF]
    assert whole == r"(-inf, inf)"


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_empty", "test_whole"])
def test_singletons():
    empty = Empty()
    whole = Whole()

    assert empty == empty
    assert empty != whole
    assert whole != empty
    assert whole == whole

    assert not empty != empty
    assert not empty == whole
    assert not whole == empty
    assert not whole != whole


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_singletons"])
def test_singles():
    empty = Empty()
    whole = Whole()

    for value in (-10, 0, 10):
        single = SingleValue(value)
        assert single == single
        assert single == value
        assert single == {value}
        assert single == "{" + str(value) + "}"

        assert single != empty
        assert empty != single
        assert single != whole
        assert whole != single

        assert not single == empty
        assert not empty == single
        assert not single == whole
        assert not whole == single


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_singletons", "test_singles"])
def test_intervals():
    empty = Empty()
    whole = Whole()

    aval, bval = -10, 10

    n2a = Interval(NEGINF, aval)
    n2b = Interval(NEGINF, bval)
    a2b = Interval(aval, bval)
    a2p = Interval(aval, POSINF)
    b2p = Interval(bval, POSINF)

    intervals = (n2a, n2b, a2b, a2p, b2p)
    for i, intvi in enumerate(intervals):
        for j, intvj in enumerate(intervals):
            if i == j:
                assert intvi == intvj
            else:
                assert intvi != intvj

    for interv in intervals:
        assert empty != interv
        assert whole != interv
        assert interv != empty
        assert interv != whole

        assert not empty == interv
        assert not whole == interv
        assert not interv == empty
        assert not interv == whole

    closed_pairs = [
        (-50, 50),
        (-50, -20),
        (20, 50),
        (NEGINF, -20),
        (NEGINF, 0),
        (NEGINF, 20),
        (-20, POSINF),
        (0, POSINF),
        (20, POSINF),
    ]
    for sta, end in closed_pairs:
        interv = Interval(sta, end, True, True)
        assert interv == [sta, end]
        assert [sta, end] == interv

    open_pairs = [
        (-50, 50),
        (-50, -20),
        (20, 50),
        (NEGINF, -20),
        (NEGINF, 0),
        (NEGINF, 20),
        (-20, POSINF),
        (0, POSINF),
        (20, POSINF),
    ]
    for sta, end in open_pairs:
        interv = Interval(sta, end, False, False)
        assert interv == (sta, end)
        assert (sta, end) == interv


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(
    depends=[
        "test_begin",
        "test_empty",
        "test_whole",
        "test_singletons",
        "test_singles",
        "test_intervals",
    ]
)
def test_all():
    pass
