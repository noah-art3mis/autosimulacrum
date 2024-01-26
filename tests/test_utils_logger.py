from src.autosimulacrum.utils.logger import make_logger


def test_make_logger() -> None:
    logger = make_logger(__file__)
    assert logger.name == "test_utils_logger"
