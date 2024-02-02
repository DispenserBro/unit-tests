"""
Main module
"""

from random import random, randint

from .average_value import AverageValue


def main():
    """Main function"""
    list_1 = [randint(1, 10) for _ in range(10)]
    list_2 = [round(random() * 10, 2) for _ in range(20)]

    avg = AverageValue(list_1, list_2)

    avg.print_comparison_result()


if __name__ == "__main__":
    main()
