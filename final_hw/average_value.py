"""
Module that contains the main class of the homework: AverageValue
"""

from typing import Literal


class AverageValue:
    """
    Class for calculating and comparing average values of 2 lists
    """
    def __init__(self, list_1: list[int] | list[float], list_2: list[int] | list[float]):
        """Initializer of the AverageValue class"""
        self.list_1 = list_1
        self.list_2 = list_2

    @staticmethod
    def get_average_value(lst: list[int] | list[float]) -> float:
        """Method to get average value of a list"""
        return sum(lst)/len(lst)

    def compare_average_values(self) -> Literal[1, 0, -1]:
        """Method to compare the average values of two lists"""
        average_1 = self.get_average_value(self.list_1)
        average_2 = self.get_average_value(self.list_2)

        if average_1 > average_2:
            return 1
        if average_1 < average_2:
            return -1
        return 0

    def print_comparison_result(self):
        """Method to print verbose comparison result"""
        comparison_result = self.compare_average_values()

        if comparison_result == 1:
            print("Первый список имеет большее среднее значение")
        elif comparison_result == -1:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
