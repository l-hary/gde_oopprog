from datetime import datetime

from car_abc import Car
from passenger_car import PassengerCar
from rental_manager import Rental, RentalManager
from truck import Truck


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

    # TODO add is not self documenting, implement add_car method for clarity
    def __add__(self, car: PassengerCar | Truck) -> "RentalCompany":
        """
        Add a car to the rental company's fleet.

        Args:
            car (PassengerCar | Truck): The car to be added to the fleet

        Returns:
            RentalCompany: The rental company instance with the new car added
        """
        if not isinstance(car, Car):
            raise TypeError("Only instances of Car can be added to the fleet.")
        self._cars.append(car)
        return self

    # TODO same as __add__, implement remove_car method for clarity
    def __sub__(self, car: PassengerCar | Truck) -> "RentalCompany":
        """
        Remove a car from the rental company's fleet.

        Args:
            car (PassengerCar | Truck): The car to be removed from the fleet

        Returns:
            RentalCompany: The rental company instance with the car removed

        Raises:
            ValueError: If the car is not found in the fleet
        """
        if car not in self._cars:
            raise ValueError("Car not found in the fleet.")
        self._cars.remove(car)
        return self

    def __str__(self) -> str:
        return self.name

    @property
    def cars(self) -> list[PassengerCar | Truck]:
        """
        Returns the list of cars in the rental company's fleet.

        Returns:
            list: List of Car objects
        """
        return self._cars

    def rent_car(self, car: PassengerCar | Truck, start_date: datetime):
        """
        Rent a car from the fleet.

        Args:
            car (PassengerCar | Truck): The car to be rented
            start_date (datetime): The start date of the rental

        Raises:
            ValueError: If the car is already rented or not found in the fleet
        """
        if car not in self._cars:
            raise ValueError("Car not found in the fleet.")
        self.rental_manager.add_rental(car, start_date)

    def cancel_rental(self, rental: Rental):
        """
        Cancel a rental.

        Args:
            rental (Rental): The rental to be canceled

        Raises:
            ValueError: If the rental is not found in the rental manager
        """
        if rental.car not in self._cars:
            raise ValueError("Car not found in the fleet.")
        self.rental_manager.remove_rental(rental)

    def list_rentals(self) -> list[str]:
        """
        List all current rentals.

        Returns:
            list: List of strings representing current rentals
        """
        return [str(rental) for rental in self.rental_manager.rentals]
