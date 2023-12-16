import os
import time

from config import settings

"""Модуль для получении информации по скачиваемым файлам"""


def get_latest_file(folder_path: str = None) -> str:
    """Получить путь к самому свежему файлу в папке"""
    if folder_path is None:
        folder_path = settings.DOWNLOAD_DIRECTORY
    files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    if not files:
        raise ValueError(f"В папке {folder_path} нет файлов")
    return max(files, key=os.path.getmtime)


def get_size_file(file_path: str) -> float:
    """Получить размер файла"""
    return os.path.getsize(file_path) / (1024 * 1024)


def _is_temporary_file(file_path: str) -> bool:
    """Загружается ли файл"""
    return file_path.endswith(".crdownload")


def is_download_completed(timeout: int = 60):
    """Загружен ли файл"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        file_path = get_latest_file(settings.DOWNLOAD_DIRECTORY)
        if not _is_temporary_file(file_path):
            return True
        time.sleep(1)
    else:
        return False
