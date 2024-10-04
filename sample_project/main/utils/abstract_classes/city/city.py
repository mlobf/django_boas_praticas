"""Base City Ruler."""

from typing import List
from abc import ABC, abstractmethod
from sample_project.main.utils.dataclasses.city.city import City


class BaseCity(ABC):
    """Base class to define specific rules for cites in this sample context."""

    @property
    @abstractmethod
    def get_cities(self) -> List[City]:
        """Get all cities"""
        raise NotImplementedError()

    def is_valid_city(self, entry: City) -> bool:
        """Check if a new City should be ignored for specific Process."""
        return not any(name in entry['name'] for name in self.get_cities)

    @abstractmethod
    def refresh(self):
        # Apply specific city constraints over a main process, changing them if applicable."""
        raise NotImplementedError()
