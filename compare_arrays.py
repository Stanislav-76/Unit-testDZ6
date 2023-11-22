"""Module providing a function compare arrays"""
import dataclasses


@dataclasses.dataclass
class CompareArrays:
    """Class compare two arrays"""

    @staticmethod
    def compare_arrays(numbers1, numbers2):
        """method compare arrays"""
        if not isinstance(numbers1, list) or not isinstance(numbers2, list):
            raise TypeError("Input should be a list.")
        mean_numbers1 = mean_numbers2 = 0
        if numbers1:
            mean_numbers1 = sum(numbers1) / len(numbers1)
        if numbers2:
            mean_numbers2 = sum(numbers2) / len(numbers2)
        if mean_numbers1 > mean_numbers2:
            print("Первый список имеет большее среднее значение")
        if mean_numbers1 < mean_numbers2:
            print("Второй список имеет большее среднее значение")
        if mean_numbers1 == mean_numbers2:
            print("Средние значения равны")