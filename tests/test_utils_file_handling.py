from pathlib import Path
from re import T
import pytest
from src.autosimulacrum.utils.file_handling import (
    get_data_folders,
    get_file_names_in_folder,
)


def test_get_data_folders_success(tmp_path: Path) -> None:
    temp_dir_a = tmp_path / "temp_folder_a"
    temp_dir_a.mkdir()

    temp_dir_b = tmp_path / "temp_folder_b"
    temp_dir_b.mkdir()

    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text("this is a file.")

    result = get_data_folders(tmp_path)
    assert result == ["temp_folder_a", "temp_folder_b"]


def test_get_data_folders_success_no_folders(tmp_path) -> None:
    result = get_data_folders(tmp_path)
    assert result == []


def test_get_data_folders_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_data_folders("TEST_109238109238")


def test_get_file_names_in_folder_success(tmp_path) -> None:
    temp_file_a = tmp_path / "temp_file_a.txt"
    temp_file_a.write_text("this is a file.")

    temp_dir_b = tmp_path / "temp_file_b.txt"
    temp_dir_b.write_text("this is a file.")

    temp_file = tmp_path / "temp_folder"
    temp_file.mkdir()

    result = get_file_names_in_folder(tmp_path)
    assert result == ["temp_file_a.txt", "temp_file_b.txt"]


def test_get_file_names_in_folder_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_file_names_in_folder("TEST_109238109238")
