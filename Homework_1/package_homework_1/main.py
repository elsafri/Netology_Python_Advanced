from package_homework_1.application import salary
from package_homework_1.application.db import people
from datetime import date


def main():
    print("Добро пожаловать!")
    salary.calculate_salary()
    people.get_employees()


if __name__ == '__main__':
    main()
    print(f"Дата:{date.today()}")
