from datetime import datetime

from passenger_car import PassengerCar
from truck import Truck


class RentalManager:
    def __init__(self) -> None:
        self.rentals: list["Rental"] = []

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
        for rental in self.rentals:
            if rental.car == car and rental.date == start_date.date():
                raise ValueError("The car is already booked for that date.")
        rental = Rental(car, start_date)
        self.rentals.append(rental)

    def remove_rental(self, rental: "Rental") -> None:
        """
        Removes a rental from the rental manager.

        Args:
            rental (Rental): The rental to be removed
        """
        if rental in self.rentals:
            self.rentals.remove(rental)
        else:
            raise ValueError("Rental not found.")


class Rental:
    def __init__(self, car: PassengerCar | Truck, start_date: datetime) -> None:
        self.car = car
        # the car should only be booked for a (calendar) day, so end date is not tracked
        self.date = self.validate_date(start_date).date()

    def __str__(self) -> str:
        return f"Rental of {self.car} on {self.date.strftime('%m/%d/%Y')}"

    def validate_date(self, start_date: datetime) -> datetime:
        """
        Validates the rental date to ensure it is in the future and not in the past.

        Args:
            start_date (datetime): The date to validate

        Returns:
            datetime: The validated date

        Raises:
            ValueError: If the date is in the past
        """
        today = datetime.now().date()
        if start_date.date() < today:
            raise ValueError("The rental date cannot be in the past.")
        return start_date
