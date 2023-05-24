from pypika.functions import *


class ArrayMax(Function):
    def __init__(self, input):
        super().__init__("ARRAY_MAX", input)


class RegexpLike(Function):
    def __init__(self, str_, regex):
        super().__init__("REGEXP_LIKE", str_, regex)


class MaxBy(Function):
    def __init__(self, returned_value, maximized_value):
        super().__init__("MAX_BY", returned_value, maximized_value)


class BoolOr(Function):
    def __init__(self, expression):
        super().__init__("BOOL_OR", expression)


class ApproxPercentile(Function):
    def __init__(self, expr, quantile):
        super().__init__("approx_percentile", expr, quantile)


class Cardinality(Function):
    def __init__(self, expr):
        super().__init__("cardinality", expr)


class ElementAt(Function):
    def __init__(self, expr, idx_or_key):
        super().__init__("element_at", expr, idx_or_key)
