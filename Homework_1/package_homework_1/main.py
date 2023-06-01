import salary
import people
from datetime import date
import pandas as pd


def main():
    print("Добро пожаловать!")
    salary.calculate_salary()
    people.get_employees()




if __name__ == '__main__':
    main()
    print(f"Дата:{date.today()}")