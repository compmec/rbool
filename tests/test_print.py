import pytest

from rbool import Disjoint, Empty, Interval, SingleValue, Whole, bigger, lower


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
    assert str(empty) == r"{}"
    assert repr(empty) == r"Empty"


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_whole():
    whole = Whole()
    assert str(whole) == r"(-inf, inf)"
    assert repr(whole) == r"Whole"


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_single():
    value = SingleValue(-10)
    assert str(value) == r"{-10}"
    assert repr(value) == r"SingleValue(-10)"

    value = SingleValue(0)
    assert str(value) == r"{0}"
    assert repr(value) == r"SingleValue(0)"

    value = SingleValue(10)
    assert str(value) == r"{10}"
    assert repr(value) == r"SingleValue(10)"


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_interval():
    interval = Interval(-10, 10, True, True)
    assert str(interval) == r"[-10, 10]"

    interval = Interval(-10, 10, True, False)
    assert str(interval) == r"[-10, 10)"

    interval = Interval(-10, 10, False, True)
    assert str(interval) == r"(-10, 10]"

    interval = Interval(-10, 10, False, False)
    assert str(interval) == r"(-10, 10)"

    interval = lower(10, True)
    assert str(interval) == r"(-inf, 10]"

    interval = lower(10, False)
    assert str(interval) == r"(-inf, 10)"

    interval = bigger(-10, True)
    assert str(interval) == r"[-10, inf)"

    interval = bigger(-10, False)
    assert str(interval) == r"(-10, inf)"


@pytest.mark.order(14)
@pytest.mark.timeout(1)
@pytest.mark.dependency(depends=["test_begin"])
def test_disjoint():
    interv0 = lower(-50)
    interv1 = bigger(50)
    disjoint = Disjoint([interv0, interv1])
    assert str(disjoint) == "(-inf, -50] U [50, inf)"
    repr(disjoint)

    interv2 = Interval(-20, 20)
    singles = list(map(SingleValue, [-30, -25, 25, 30, 40]))
    disjoint = Disjoint([interv0, interv1, interv2] + singles)
    blocks = [
        "(-inf, -50]",
        "{-30, -25}",
        "[-20, 20]",
        "{25, 30, 40}",
        "[50, inf)",
    ]
    assert str(disjoint) == " U ".join(blocks)
    repr(disjoint)

    disjoint = Disjoint([interv0, interv2] + singles)
    blocks = ["(-inf, -50]", "{-30, -25}", "[-20, 20]", "{25, 30, 40}"]
    assert str(disjoint) == " U ".join(blocks)
    repr(disjoint)

    disjoint = Disjoint(singles)
    assert str(disjoint) == "{-30, -25, 25, 30, 40}"
    repr(disjoint)


@pytest.mark.order(14)
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
