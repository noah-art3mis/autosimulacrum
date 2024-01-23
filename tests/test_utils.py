import utils
import pytest
from utils import make_logger, count_time, get_data_folders, get_file_names_in_folder
import time
from pytest import MonkeyPatch
import os


def test_make_logger() -> None:
    logger = make_logger(__file__)
    assert logger.name == "test_utils"


def test_count_time(capsys):
    start_time = time.perf_counter()
    count_time(start_time, "Task Name")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Task Name: {:.2f} seconds".format(
        time.perf_counter() - start_time
    )


def test_get_data_folders_success(monkeypatch) -> None:
    def mock_listdir(path):
        return ["folder1", "folder2"]

    monkeypatch.setattr("utils.os.path.exists", lambda path: True)
    monkeypatch.setattr("utils.os.listdir", mock_listdir)

    result = get_data_folders("/existing/path")
    assert result == ["folder1", "folder2"]


def test_get_data_folders_fail() -> None:
    with pytest.raises(FileNotFoundError):
        utils.get_data_folders("TEST_109238109238")


def test_get_file_names_in_folder_success(monkeypatch) -> None:
    def mock_listdir(path):
        return ["file1.txt", "file2.txt"]

    monkeypatch.setattr("utils.os.path.exists", lambda path: True)
    monkeypatch.setattr("utils.os.listdir", mock_listdir)

    result = get_file_names_in_folder("/existing/path")
    assert result == ["file1.txt", "file2.txt"]


def test_get_file_names_in_folder_fail() -> None:
    with pytest.raises(FileNotFoundError):
        utils.get_file_names_in_folder("TEST_109238109238")
