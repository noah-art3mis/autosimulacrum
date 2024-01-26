from src.autosimulacrum.utils.time_counter import count_time
import time


def test_count_time(capsys):
    start_time = time.perf_counter()
    count_time(start_time, "Task Name")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Task Name: {:.2f} seconds".format(
        time.perf_counter() - start_time
    )
