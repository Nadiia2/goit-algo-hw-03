from collections import deque

def is_palindrome(input_str):
  
    char_str = deque()

    # Перетворюємо рядок в нижній регістр і видаляємо пробіли
    input_str = input_str.lower().replace(" ", "")

    # Додаємо символи рядка до двосторонньої черги
    for char in input_str:
        char_str.append(char)

    # Порівнюємо символи з обох кінців черги для визначення, чи є рядок паліндромом
    while len(char_str) > 1:
        if char_str.popleft() != char_str.pop():
            return False

    return True

# input_string = "A man a plan a canal Panama"
# print(is_palindrome(input_string)) 