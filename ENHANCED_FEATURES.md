# 🚀 Улучшения системы анализа диалогов

## 📋 Обзор улучшений

Система была значительно расширена для повышения качества и глубины анализа диалогов. Добавлены новые этапы, улучшены существующие компоненты и созданы дополнительные инструменты.

## 🆕 Новые компоненты

### 1. Улучшенное извлечение сущностей (Stage 2 Enhanced)

**Файл:** `pipeline/stage2_extract_entities_enhanced.py`
**Промпт:** `prompts/extract_entities_enhanced.txt`

**Улучшения:**
- Расширенный набор категорий барьеров, идей и сигналов
- Контекстный анализ с эмоциональными состояниями
- Уровни экспертности пользователей
- Анализ влияния на решение о покупке
- Структурированные метаданные

**Использование:**
```bash
python pipeline/stage2_extract_entities_enhanced.py
```

### 2. Семантическая кластеризация (Stage 4 Enhanced)

**Файл:** `pipeline/stage4_cluster_enhanced.py`

**Улучшения:**
- Использование TF-IDF и DBSCAN для семантической кластеризации
- Автоматическое определение приоритетов кластеров
- Генерация описаний кластеров
- Метрики семантической связности

**Использование:**
```bash
python pipeline/stage4_cluster_enhanced.py
```

### 3. Контекстный анализ (Stage 2.5)

**Файл:** `pipeline/stage2_5_contextual_analysis.py`

**Возможности:**
- Анализ последовательности проблем в диалогах
- Эмоциональная динамика пользователей
- Выявление корневых причин проблем
- Паттерны экспертности пользователей

**Использование:**
```bash
python pipeline/stage2_5_contextual_analysis.py
```

### 4. Семантическое обогащение (Stage 4.5)

**Файл:** `pipeline/stage4_5_semantic_enrichment.py`

**Возможности:**
- Генерация описаний кластеров
- Предложения по решению проблем
- Метрики влияния кластеров
- Анализ трендов

**Использование:**
```bash
python pipeline/stage4_5_semantic_enrichment.py
```

### 5. Расширенные метрики качества (Stage 7 Enhanced)

**Файл:** `pipeline/stage7_quality_enhanced.py`

**Метрики:**
- Precision, Recall, F1-score для извлечения
- Качество кластеризации и цитат
- Семантическое качество
- Бизнес-метрики
- Общий балл качества

**Использование:**
```bash
python pipeline/stage7_quality_enhanced.py
```

### 6. Интерактивный дашборд

**Файл:** `dashboard/interactive_dashboard.py`

**Возможности:**
- Интерактивные графики с Plotly
- Ключевые метрики в реальном времени
- Детальный анализ кластеров
- Рекомендации по улучшению
- Адаптивный дизайн

**Использование:**
```bash
python dashboard/interactive_dashboard.py
```

### 7. A/B тестирование промптов

**Файл:** `pipeline/ab_testing_prompts.py`

**Возможности:**
- Сравнение разных версий промптов
- Автоматическая оценка качества
- Рекомендации по выбору лучшего промпта
- Статистический анализ результатов

**Использование:**
```bash
python pipeline/ab_testing_prompts.py
```

## 🎯 Enhanced Pipeline Manager

**Файл:** `pipeline_manager_enhanced.py`

Новый менеджер pipeline с поддержкой всех улучшений.

### Предустановленные конфигурации:

```bash
# Базовая конфигурация
python pipeline_manager_enhanced.py --preset basic

# Улучшенная конфигурация (рекомендуется)
python pipeline_manager_enhanced.py --preset enhanced

# Полная конфигурация со всеми этапами
python pipeline_manager_enhanced.py --preset full

# Только анализ качества
python pipeline_manager_enhanced.py --preset quality

# Только A/B тестирование
python pipeline_manager_enhanced.py --preset ab_testing

# Только дашборд
python pipeline_manager_enhanced.py --preset dashboard_only
```

### Запуск конкретных этапов:

```bash
# Запуск улучшенного извлечения и кластеризации
python pipeline_manager_enhanced.py --stages 2_enhanced 4_enhanced 4.5

# Запуск с определенного этапа
python pipeline_manager_enhanced.py --from 2_enhanced

# Запуск до определенного этапа
python pipeline_manager_enhanced.py --to 4.5
```

### Просмотр доступных этапов:

```bash
# Список всех этапов
python pipeline_manager_enhanced.py --list-stages

# Список предустановок
python pipeline_manager_enhanced.py --list-presets
```

