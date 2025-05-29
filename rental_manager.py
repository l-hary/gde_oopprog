from datetime import datetime, timedelta

from passenger_car import PassengerCar
from truck import Truck


class RentalManager:
    def __init__(self):
        self.rentals = []

    def __str__(self) -> str:
        return "\n".join(str(rental) for rental in self.rentals)

    def add_rental(self, car: PassengerCar | Truck, start_date: datetime) -> None:
        """
        Adds a rental to the rental manager.

        Args:
            car (PassengerCar | Truck): The car to be rented
            start_date (datetime): The start date of the rental

        Raises:
            ValueError: If the start date is in the past
        """
        if car.is_rented:
            raise ValueError("The car is already rented and cannot be booked.")
        rental = Rental(car, start_date)
        self.rentals.append(rental)

    def remove_rental(self, rental: "Rental") -> None:
        """
        Removes a rental from the rental manager.

        Args:
            rental (Rental): The rental to be removed
        """
        if rental in self.rentals:
            rental.terminate()
            self.rentals.remove(rental)
        else:
            raise ValueError("Rental not found in the manager.")


class Rental:
    def __init__(self, car: PassengerCar | Truck, start_date: datetime) -> None:
        self.car = car
        self.start_date = self.validate_date(start_date)
        # car should only be booked for exactly one day per the specification
        self.end_date = self.start_date + timedelta(days=1)
        self.car.is_rented = True

    def __str__(self) -> str:
        return (
            f"Rental of {self.car} from "
            f"{self.start_date.strftime('%Y-%m-%d')} to "
            f"{self.end_date.strftime('%Y-%m-%d')}"
        )

    def validate_date(self, start_date: datetime) -> datetime:
        """
        Validates the rental date to ensure it is in the future and not in the past.

        Args:
            date (datetime): The date to validate

        Returns:
            datetime: The validated date

        Raises:
            ValueError: If the date is in the past
        """

        if start_date < datetime.now():
            raise ValueError("The rental date cannot be in the past.")
        return start_date

    def terminate(self) -> None:
        """
        Terminates the rental, marking the car as not rented.

        This method should be called when the rental period ends or is canceled.
        """
        assert self.car is not None
        self.car.is_rented = False
        self.car = None
