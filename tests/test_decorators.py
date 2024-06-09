from typing import Any

import pytest

from src.decorators import log


def test_log_file() -> None:
    @log(filename="mylog.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    result = my_function(1, 2)

    with open("mylog.txt") as file:
        for line in file:
            log_message = line

    assert log_message == "my_function ok. Result: 3\n"
    assert result == 3


def test_log_console_raise(capsys: Any) -> None:
    @log()
    def my_function_error(x: Any, y: Any) -> Any:
        raise ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        my_function_error(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function_error error: ZeroDivisionError. Inputs(2, 0), {}\n\n"


def test_log_file_raise() -> None:
    @log(filename="mylog.txt")
    def my_function_error(x: Any, y: Any) -> Any:
        raise ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        my_function_error(2, 0)

    with open("mylog.txt") as file:
        for line in file:
            log_message = line

    assert log_message == "my_function_error error: ZeroDivisionError. Inputs(2, 0), {}\n"
