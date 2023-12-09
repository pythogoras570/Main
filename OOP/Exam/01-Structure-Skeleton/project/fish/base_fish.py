from abc import ABC, abstractmethod


class BaseFish(ABC):

    def __init__(self, name: str, points: float, time_to_catch: int):
        # Validate name
        if not name or name.isspace():
            raise ValueError("Fish name should be determined!")

        # Validate points
        if not 1 <= points <= 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")

        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @abstractmethod
    def fish_details(self):
        pass
