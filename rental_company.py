from car_abc import Car
from rental_manager import RentalManager


class RentalCompany:
    """
    Represents a rental company that manages a fleet of cars.

    This class provides functionality to add cars to the fleet, calculate
    rental costs, and retrieve information about the available cars.

    Attributes:
        fleet (list): List of Car objects representing the rental company's fleet
    """

    def __init__(self, name: str):
        """
        Initialize an empty fleet for the rental company.
        """
        self.name = name
        self._cars = []
        self.rental_manager = RentalManager()

    def __add__(self, car: Car):
        """
        Add a car to the rental company's fleet.

        Args:
            car (Car): The car to be added to the fleet

        Returns:
            RentalCompany: The rental company instance with the new car added
        """
        if not isinstance(car, Car):
            raise TypeError("Only instances of Car can be added to the fleet.")
        self._cars.append(car)
        return self

    def __str__(self) -> str:
        return self.name

    @property
    def cars(self) -> list[Car]:
        """
        Returns the list of cars in the rental company's fleet.

        Returns:
            list: List of Car objects
        """
        return self._cars
