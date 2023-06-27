"""
This module contains the ArangoDB FilterCombiner classes.


FilterCombiner is the class that defines the representation of the filter combiner like AND, OR.
"""


from typing import List, Protocol


class FilterCombiner(Protocol):
    """
    FilterCombiner is the interface that defines the methods that
    a filter combiner should implement.
    """
    name: str

    def combine(self, filters: List[str]) -> str:
        """
        combine is the method that combines the filters using the combiner

        :param filters: List[str]
        :return: str
        """
        pass



class AndCombiner(FilterCombiner):
    """
    AndCombiner is the class that defines the representation of the AND combiner.
    """
    name = "and"

    def combine(self, filters: List[str]) -> str:
        return f'({" && ".join(filters)})'


class OrCombiner(FilterCombiner):
    """
    OrCombiner is the class that defines the representation of the OR combiner.
    """
    name = "or"

    def combine(self, filters: List[str]) -> str:
        return f'({" || ".join(filters)})'
