from dataclasses import dataclass
from typing import Optional


@dataclass
class City:
    id: Optional[str] = None
    city_name: str
    short_name: str

    def __post_init__(self):
        if not isinstance(self.id, (str, type(None))):
            raise TypeError(
                f"Expected 'id' to be 'Optional[str]', got {
                    type(self.id).__name__}"
            )
        if not isinstance(self.city_name, str):
            raise TypeError(
                f"Expected 'city_name' to be 'str', got {
                    type(self.city_name).__name__}"
            )
        if not isinstance(self.short_name, str):
            raise TypeError(
                f"Expected 'short_name' to be 'str', got {
                    type(self.short_name).__name__}"
            )


@dataclass
class Cassino:
    id: Optional[str] = None
    cassino_name: str
    short_name: str
    address: str
    manager: str

    def __post_init__(self):
        if not isinstance(self.id, (str, type(None))):
            raise TypeError(
                f"Expected 'id' to be 'Optional[str]', got {
                    type(self.id).__name__}"
            )
        if not isinstance(self.cassino_name, str):
            raise TypeError(
                f"Expected 'city_name' to be 'str', got {
                    type(self.cassino_name).__name__}"
            )
        if not isinstance(self.short_name, str):
            raise TypeError(
                f"Expected 'short_name' to be 'str', got {
                    type(self.short_name).__name__}"
            )
        if not isinstance(self.address, str):
            raise TypeError(
                f"Expected 'short_name' to be 'str', got {
                    type(self.address).__name__}"
            )
        if not isinstance(self.manager, str):
            raise TypeError(
                f"Expected 'short_name' to be 'str', got {
                    type(self.manager).__name__}"
            )
