from abc import ABC, abstractmethod


class Car(ABC):
    """
    Abstract base class for a car in the rental system.

    This class defines the common properties and behaviors of all car types
    in the rental system. It provides core functionality for tracking rental
    status and calculating costs.

    Attributes:
        license_plate (str): Unique identifier for the car
        car_type (str): Type/model of the car
        rental_cost (int): Base daily rental cost in HUF
        _is_rented (bool): Internal flag to track rental status
    """

    def __init__(self, license_plate: str, car_type: str, rental_cost: int):
        """
        Initializes the car with a license plate, type, and rental cost.

        Args:
            license_plate (str): Unique identifier for the car
            car_type (str): Type/model of the car
            rental_cost (int): Base daily rental cost in HUF

        Note:
            All cars are initialized as not rented (is_rented = False).
        """
        self.license_plate = license_plate
        self.car_type = car_type
        self.rental_cost = rental_cost
        self._is_rented = False

    def __str__(self):
        """
        Returns a string representation of the car.

        Returns:
            str: A formatted string with car type, license plate, and daily rental cost
        """
        return f"{self.car_type} ({self.license_plate}) - {self.rental_cost} HUF/day"

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> int:
        """
        Abstract method to calculate the rental cost for a given number of days.

        This method must be implemented by all concrete car subclasses to provide
        specific pricing calculations.

        Args:
            days (int): Number of days for the rental period

        Returns:
            int: Total rental cost in HUF for the specified period

        Raises:
            NotImplementedError: If called directly on the abstract class
        """
        pass

    @property
    def is_rented(self) -> bool:
        """
        Property to check if the car is currently rented.

        Returns:
            bool: True if the car is currently rented, False otherwise
        """
        return self._is_rented

    @is_rented.setter
    def is_rented(self, value: bool):
        """
        Setter to update the rental status of the car.

        Args:
            value (bool): The new rental status (True for rented, False for available)
        """
        self._is_rented = value
