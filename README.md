# 🔍 Dialogs RAG Pipeline System

Система анализа диалогов с использованием многоэтапного pipeline и RAG (Retrieval-Augmented Generation) технологии.

## 🏗️ Архитектура

Система построена вокруг **Pipeline Manager** как центрального компонента:

```
┌─────────────────────────────────────────────────────────────┐
│                    Pipeline Manager                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Stage 1   │  │   Stage 2   │  │   Stage 3   │  ...   │
│  │ Детекция    │  │ Извлечение  │  │Нормализация │        │
│  │ доставки    │  │ сущностей   │  │формулировок │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
           │                    │                    │
    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    │ Pipeline    │    │ Pipeline    │    │ Pipeline    │
    │ Core        │    │ API         │    │ Dashboard   │
    │ (Бизнес-    │    │ (REST API)  │    │ (Web UI)    │
    │  логика)    │    │             │    │             │
    └─────────────┘    └─────────────┘    └─────────────┘
```

## ✨ Ключевые возможности

- **Автоматическое извлечение сущностей** из диалогов (барьеры, идеи, сигналы)
- **Умная кластеризация** похожих формулировок
- **Очистка и нормализация** текста
- **Генерация отчетов** в Markdown и Excel
- **REST API** для интеграции
- **Веб-дашборд** для визуализации

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Настройка API ключа
```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. Запуск pipeline
```bash
python pipeline_manager.py --stages all
```

### 4. Запуск полной системы (API + Dashboard)
```bash
# API сервер
python api/pipeline_api.py

# Дашборд (в другом терминале)
python dashboard/pipeline_dashboard.py
```

## 📋 Этапы Pipeline

| Этап | Название | Описание | Входные данные | Выходные данные |
|------|----------|----------|----------------|-----------------|
| 1 | Детекция доставки | Определение диалогов с обсуждением доставки | Excel файл с диалогами | `stage1_delivery.jsonl` |
| 2 | Извлечение сущностей | Извлечение барьеров, идей, сигналов | Результаты этапа 1 | `stage2_extracted.jsonl` |
| 3 | Нормализация формулировок | Приведение к единому виду | Результаты этапа 2 | `stage3_normalized.jsonl` |
| 4 | Кластеризация | Группировка похожих формулировок | Результаты этапа 3 | `stage4_clusters.json` |
| 5 | Агрегация метрик | Расчет статистики и метрик | Результаты этапа 4 | `aggregate_results.json` |
| 6 | Генерация отчетов | Создание финальных отчетов | Результаты этапа 5 | `report.md`, `report.xlsx` |

## 🛠️ Компоненты системы

### Pipeline Manager (`pipeline_manager.py`)
Центральный менеджер для управления всеми этапами:
- Запуск отдельных этапов или всего pipeline
- Управление зависимостями между этапами
- Отслеживание статуса выполнения
- Сохранение состояния pipeline

### Pipeline Core (`core/pipeline_core.py`)
Бизнес-логика системы:
- Управление запросами на анализ
- Асинхронное выполнение pipeline
- Работа с результатами анализа
- Сервис данных

### Pipeline API (`api/pipeline_api.py`)
REST API для управления системой:
- Запуск pipeline через HTTP
- Получение статуса и результатов
- Управление файлами
- Системная информация

### Pipeline Dashboard (`dashboard/pipeline_dashboard.py`)
Веб-интерфейс для управления:
- Визуализация результатов
- Управление pipeline
- Мониторинг системы
- Скачивание отчетов

## 📖 Использование

### CLI интерфейс

```bash
# Запуск всех этапов
python pipeline_manager.py --stages all

# Запуск конкретных этапов
python pipeline_manager.py --stages 1 2 3

# Запуск с определенного этапа
python pipeline_manager.py --from 3

# Запуск до определенного этапа
python pipeline_manager.py --to 4

