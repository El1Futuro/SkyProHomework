import functools

from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор, который будет логировать вызов функции и ее результат в файл или в консоль."""

    def wrapper(func: Any) -> Any:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok. Result: {result}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                return result

            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs{args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:  # Вывод лога в консоль
                    print(log_message)
                raise
        return inner

    return wrapper
