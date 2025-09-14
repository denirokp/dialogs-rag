# 🎯 ФИНАЛЬНАЯ СИСТЕМА DoD - "КАЧЕСТВО КАК CHATGPT-5"

## 📋 Обзор

Полная система анализа диалогов с соблюдением Definition of Done (DoD), включающая все компоненты: самообучение, A/B тесты, мониторинг качества, автокоррекцию и масштабирование.

## 🏗️ Архитектура системы

### Основные компоненты

1. **DoD Core Components**
   - `taxonomy.yaml` - Таксономия с 11 темами и 25 подтемами
   - `schemas/mentions.schema.json` - JSON схема для валидации
   - `prompts/universal_extractor_ru.txt` - Промпт для извлечения

2. **Processing Pipeline**
   - `comprehensive_dod_pipeline.py` - Основной пайплайн
   - `scripts/dedup.py` - Дедупликация (≤1%)
   - `scripts/clusterize.py` - Кластеризация UMAP + HDBSCAN
   - `scripts/eval_extraction.py` - Оценка micro-F1 ≥ 0.90

3. **Quality Assurance**
   - `quality/checks.sql` - SQL проверки DoD (Q1-Q4)
   - `quality/run_checks.py` - Запуск проверок качества
   - `sql/build_summaries.sql` - Построение сводок

4. **Enhanced Features**
   - `enhanced/integrated_system.py` - Интегрированная система качества
   - `enhanced/quality_autocorrection.py` - Автокоррекция качества
   - `enhanced/adaptive_prompts.py` - Адаптивные промпты с A/B тестами
   - `enhanced/continuous_learning.py` - Непрерывное обучение
   - `enhanced/quality_monitoring.py` - Мониторинг качества
   - `enhanced/scaling_optimizer.py` - Масштабирование

5. **Reports & Templates**
   - `reports/templates/summary.jinja` - Основной отчет
   - `reports/templates/subtheme_card.jinja` - Карточка подтемы
   - `reports/templates/dialog_card.jinja` - Карточка диалога

6. **Automation & CI**
   - `Makefile` - Автоматизация процессов
   - `.github/workflows/qa.yml` - CI/CD пайплайн

## 🎯 DoD Требования (Definition of Done)

### Обязательные критерии качества

- **Evidence-100**: Все упоминания имеют непустые цитаты
- **Client-only-100**: Только реплики клиента как источник фактов
- **Schema-valid-100**: Все извлечения соответствуют JSON схеме
- **Dedup ≤1%**: Дубликаты составляют не более 1% от общего числа
- **Coverage ≥98%**: Категория "прочее" не более 2% от всех упоминаний
- **micro-F1 ≥ 0.90**: На gold standard оценке

### Дополнительные требования

- **Ambiguity-report**: Отчет по распределению уверенности
- **Descriptive analytics only**: Только описательная аналитика, без рекомендаций
- **No business metrics**: Никаких бизнес-метрик в отчетах

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
make install
```

### 2. Тестирование системы

```bash
# Полное тестирование
make test

# Быстрые тесты
make test-quick

