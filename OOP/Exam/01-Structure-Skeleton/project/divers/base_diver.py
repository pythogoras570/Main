from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        # Use properties to set values with validation
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Diver name cannot be null or empty!")
        self._name = value

    @property
    def oxygen_level(self):
        return self._oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self._oxygen_level = value

    def miss(self, time_to_catch: int):
        # To be implemented in derived classes
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    @abstractmethod
    def hit(self, fish: BaseFish):
        pass

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{type(self).__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
