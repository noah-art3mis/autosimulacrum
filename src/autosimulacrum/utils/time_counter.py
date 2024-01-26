import time


def count_time(start_time: float, task_name: str) -> None:
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{task_name}: {elapsed_time:.2f} seconds")