# Финальное тестирование DoD
python final_system_test.py
```

### 3. Запуск полного цикла DoD

```bash
# Очистка + установка + тестирование + обработка + проверки
make dod-full
```

### 4. Обработка данных

```bash
# Комплексная обработка с DoD
python comprehensive_dod_pipeline.py --input data/dialogs.xlsx --output artifacts
```

## 📊 Структура данных

### Входные данные

Диалоги в формате:
```json
{
  "dialog_id": 1,
  "turns": [
    {"role": "client", "text": "У меня проблема с доставкой"},
    {"role": "operator", "text": "Понимаю, помогу разобраться"}
  ]
}
```

### Выходные данные

Упоминания в формате:
```json
{
  "dialog_id": 1,
  "turn_id": 0,
  "theme": "доставка",
  "subtheme": "не работает выборочно",
  "label_type": "барьер",
  "text_quote": "У меня проблема с доставкой",
  "delivery_type": "complaint",
  "cause_hint": "причина указана",
  "confidence": 0.95
}
```

## 🔧 Конфигурация

### Основные настройки

```json
{
  "processing": {
    "enable_validation": true,
    "enable_dedup": true,
    "enable_clustering": true,
    "enable_quality_checks": true,
    "enable_autocorrection": true,
    "enable_adaptive_prompts": true,
    "enable_continuous_learning": true,
    "enable_monitoring": true,
    "enable_scaling": true,
    "max_dialogs_per_batch": 1000,
    "quality_threshold": 0.6
  }
}
```

## 📈 Мониторинг и метрики

### DoD метрики

- **Evidence-100**: Количество пустых цитат = 0
- **Client-only-100**: Количество не-клиентских упоминаний = 0
- **Dedup**: Процент дубликатов ≤ 1%
- **Coverage**: Процент "прочее" ≤ 2%

### Качественные метрики

- **micro-F1**: Точность извлечения ≥ 0.90
- **Confidence distribution**: Распределение уверенности
- **Processing speed**: Скорость обработки диалогов/сек

## 🧪 Тестирование

### Типы тестов

1. **Unit Tests**: Тестирование отдельных компонентов
2. **Integration Tests**: Тестирование интеграции компонентов
3. **DoD Tests**: Проверка соответствия DoD требованиям
4. **Performance Tests**: Тестирование производительности

### Запуск тестов

```bash
# Все тесты
python final_system_test.py

# Отдельные компоненты
python -c "from final_system_test import test_taxonomy; test_taxonomy()"
python -c "from final_system_test import test_schema; test_schema()"
```

## 📁 Структура файлов

```
dialogs-rag/
├── taxonomy.yaml                    # Таксономия тем/подтем
├── schemas/mentions.schema.json     # JSON схема валидации
├── prompts/universal_extractor_ru.txt # Промпт извлечения
├── scripts/
│   ├── dedup.py                     # Дедупликация
│   ├── clusterize.py                # Кластеризация
│   └── eval_extraction.py           # Оценка качества
├── quality/
│   ├── checks.sql                   # SQL проверки DoD
│   └── run_checks.py                # Запуск проверок
├── sql/build_summaries.sql          # SQL сводки
├── reports/templates/                # Jinja шаблоны
├── enhanced/                        # Расширенные компоненты
├── comprehensive_dod_pipeline.py    # Основной пайплайн
├── final_system_test.py             # Тестирование
├── Makefile                         # Автоматизация
└── .github/workflows/qa.yml         # CI/CD
```

## 🔄 CI/CD Pipeline

### Автоматические проверки

1. **При каждом PR**: Запуск `make qa` и `make eval`
2. **При push в main**: Полное тестирование системы
3. **DoD compliance**: Проверка всех критериев качества

### Статус проверок

- ✅ **Passed**: Все DoD требования выполнены
- ❌ **Failed**: Нарушение DoD требований
- ⚠️ **Warning**: Предупреждения о качестве

## 📊 Отчеты

### Типы отчетов

1. **Summary Report**: Общая статистика по диалогам
2. **Subtheme Cards**: Детальный анализ подтем
3. **Dialog Cards**: Анализ отдельных диалогов
4. **Quality Report**: Отчет по качеству DoD

### Генерация отчетов

```bash
make report
```

## 🚨 Troubleshooting

### Частые проблемы

1. **ModuleNotFoundError**: Установите зависимости `make install`
2. **DoD validation failed**: Проверьте качество входных данных
3. **Redis connection error**: Система работает без кэширования
4. **SQL errors**: Проверьте структуру данных

### Логи

- Основные логи: `logs/comprehensive_dod_pipeline.log`
- Тестирование: `logs/final_system_test.log`
- Мониторинг: `logs/quality_monitoring.log`

## 🎉 Заключение

Система полностью готова к использованию и соответствует всем требованиям DoD "качество как ChatGPT-5". Все компоненты протестированы и работают корректно.

### Ключевые достижения

- ✅ Полная автоматизация DoD проверок
- ✅ Интегрированная система качества
- ✅ A/B тестирование и самообучение
- ✅ Масштабируемая архитектура
- ✅ Comprehensive тестирование
- ✅ CI/CD интеграция

---

*Система создана в соответствии с требованиями Definition of Done для обеспечения качества анализа диалогов на уровне ChatGPT-5.*
