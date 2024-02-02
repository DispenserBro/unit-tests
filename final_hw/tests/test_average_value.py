import pytest

from ..average_value import AverageValue
# from average_value import AverageValue


@pytest.fixture(name='results')
def results() -> list[str]:
    return [
        "Первый список имеет большее среднее значение",
        "Второй список имеет большее среднее значение",
        "Средние значения равны"
    ]


@pytest.fixture(name='list_1')
def list_1() -> list[int]:
    '''
    First list for tests. Equals to the list=[1, 2, 3, 4]
    Average value = 2.5
    '''
    return [1, 2, 3, 4]


@pytest.fixture(name='list_2')
def list_2() -> list[int]:
    '''
    Second list for tests. Equals to the list=[2, 3, 4, 5]
    Average value = 3.5
    '''
    return [2, 3, 4, 5]


@pytest.fixture(name='list_3')
def list_3() -> list[float]:
    '''
    Third list for tests. Equals to the list=[1.1, 2.1, 3.1, 4.1, 5.1]
    Average value = 3.1
    '''
    return [1.1, 2.1, 3.1, 4.1, 5.1]


@pytest.fixture(name='list_4')
def list_4() -> list[float]:
    '''
    Third list for tests. Equals to the list=[2.2, 3.2, 4.2, 5.2, 6.2]
    Average value = 4.2
    '''
    return [2.2, 3.2, 4.2, 5.2, 6.2]


def test_create(list_1, list_2):
    avg = AverageValue(list_1, list_2)
    assert avg.list_1 == list_1
    assert avg.list_2 == list_2


def test_get_average_value(list_1, list_2):
    avg = AverageValue(list_1, list_2)
    assert avg.get_average_value(list_1) == 2.5
    assert avg.get_average_value(list_2) == 3.5


def test_get_average_value_float(list_3, list_4):
    avg = AverageValue(list_3, list_4)
    assert avg.get_average_value(list_3) == 3.1
    assert avg.get_average_value(list_4) == 4.2


def test_compare_average_value(list_1, list_2):
    avg = AverageValue(list_1, list_2)
    assert avg.compare_average_values() == -1


def test_compare_average_value_float(list_3, list_4):
    avg = AverageValue(list_3, list_4)
    assert avg.compare_average_values() == -1


def test_compare_average_values_mixed(list_1, list_4):
    avg = AverageValue(list_1, list_4)
    assert avg.compare_average_values() == -1


def test_compare_average_values_reversed(list_1, list_2):
    avg = AverageValue(list_2, list_1)
    assert avg.compare_average_values() == 1


def test_compare_average_values_same(list_1):
    avg = AverageValue(list_1, list_1)
    assert avg.compare_average_values() == 0


def test_print_comparison_result_first_more(list_1, list_2, results, capfd):
    avg = AverageValue(list_2, list_1)
    avg.print_comparison_result()
    captured = capfd.readouterr()
    assert captured.out.strip() == results[0]


def test_print_comparison_result_second_more(list_1, list_2, results, capfd):
    avg = AverageValue(list_1, list_2)
    avg.print_comparison_result()
    captured = capfd.readouterr()
    assert captured.out.strip() == results[1]


def test_print_comparison_result_equal(list_1, results, capfd):
    avg = AverageValue(list_1, list_1)
    avg.print_comparison_result()
    captured = capfd.readouterr()
    assert captured.out.strip() == results[2]
