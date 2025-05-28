from car_abc import Car


class PassengerCar(Car):
    """
    Represents a passenger car in the rental system.

    This class extends the Car abstract base class and provides specific
    functionality for passenger cars, including rental cost calculation.

    Attributes:
        license_plate (str): Unique identifier for the car
        car_type (str): Type/model of the car
        rental_cost (int): Base daily rental cost in HUF
        electric (bool): Whether the car is electric or combustion engine
    """

    def __init__(
        self, license_plate: str, car_type: str, rental_cost: int, electric: bool
    ):
        """
        Initialize a passenger car with basic attributes and electric status.

        Args:
            license_plate (str): Unique identifier for the car
            car_type (str): Type/model of the car
            rental_cost (int): Base daily rental cost in HUF
            electric (bool): Whether the car is electric (True) or uses fossil fuel (False)
        """
        super().__init__(license_plate, car_type, rental_cost)
        self.electric = electric

    def __str__(self) -> str:
        """
        Returns a string representation of the passenger car.

        Extends the base Car string representation with information about
        whether the car is electric.

        Returns:
            str: A formatted string with car details including electric status
        """
        return f"{super().__str__()} | Electric: {self.electric}"

    def calculate_rental_cost(self, days: int) -> int:
        """
        Calculates the rental cost for a passenger car based on the number of days.

        For passenger cars, the calculation is straightforward:
        Total cost = daily rental cost × number of days

        Args:
            days (int): Number of days for the rental period

        Returns:
            int: Total rental cost in HUF for the specified period

        Raises:
            ValueError: If days is less than 1
        """
        if days < 1:
            raise ValueError("Rental period must be at least 1 day")
        return self.rental_cost * days
