.. _get_started:

===========
Get started
===========

This library allows you to make boolean operations between subsets on the real line:

* `Empty`: An empty subset, without any elements
* `Whole`: The entire real line
* `SingleValue`: An subset with only one element
* `Interval`: An subset of continuous elements between 
* `Disjoint`: The union of `SingleValue` and `Interval`


Create an interval
------------------

The standard is a closed interval

```python
>>> from rbool import *
>>> interval = Interval(-10, 5)
>>> interval
[-10, 5]
```

You can convert from a list (closed interval) or a tuple:

```python
>>> from rbool import from_any
>>> interval1 = from_any([-5, 2])  # closed interval 
>>> interval1
[-5, 2]
>>> interval2 = from_any((-3, 8))  # open interval
(-3, 8)
```


Operate with intervals
----------------------

You can operate with the symbols:
* `|`: union
* `&`: intersection
* `^`: XOR
* `~`: complementar
* `-`: subtract

Examples:

```python
>>> from rbool import from_any
>>> interval1 = from_any([-5, 2])  # closed interval
>>> interval2 = from_any((-3, 8))  # open interval
>>> interval1 & interval2  # intersect
(-3, 2]
>>> interval1 | interval2  # unite
[-5, 8)
>>> interval1 ^ interval2  # XOR
[-5, -3] U (2, 8)
>>> interval1 - interval2  # subtract
[-5, -3]
>>> ~interval1  # complementar
(-inf, -5) U (2, inf)
>>> interval1 | (~interval1)  # unite with its complementar
(-inf, inf)
```

Use single values
-----------------

You can also create single scalar values:
```python
>>> from rbool import SingleValue
>>> single = SingleValue(5)  # Only one value
>>> single
{5}
>>> single |= {-3, 9, 12}  # Unite with other 3 values
>>> single
{-3, 5, 9, 12}
>>> single | [6, 10]  # Unite with an interval
{-3, 5} U [6, 10] U {12}
```

