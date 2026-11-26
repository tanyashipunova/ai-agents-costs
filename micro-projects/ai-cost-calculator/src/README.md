# LLM Multi-Agent Planned FinOps & Architecture Visualizer

[English](#english) | [Русский](#русский)

---

## English

A zero-dependency Python utility designed to trace planned token accumulation, calculate planned API costs, and automatically generate Mermaid.js sequence diagrams for multi-agent LLM systems from a single JSON configuration.

### Key Features
* **Dynamic FinOps Auditing.** Tracks sliding context windows where input size grows linearly based on previous steps' outputs.
* **Mermaid.js Generation.** Automatically creates copy-pasteable sequence diagram code compatible with Draw.io and GitHub markdown.
* **Visual Error Highlighting.** Uses condition-based arrows (`-->>`) to explicitly flag failed steps or validation errors in logs.

### Quick Start (template)

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ai-cost-calculator/src
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

### Configuration Format (JSON)
_Example_
```json
{
 "base_repo_tokens": 50000,
 "agents": {
   "UI": "UI-Agent",
   "Code": "Code-Agent"
 },
 "pipeline": [
   {"from": "User", "to": "UI", "desc": "PR Description", "out": 2000},
   {"from": "UI", "to": "Code", "desc": "Generate UI Code", "out": 2000}
 ]
}
```

---

## Русский

### Структура проекта
```
ai-cost-calculator/src
│
├── .gitignore               # Исключение лишних файлов (pycache, venv)
├── LICENSE                  # Лицензия проекта
├── README.md                # Главное описание
├── requirements.txt         # Список зависимостей
│
├── config/                  # Папка для конфигурационных файлов
│   └── example_pipeline.json # Тестовый JSON на 10 сложных шагов
│
├── core/                     # Исходный код программы
│   ├── __init__.py          # Делает папку модулем Python
│   ├── core.py              # Основная логика генерации Mermaid и подсчета плановых затрат
│   └── models_config.py     # Цены и тарифы провайдеров
│
└── main.py                  # Точка входа для запуска скрипта из консоли
```

Минималистичный Python-скрипт без внешних зависимостей для планового FinOps-аудита мультиагентных ИИ-систем. Он рассчитывает накопление контекста токенов, вычисляет стоимость API-запросов и автоматически строит диаграммы последовательности Mermaid.js на основе одного конфигурационного JSON-файла.

### Основные возможности
* **Плановый FinOps-аудит.** Рассчитывает скользящее окно контекста, учитывая линейное накопление токенов на каждом шаге пайплайна.
* **Генерация Mermaid.js.** Создает готовый код диаграмм для вставки в GitHub Markdown или Draw.io.
* **Визуализация ошибок.** Автоматически подсвечивает сбойные шаги пунктирными стрелками (`-->>`) на основе флага `is_error`.

### Пример вывода планового финансового отчета (Console Output)

```text
=== ФИНАНСОВЫЙ АУДИТ ИИ-АРХИТЕКТУРЫ ===
Отправитель          | Действие / Описание            | Вход (In)  | Выход (Out)  | Стоимость ($)
---------------------------------------------------------------------------------------------
Пользователь (PM)    | ТЗ: 'Добавить кнопку'          | 50,000     | 2,000        | $0.1800
Агент-Интерфейс      | UI-код кнопки                  | 52,000     | 2,000        | $0.1860
---------------------------------------------------------------------------------------------
ОБЩИЙ БЮДЖЕТ ЦИКЛА:
Всего входных токенов: 102,000 (Затраты: $0.3060)
Всего выходных токенов: 4,000 (Затраты: $0.0600)
Финальная стоимость выполнения задачи: $0.3660
```

### Планы по развитию (Roadmap)
- [ ] Добавить поддержку динамических тарифов для разных моделей.
- [ ] Реализовать веб-интерфейс для загрузки JSON файлов через браузер.
- [ ] Интегрировать поддержку параллельных шагов (ветвления пайплайна).

### Лицензия / License
MIT License. Свободно для использования и модификации.
