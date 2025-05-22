from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом, використовуючи deque.
    Функція нечутлива до регістру та пробілів.
    :param s: Вхідний рядок
    :return: True, якщо рядок є паліндромом, інакше False
    """
    # Робимо рядок нечутливим до регістру та видаляємо пробіли
    processed_s = "".join(filter(str.isalnum, s)).lower()

    # Створюємо deque з символів обробленого рядка
    char_deque = deque(processed_s)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        # char_deque.popleft() - видаляє та повертає перший елемент (зліва).
        # char_deque.pop() - видаляє та повертає останній елемент (справа).
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

if __name__ == "__main__":
    # Тестові повідомлення для результатів
    result_messages = {
        True: "є паліндромом",
        False: "це не паліндром"
    }

    test_cases = [
        "Мадам", # Паліндром з одного слова
        "А роза упала на лапу Азора",
        "Race car!", # Паліндром з пробілами та знаками пунктуації
        "hello",
        "No lemon, no melon.",
        "Was it a car or a cat I saw?",
        "Eva, can I see bees in a cave?",
        "",  # Порожній рядок
        "a", # Рядок з одним символом
        "  A b B a  ", # Рядок з пробілами на початку/кінці та всередині
        "12321", # Числовий паліндром
        "12345", # Числовий не-паліндром
        "!!!!", # Паліндром зі спеціальних символів
        "Абвггвба", # Паліндром з парною кількістю символів
        "Абвгвба"   # Паліндром з непарною кількістю символів
    ]

    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' {result_messages[result]}")