## 📊 Новые метрики качества

### Метрики извлечения:
- **Precision:** Точность извлечения сущностей
- **Recall:** Полнота извлечения
- **F1-score:** Гармоническое среднее precision и recall

### Метрики кластеризации:
- **Duplicate Rate:** Процент дублирующихся кластеров
- **Cluster Coherence:** Семантическая связность кластеров
- **Clustering Quality:** Общее качество кластеризации

### Семантические метрики:
- **Concept Diversity:** Разнообразие концепций
- **Semantic Richness:** Богатство семантической информации
- **Context Richness:** Богатство контекстной информации

### Бизнес-метрики:
- **Actionable Insights:** Количество практических инсайтов
- **Priority Distribution:** Распределение приоритетов
- **Solution Feasibility:** Осуществимость решений

## 🔧 Настройка и конфигурация

### Обновление конфигурации моделей

В `config/models.yaml` добавлены новые модели:

```yaml
openai:
  extraction:
    default: gpt-4o-mini
    alt_quality: o3-mini
  labeling:
    default: gpt-4o-mini
    alt_quality: o3-mini
  summary:
    default: gpt-4o-mini
    alt_quality: gpt-4o
```

### Настройка порогов кластеризации

В `pipeline/stage4_cluster_enhanced.py` можно настроить:

```python
# Пороги для семантической кластеризации
barrier_clusters = semantic_cluster(barriers, threshold=0.6)
idea_clusters = semantic_cluster(ideas, threshold=0.7)
signal_clusters = semantic_cluster(signals, threshold=0.8)
```

## 📈 Примеры использования

### 1. Полный анализ с улучшениями

```bash
# Запуск полного enhanced pipeline
python pipeline_manager_enhanced.py --preset enhanced

# Результаты будут в:
# - reports/report.md (улучшенный отчет)
# - reports/interactive_dashboard.html (интерактивный дашборд)
# - reports/quality_enhanced.json (расширенные метрики)
```

### 2. A/B тестирование промптов

```bash
# Тестирование разных промптов
python pipeline_manager_enhanced.py --preset ab_testing

# Результаты в reports/ab_test_results.json
```

### 3. Анализ только качества

```bash
# Быстрый анализ качества существующих данных
python pipeline_manager_enhanced.py --preset quality
```

## 🎨 Интерактивный дашборд

Дашборд включает:

1. **Ключевые метрики** - охват, количество проблем, идей, сигналов
2. **Общий балл качества** - визуальная оценка качества анализа
3. **График тональности** - распределение эмоциональных состояний
4. **Матрица приоритетов** - приоритизация кластеров
5. **Анализ трендов** - динамика по категориям
6. **Детальный анализ кластеров** - с предложениями по решению
7. **Рекомендации** - практические советы по улучшению

## 🔍 Отладка и мониторинг

### Логирование

Все новые компоненты используют структурированное логирование:

```python
import logging
logger = logging.getLogger(__name__)

logger.info("🚀 Запуск этапа...")
logger.error("❌ Ошибка...")
logger.warning("⚠️ Предупреждение...")
```

### Проверка качества

После каждого этапа проверяйте:

1. **Логи** - наличие ошибок и предупреждений
2. **Метрики качества** - `reports/quality_enhanced.json`
3. **Интерактивный дашборд** - визуальная проверка результатов

### Типичные проблемы

1. **Ошибки API** - проверьте настройки OpenAI в `config.py`
2. **Низкое качество кластеризации** - настройте пороги в Stage 4 Enhanced
3. **Пустые результаты** - проверьте входные данные и промпты

## 🚀 Рекомендации по использованию

### Для быстрого старта:
```bash
python pipeline_manager_enhanced.py --preset enhanced
```

### Для глубокого анализа:
```bash
python pipeline_manager_enhanced.py --preset full
```

### Для тестирования промптов:
```bash
python pipeline_manager_enhanced.py --preset ab_testing
```

### Для мониторинга качества:
```bash
python pipeline_manager_enhanced.py --preset quality
```

## 📝 Дополнительные файлы

- `ENHANCED_FEATURES.md` - этот файл с описанием улучшений
- `pipeline_manager_enhanced.py` - новый менеджер pipeline
- `dashboard/interactive_dashboard.py` - интерактивный дашборд
- `pipeline/ab_testing_prompts.py` - A/B тестирование промптов

Все улучшения полностью совместимы с существующей системой и могут использоваться как дополнение к базовому pipeline.
