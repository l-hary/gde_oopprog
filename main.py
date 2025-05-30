from datetime import datetime, timedelta

from passenger_car import PassengerCar
from rental_company import RentalCompany
from truck import Truck


def seed_data(company: RentalCompany):
    car1 = PassengerCar("ABC-123", "Toyota Corolla", 12000, electric=False)
    car2 = PassengerCar("DEF-456", "Nissan Leaf", 15000, electric=True)
    truck1 = Truck("GHI-789", "Ford Transit", 20000, 1000)
    company + car1
    company + car2
    company + truck1

    future_date_1 = datetime.now() + timedelta(days=1)
    future_date_2 = datetime.now() + timedelta(days=2)
    company.rent_car(car1, future_date_1)
    company.rent_car(car2, future_date_1)
    company.rent_car(truck1, future_date_1)
    company.rent_car(car2, future_date_2)


def display_menu():
    # TODO use str repr of the company
    print("\n--- Awesome Car Rental Company ---")
    print("1. Rent a car")
    print("2. Cancel a rental")
    print("3. List active rentals")
    print("4. Exit")


def choose_car(cars):
    print("Available cars:")
    for idx, car in enumerate(cars, start=1):
        print(f"{idx}. {car}")
    try:
        index = (
            int(input("Please provide the id of the car you would like to rent: ")) - 1
        )
        return cars[index]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return None


def main():
    company = RentalCompany("Awesome Car Rental Company")
    seed_data(company)

    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            car = choose_car(company.cars)
            if car:
                try:
                    date_input = input(
                        "When would you like to rent the car (mm/dd/YYYY): "
                    )
                    date = datetime.strptime(date_input, "%m/%d/%Y")
                    company.rent_car(car, date)
                    print(f"{car} booked successfully.")
                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "2":
            if not company.rental_manager.rentals:
                print("No active rentals.")
                continue
            print("Active rentals:")
            for idx, rental in enumerate(company.rental_manager.rentals, start=1):
                print(f"{idx}. {rental}")
            try:
                index = int(input("Select the rental you would like to cancel: ")) - 1
                rental = company.rental_manager.rentals[index]
                company.cancel_rental(rental)
                print("Successful cancellation.")
            except (ValueError, IndexError):
                print("Invalid choice. Please use a valid number.")

        elif choice == "3":
            rentals = company.list_rentals()
            if not rentals:
                print("No active rentals.")
            else:
                print("Active rentals:")
                for rental in rentals:
                    print(rental)

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
