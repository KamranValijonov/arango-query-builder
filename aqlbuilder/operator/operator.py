"""
This module contains the FilterOperators for ArangoDB.

FilterOperator is the class that defines the representation of the filter operator.
"""

from typing import Any, Protocol


class FilterOperator(Protocol):
    """
    FilterOperator is the interface that defines the methods that
    a filter operator should implement.
    """
    name: str

    def compose(self, key: str, value: Any) -> str:
        """
        compose is the method that composes the filtration subquery
        using the key and value

        :param key: str
        :param value: Any
        :return: str
        """
        pass


class EqualOperator(FilterOperator):
    """
    EqualOperator is the class that defines the representation of the equal operator.
    """
    name = "eq"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} == {value}'


class NotEqualOperator(FilterOperator):
    """
    NotEqualOperator is the class that defines the representation of the not equal operator.
    """
    name = "neq"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} != {value}'


class GreaterThanOperator(FilterOperator):
    """
    GreaterThanOperator is the class that defines the representation of the greater than operator.
    """
    name = "gt"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} > {value}'


class GreaterThanOrEqualOperator(FilterOperator):
    """
    GreaterThanOrEqualOperator is the class that defines the representation of the greater than or equal operator.
    """
    name = "gte"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} >= {value}'


class LessThanOperator(FilterOperator):
    """
    LessThanOperator is the class that defines the representation of the less than operator.
    """
    name = "lt"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} < {value}'


class LessThanOrEqualOperator(FilterOperator):
    """
    LessThanOrEqualOperator is the class that defines the representation of the less than or equal operator.
    """
    name = "lte"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} <= {value}'


class InOperator(FilterOperator):
    """
    InOperator is the class that defines the representation of the in operator.
    """
    name = "in"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} in {value}'


class NotInOperator(FilterOperator):
    """
    NotInOperator is the class that defines the representation of the not in operator.
    """
    name = "nin"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} not in {value}'


class LikeOperator(FilterOperator):
    """
    LikeOperator is the class that defines the representation of the like operator.
    """
    name = "like"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} like {value}'


class NotLikeOperator(FilterOperator):
    """
    NotLikeOperator is the class that defines the representation of the not like operator.
    """
    name = "nlike"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} not like {value}'


class HasOperator(FilterOperator):
    """
    HasOperator is the class that defines the representation of the has operator.
    """
    name = "has"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} has {value}'


class NotHasOperator(FilterOperator):
    """
    NotHasOperator is the class that defines the representation of the not has operator.
    """
    name = "nhas"

    def compose(self, key: str, value: Any) -> str:
        return f'{key} not has {value}'
