# Draft idea for code review, debugging, refactoring, etc.

import os
import sys
import re
import datetime
from pathlib import Path
import pytesseract
from PIL import Image
import subprocess
import json

# Пути
SCREENSHOTS_DIR = r"d:\screenshots"
PROJECT_DIR = r"d:\project"
TASKS_MD = os.path.join(PROJECT_DIR, "tasks.md")
TASK_SCRIPTS_DIR = os.path.join(PROJECT_DIR, "task-scripts")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")

# Убедимся, что папки существуют
os.makedirs(TASK_SCRIPTS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Список файлов в папке screenshots
files = os.listdir(SCREENSHOTS_DIR)
files.sort(key=lambda x: re.search(r'IMG_(\d{8}_\d{6})\.jpg', x))

# Если файлов нет — выйти
if not files:
    print("Нет скриншотов в папке d:\\screenshots")
    sys.exit(1)

# Пример: IMG_20261101_194302.jpg → дата 2026-11-01, время 19:43:02
# Извлекаем дату и время из имени
def parse_filename(filename):
    match = re.search(r'IMG_(\d{8}_\d{6})\.jpg', filename)
    if match:
        date_part = match.group(1)
        date_str = date_part[:8]  # 20261101 → 2026-11-01
        time_str = date_part[8:14]  # 194302 → 19:43:02
        return f"{date_str} {time_str}"
    return None

# Проверка: есть ли файлы с именем IMG_YYYYMMDD_HHMMSS.jpg
valid_files = []
for f in files:
    if f.startswith("IMG_") and f.endswith(".jpg"):
        valid_files.append(f)

if not valid_files:
    print("Нет файлов в формате IMG_YYYYMMDD_HHMMSS.jpg")
    sys.exit(1)

# Извлечение текста из скриншота
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        # Убедимся, что изображение в цвете
        if img.mode in ("P", "LA", "L"):
            img = img.convert("RGB")
        # OCR
        text = pytesseract.image_to_string(img, lang="rus+eng", config="--psm 6")
        return text.strip()
    except Exception as e:
        print(f"Ошибка при извлечении текста из {image_path}: {e}")
        return ""

# Список задач
tasks = []
for filename in valid_files:
    filepath = os.path.join(SCREENSHOTS_DIR, filename)
    date_time = parse_filename(filename)
    text = extract_text_from_image(filepath)
    if not text:
        print(f"Не удалось извлечь текст из {filename}")
        continue

    # Название задачи
    task_id = f"task{len(tasks):02d}-v0"
    task_name = f"{task_id} - {date_time}"
    
    # Сохраняем в tasks.md
    with open(TASKS_MD, "a", encoding="utf-8") as f:
        f.write(f"\n## {task_name}\n")
        f.write(f"{text}\n\n")
    
    # Генерация Python-скрипта через LLM
    # Для примера — используем фиксированный шаблон
    # В реальности — нужно подключить LLM
    
    # Пример: генерация скрипта на Python (в реальности — через LLM)
    script_template = """
# Скрипт для анализа данных
import pandas as pd
import numpy as np

# Пример: анализ текста
text = """ + text + """  # Входной текст

# Пример анализа
print("Анализ текста завершён.")
print(f"Длина текста: {len(text)} символов.")
"""

    # Сохраняем скрипт
    script_path = os.path.join(TASK_SCRIPTS_DIR, f"{task_id}.py")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_template)
    
    # Запуск скрипта
    try:
        result = subprocess.run(
            [sys.executable, "-c", script_template],
            capture_output=True,
            text=True,
            timeout=30
        )
        output_log = f"Log {datetime.datetime.now().strftime('%Y %m %d %H%M')}.txt"
        with open(os.path.join(OUTPUT_DIR, output_log), "w", encoding="utf-8") as f:
            f.write(f"Выход из скрипта:\n{result.stdout}\n{result.stderr}")
        print(f"Запуск скрипта {task_id}.py завершён.")
    except Exception as e:
        print(f"Ошибка при запуске скрипта {task_id}: {e}")

print("Автоматизация завершена.")
