import pytest
from src.autosimulacrum.utils.file_handling import (
    get_data_folders,
    get_file_names_in_folder,
)


def test_get_data_folders_success(monkeypatch) -> None:
    def mock_listdir(path):
        return ["folder1", "folder2"]

    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.path.exists", lambda path: True
    )
    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.listdir", mock_listdir
    )
    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.path.isdir", lambda path: True
    )

    result = get_data_folders("/existing/path")
    assert result == ["folder1", "folder2"]


def test_get_data_folders_success_no_folders(monkeypatch) -> None:
    def mock_listdir(path):
        return []

    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.path.exists", lambda path: True
    )
    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.listdir", mock_listdir
    )

    result = get_data_folders("/existing/path")
    assert result == []


def test_get_data_folders_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_data_folders("TEST_109238109238")


def test_get_file_names_in_folder_success(monkeypatch) -> None:
    def mock_listdir(path):
        return ["file1.txt", "file2.txt"]

    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.path.exists", lambda path: True
    )
    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.listdir", mock_listdir
    )
    monkeypatch.setattr(
        "src.autosimulacrum.utils.file_handling.os.path.isfile", lambda path: True
    )

    result = get_file_names_in_folder("/existing/path")
    assert result == ["file1.txt", "file2.txt"]


def test_get_file_names_in_folder_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_file_names_in_folder("TEST_109238109238")
