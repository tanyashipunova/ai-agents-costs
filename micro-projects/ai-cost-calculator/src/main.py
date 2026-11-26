import os
from pathlib import Path
import json

from src.generate_financial_report import generate_financial_report
from src.generate_mermaid_diagram import generate_mermaid_diagram

# Путь к файлу конфигурации
CONFIG_DIR = Path("config")
JSON_DATA_PATH = CONFIG_DIR / "example_pipeline.json"
# config_path = "config/example_pipeline.json"

with open(JSON_DATA_PATH, 'r', encoding='utf-8') as f:
    config_data = json.load(f)


def main():
    print("Запущено консольное приложение для генерации плановых отчетов и диаграмм.")
    
    while True:
        print("\n--- Меню ---")
        print("1. Создать плановый отчет и вывести на экран")
        print("2. Сгенерить диаграмму с сохранением файла architecture.mermaid в папку проекта config")
        print("3. Открыть диаграмму в ПО, если уже сгенерили диаграмму на шаге 2")
        print("4. Выйти из консольного приложения")
        
        try:
            choice = int(input("\nВыберите действие (1-4): "))
        except ValueError:
            print("[Error] Введите корректное число.")
            continue
        
        if choice == 1: 
            print("\n" + generate_financial_report(config_data))
            
        elif choice == 2: 
            output_mermaid_path = "config/architecture.mermaid"
            mermaid_code = generate_mermaid_diagram(config_data)
            with open(output_mermaid_path, "w", encoding="utf-8") as file:
                file.write(mermaid_code)
            print(f"[Успех] Схема Mermaid успешно сохранена в файл: {output_mermaid_path}")
            print("[Инфо] Вы можете скопировать её содержимое на сайт или в Draw.io")

            generate_mermaid_diagram(config_data)
            
        elif choice == 3: 
            mermaid_path = CONFIG_DIR / "architecture.mermaid"
            if mermaid_path.exists():
                try:
                    os.startfile(mermaid_path)
                    print("[Успех] Диаграмма успешно открыта в Draw.io.")
                except FileNotFoundError:
                    print("[Warning] Программа для открытия файлов не найдена. Попробуйте открыть вручную.")
            else:
                print("[Error] Диаграмма не найдена. Сначала сгенерируйте её.")
                
        elif choice == 4: 
            print("До свидания!")
            break
            
        else:
            print("[Error] Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
