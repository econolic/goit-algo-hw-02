import queue
import time
import random

# Глобальні лічильники для статистики
request_id_counter = 0         # Загальна кількість згенерованих заявок
processed_requests_count = 0   # Загальна кількість оброблених заявок
total_processing_time = 0.0    # Сумарний час, витрачений на обробку всіх заявок

# Створення черги заявок
application_queue = queue.Queue()

def generate_request():
    """
    Генерує нову заявку з унікальним ID та додає її до черги.
    """
    global request_id_counter
    request_id_counter += 1
    # Створення нової заявки
    new_request = {"id": request_id_counter, "data": f"Заявка номер {request_id_counter}"}
    # Додання заявки до черги
    application_queue.put(new_request)
    print(f"✅ Нова заявка згенерована: ID {new_request['id']}")

def process_request():
    """
    Обробляє заявку, видаляючи її з черги.
    Якщо черга пуста, виводить відповідне повідомлення.
    """
    global processed_requests_count
    global total_processing_time

    if not application_queue.empty():
        # Видалення заявку з черги
        current_request = application_queue.get()
        print(f"⚙️ Обробка заявки: ID {current_request['id']} - {current_request['data']}")

        # Імітація часу на обробку (від 0.5 до 2.5 секунд)
        processing_delay = random.uniform(0.5, 2.5)
        time.sleep(processing_delay)

        # Оновлення статистики
        processed_requests_count += 1
        total_processing_time += processing_delay

        print(f"🟢 Заявка ID {current_request['id']} оброблена за {processing_delay:.2f} сек.")
        application_queue.task_done() # Позначити задачу як виконану
    else:
        # Виведення повідомлення, що черга пуста
        print("ℹ️ Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
if __name__ == "__main__":
    print("Сервісний центр розпочав роботу...")
    start_time = time.time() # Для загального часу роботи

    try:
        while True:
            # Імітуємо випадкову генерацію заявок
            # Зменшимо частоту генерації, щоб обробка встигала
            if random.random() < 0.4: # ~40% шанс згенерувати заявку
                generate_request()

            # Імітуємо випадкову обробку заявок, якщо вони є
            if not application_queue.empty():
                # Збільшимо шанс обробки, якщо є заявки
                if random.random() < 0.8 or application_queue.qsize() > 3:
                    process_request()
            else:
                pass

            # Невеликий інтервал для імітації реального часу
            # Зменшимо основний sleep, щоб частіше перевіряти можливість генерації/обробки
            time.sleep(random.uniform(0.2, 0.8))

    except KeyboardInterrupt:
        print("\n🚪 Сервісний центр завершує роботу...")
        # Обробка залишкових заявок перед виходом
        print("Обробка залишкових заявок...")
        while not application_queue.empty():
            process_request()

        end_time = time.time() # Час завершення роботи
        total_runtime = end_time - start_time

        print("\n--- Статистика роботи сервісного центру ---")
        print(f"Загальний час роботи: {total_runtime:.2f} сек.")
        print(f"Всього згенеровано заявок: {request_id_counter}")
        print(f"Всього оброблено заявок: {processed_requests_count}")

        if processed_requests_count > 0:
            # Обчислення середнього часу обробки
            average_processing_time = total_processing_time / processed_requests_count
            print(f"Середній час обробки однієї заявки: {average_processing_time:.2f} сек.")
            # Обчислення середньої швидкості обробки
            throughput_per_processing_time = processed_requests_count / total_processing_time if total_processing_time > 0 else 0
            print(f"Середня швидкість обробки: {throughput_per_processing_time:.2f} заявки/сек.")
        else:
            print("Жодної заявки не було оброблено.")

        print("Всі доступні заявки оброблені. До побачення!")