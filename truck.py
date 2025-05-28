from car_abc import Car


class Truck(Car):
    """
    Represents a truck in the rental system.

    This class extends the Car abstract base class and provides specific
    functionality for trucks, including rental cost calculation.
    Attributes:
        license_plate (str): Unique identifier for the truck
        car_type (str): Type/model of the truck
        rental_cost (int): Base daily rental cost in HUF
        load_capacity (int): Maximum load capacity of the truck in kg
    """

    def __init__(
        self, license_plate: str, car_type: str, rental_cost: int, load_capacity: int
    ):
        """
        Initialize a truck with basic attributes and load capacity.

        Args:
            license_plate (str): Unique identifier for the truck
            car_type (str): Type/model of the truck
            rental_cost (int): Base daily rental cost in HUF
            load_capacity (int): Maximum load capacity of the truck in kg
        """
        super().__init__(license_plate, car_type, rental_cost)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        """
        Returns a string representation of the truck.

        Extends the base Car string representation with information about
        the truck's load capacity.

        Returns:
            str: A formatted string with truck details including load capacity
        """
        return f"{super().__str__()} | Load Capacity: {self.load_capacity} kg"

    def calculate_rental_cost(self, days: int) -> int:
        """
        Calculates the rental cost for a truck based on the number of days.

        For trucks, the calculation is straightforward:
        Total cost = daily rental cost × number of days

        Args:
            days (int): Number of days for the rental period

        Returns:
            int: Total rental cost in HUF for the specified period

        Raises:
            ValueError: If days is less than 1
        """
        if days < 1:
            raise ValueError("Number of days must be at least 1")
        return self.rental_cost * days
