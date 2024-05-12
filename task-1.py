import queue
import random

# Створити чергу заявок
queue = queue.Queue()

def generate_request():
    # Створити нову заявку
    new_request = f"Request {random.randint(1, 100)}"
    # Додати заявку до черги
    queue.put(new_request)
    print(f"New request generated: {new_request}")

def process_request():
    # Якщо черга не пуста
    if not queue.empty():
        # Видалити заявку з черги
        processed_request = queue.get()
        # Обробити заявку
        print(f"Processing request: {processed_request}")
    else:
        # Якщо черга пуста
        print("Queue is empty. No requests to process.")

# Головний цикл програми
while True:
    generate_request()
    process_request()