from src.utils.exception_logging import log_exception
import logging


logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def test_exception_logging(caplog):
    @log_exception
    def function_that_will_error():
        return 1 / 0

    try:
        function_that_will_error()
    except ZeroDivisionError:
        pass

    assert "ZeroDivisionError" in caplog.text