# Запуск с кастомной конфигурацией
python pipeline_manager.py --stages all --skip-failed
```

### API интерфейс

```bash
# Запуск pipeline
curl -X POST "http://localhost:8000/pipeline/run" \
     -H "Content-Type: application/json" \
     -d '{"input_file": "data/dialogs.xlsx", "stages": ["1", "2", "3", "4", "5", "6"]}'

# Получение статуса
curl "http://localhost:8000/pipeline/status/{request_id}"

# Получение результатов
curl "http://localhost:8000/pipeline/results/{request_id}"

# Список анализов
curl "http://localhost:8000/pipeline/analyses"
```

### Веб-интерфейс

Откройте http://localhost:8501 в браузере для доступа к дашборду.

## 🔧 Конфигурация

### PipelineConfig
```python
@dataclass
class PipelineConfig:
    input_file: str = "data/dialogs.xlsx"
    output_dir: str = "artifacts"
    reports_dir: str = "reports"
    logs_dir: str = "logs"
    batch_size: int = 100
    max_retries: int = 3
    parallel_execution: bool = False
    skip_failed_stages: bool = False
    cleanup_intermediate: bool = False
```

### Переменные окружения
```bash
export OPENAI_API_KEY="your-api-key"
export CHROMA_PATH="./chroma_db"
export LOG_LEVEL="INFO"
```

## 📊 Результаты

После выполнения pipeline результаты сохраняются в:

### Артефакты (`artifacts/`)
- `stage1_delivery.jsonl` - результаты детекции доставки
- `stage2_extracted.jsonl` - извлеченные сущности
- `stage3_normalized.jsonl` - нормализованные формулировки
- `stage4_clusters.json` - кластеры формулировок
- `aggregate_results.json` - агрегированные метрики
- `barriers.csv`, `ideas.csv`, `signals.csv` - CSV отчеты

### Отчеты (`reports/`)
- `report.md` - детальный Markdown отчет
- `report.xlsx` - Excel отчет для анализа
- `appendix_ids.md` - приложение с ID диалогов

## 🔍 Мониторинг

### Логи
- `logs/pipeline_manager.log` - логи pipeline
- `logs/pipeline_api.log` - логи API
- `logs/pipeline_dashboard.log` - логи дашборда

### Метрики
- Время выполнения каждого этапа
- Количество обработанных диалогов
- Статистика ошибок
- Использование ресурсов

## 🚨 Требования

- Python 3.8+
- OpenAI API ключ
- ChromaDB
- Все зависимости из `requirements.txt`

## 🛠️ Разработка

### Структура проекта
```
dialogs-rag/
├── pipeline_manager.py          # Центральный менеджер
├── core/
│   └── pipeline_core.py         # Бизнес-логика
├── api/
│   └── pipeline_api.py          # REST API
├── dashboard/
│   └── pipeline_dashboard.py    # Веб-интерфейс
├── pipeline/                    # Этапы pipeline
│   ├── stage1_detect_delivery.py
│   ├── stage2_extract_entities.py
│   ├── stage3_normalize.py
│   ├── stage4_cluster.py
│   ├── stage5_aggregate.py
│   └── stage6_report.py
├── pipeline_manager.py          # Главный скрипт
└── requirements.txt
```

### Добавление нового этапа
1. Создайте файл `pipeline/stageN_new_stage.py`
2. Добавьте функцию `main()` в файл
3. Обновите `pipeline_manager.py` - добавьте этап в `_initialize_stages()`
4. Обновите зависимости в других этапах при необходимости

### Тестирование
```bash
# Запуск тестов
python -m pytest tests/

# Запуск конкретного этапа
python pipeline/stage1_detect_delivery.py

# Проверка API
curl http://localhost:8000/health
```

## 📞 Поддержка

При возникновении проблем:
1. Проверьте логи в папке `logs/`
2. Убедитесь, что все зависимости установлены
3. Проверьте конфигурацию в `PipelineConfig`
4. Проверьте доступность OpenAI API

---

**Система готова к использованию! 🎉**
