"""Test module providing a function compare arrays"""
from io import StringIO
import sys
import pytest
from compare_arrays import CompareArrays

class TestCompareArrays:
    """TestClass compare two arrays"""

    @pytest.mark.parametrize("array1, array2", [
        ([], "test"),
        (1, [10, 20, 30, 40]),
        ("test", [])
    ])
    def test_compare_arrays_zero(self, array1, array2):
        """" Test method compare arrays zero"""
        with pytest.raises(TypeError):
            CompareArrays.compare_arrays(array1, array2)


    @pytest.mark.parametrize("array1, array2, expected", [
        ([10, 20, 30, 40], [2, 4, 6, 8], "Первый список имеет большее среднее значение\n"),
        ([2, 4, 6, 8], [10, 20, 30, 40], "Второй список имеет большее среднее значение\n"),
        ([10, 20, 30, 40], [10, 20, 30, 40], "Средние значения равны\n"),
        ([], [-5], "Первый список имеет большее среднее значение\n"),
        ([-5], [], "Второй список имеет большее среднее значение\n"),
        ([], [], "Средние значения равны\n")
    ])
    def test_compare_arrays(self, array1, array2, expected):
        """" Test method compare arrays"""
        captured_output = StringIO()
        sys.stdout = captured_output
        CompareArrays.compare_arrays(array1, array2)
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue() == expected