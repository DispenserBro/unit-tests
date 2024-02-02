import pytest

from .test_average_value import results
from ..main import main


def test_printed_value_in_results(results, capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() in results