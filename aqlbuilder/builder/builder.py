"""
This module contains the QueryBuilder class for ArangoDB.
QueryBuilder is the class that builds the query for ArangoDB using pydantic models.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseQueryBuilder(ABC):
    """
    BaseQueryBuilder is an abstract class that defines the methods that
    """

    def __init__(self, model: Any):
        self.model = model
        self.query: Dict[str, Any] = {}
        self.sort: List[str] = []
        self.limit: Optional[int] = None
        self.offset: Optional[int] = None
        self.bind_vars: Dict[str, Any] = {}

    @abstractmethod
    def build(self) -> str:
        """
        build is the method that builds the query
        """
        ...
