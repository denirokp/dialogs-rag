import json
import re
import sys
from pathlib import Path

# Добавляем корневую папку в путь
sys.path.append(str(Path(__file__).parent.parent))

from utils.turns import split_turns
from pipeline.stage1_5_sample_filter import analyze_dialog
from pipeline.stage2_extract_entities import pick_client_quotes

# Тестовые диалоги
dialog_136110073 = """Оператор: Алло добрый день.
Клиент: Здравствуйте.
Оператор: Слушаю вас.
Клиент: Да, у меня вопрос по рекламе.
Оператор: Да, слушаю.
Клиент: Вот у меня есть объявление, но оно не показывается.
Оператор: Понятно, давайте разберемся.
Клиент: Вообще не хочется, высасывают деньги.
Оператор: Понимаю вашу ситуацию.
Клиент: Да, спасибо."""

dialog_136110136 = """Оператор: Здравствуйте, как дела?
Клиент: Да.
Оператор: Хотите обсудить тариф за успешные сделки?
Клиент: Угу, хорошо. Подумаем.
Оператор: Отлично, ждем вашего решения.
Клиент: Хорошо, спасибо."""

dialog_136110545 = """Оператор: Добрый день, у нас есть строй материалы с доставкой.
Клиент: Ну пойдёт минут 5 могу поговорить.
Оператор: Конечно, расскажу про наши услуги.
Клиент: Ну я правильно понимаю у нас-то сейчас самовывоз и доставка есть конечно правильно подключён ли у меня, только доставкой.
Оператор: Нет вот столько доставка силами продавца.
Клиент: Значит ошиблись.
Клиент: Человек вводит карту, а дальше что происходит?
Оператор: После оплаты товар отправляется курьером.
Клиент: Понятно, спасибо за информацию."""


def test_136110073_platform_noise():
    """Тест: диалог с платформенным шумом должен быть отклонен"""
    dialog = {
        "ID звонка": "136110073",
        "Текст транскрибации": dialog_136110073,
        "Длительность (сек)": 600
    }
    result = analyze_dialog(dialog)
    assert result["valid_sample"] is False
    assert result["reason"] in {"platform_noise", "no_client_kw", "no_marker"}


def test_136110136_platform_noise():
    """Тест: диалог с тарифами должен быть отклонен"""
    dialog = {
        "ID звонка": "136110136", 
        "Текст транскрибации": dialog_136110136,
        "Длительность (сек)": 480
    }
    result = analyze_dialog(dialog)
    assert result["valid_sample"] is False
    assert result["reason"] in {"platform_noise", "no_client_kw", "no_marker"}


def test_136110545_delivery_and_quotes():
    """Тест: диалог с доставкой должен иметь цитаты (может не пройти фильтр из-за отсутствия маркеров)"""
    dialog = {
        "ID звонка": "136110545",
        "Текст транскрибации": dialog_136110545,
        "Длительность (сек)": 900
    }
    result = analyze_dialog(dialog)
    
    # Проверяем, что диалог обрабатывается
    assert result["dialog_id"] == "136110545"
    
    # Проверяем извлечение цитат независимо от результата фильтра
    turns = split_turns(dialog_136110545)
    quotes = pick_client_quotes(turns, limit=3)
    assert len(quotes) >= 1
    # хотя бы одна цитата про самовывоз/доставку
    assert any(re.search(r"(самовывоз|доставк)", q["quote"].lower()) for q in quotes)


def test_quotes_pii_masking():
    """Тест: маскирование PII в цитатах"""
    test_turns = [
        {"speaker": "клиент", "text": "Мой телефон 89123456789, email test@example.com"},
        {"speaker": "клиент", "text": "Нужна доставка курьером"}
    ]
    
    quotes = pick_client_quotes(test_turns, limit=3)
    assert len(quotes) >= 1
    
    # Проверяем, что PII замаскированы
    for quote in quotes:
        assert "[masked-phone]" in quote["quote"] or "89123456789" not in quote["quote"]
        assert "[masked-email]" in quote["quote"] or "test@example.com" not in quote["quote"]


def test_quotes_length_filtering():
    """Тест: фильтрация цитат по длине"""
    test_turns = [
        {"speaker": "клиент", "text": "Да"},  # слишком короткая
        {"speaker": "клиент", "text": "Нужна доставка курьером в Москву"},  # подходящая
        {"speaker": "клиент", "text": "Очень длинная цитата " * 50}  # слишком длинная
    ]
    
    quotes = pick_client_quotes(test_turns, limit=3)
    assert len(quotes) == 1
    assert "доставка курьером" in quotes[0]["quote"]


def test_quotes_two_stage_search():
    """Тест: двухэтапный поиск цитат"""
    test_turns = [
        {"speaker": "клиент", "text": "Просто вопрос"},  # без ключевых слов
        {"speaker": "оператор", "text": "У нас есть доставка СДЭК"},  # оператор с ключевыми словами
        {"speaker": "клиент", "text": "А сколько стоит?"},  # клиент рядом с оператором
        {"speaker": "клиент", "text": "Нужна доставка курьером"}  # клиент с ключевыми словами
    ]
    
    quotes = pick_client_quotes(test_turns, limit=3)
    assert len(quotes) >= 2
    # Должны быть цитаты и от клиента с ключевыми словами, и от клиента рядом с оператором
    assert any("доставка курьером" in q["quote"] for q in quotes)
    assert any("сколько стоит" in q["quote"] for q in quotes)


if __name__ == "__main__":
    # Запуск тестов
    test_136110073_platform_noise()
    print("✅ test_136110073_platform_noise passed")
    
    test_136110136_platform_noise()
    print("✅ test_136110136_platform_noise passed")
    
    test_136110545_delivery_and_quotes()
    print("✅ test_136110545_delivery_and_quotes passed")
    
    test_quotes_pii_masking()
    print("✅ test_quotes_pii_masking passed")
    
    test_quotes_length_filtering()
    print("✅ test_quotes_length_filtering passed")
    
    test_quotes_two_stage_search()
    print("✅ test_quotes_two_stage_search passed")
    
    print("\n🎉 Все тесты прошли успешно!")
