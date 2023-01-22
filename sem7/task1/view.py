
import validator

def show_answer(data):
    print(f'Ответ: {data}')

def view_data(data):
    print(data)

def get_value(text):
    result = input(text)
    while not validator.is_num(result):
        print('Нужно ввести число. Попробуйте снова: ')
        result = input()
    return int(result)

def get_complex_value(text):
    result = input(text)
    while not validator.is_complex(result):
        print('Нужно ввести комплексное число. Попробуйте снова: ')
        result = input()
    return complex(result)

def get_sign():
    return input('Введите знак операции (например, +): ')



