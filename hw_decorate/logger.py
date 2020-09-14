from datetime import datetime


# def logger(old_function):
#
#     def new_function(*args, **kwargs):
#         now = datetime.now()
#         result = old_function(*args, **kwargs)
#         func_name = old_function.__name__
#         with open('logs', 'a', encoding='utf-8') as filewrite:
#             filewrite.write(f'Вызвана функция {func_name} с аргументами {args} {kwargs}. Результат: {result}')
#         return result
#
#     return new_function


def logger(logs_path):

    def _logger(old_function):

        def new_function(*args, **kwargs):
            now = datetime.now()
            result = old_function(*args, **kwargs)
            func_name = old_function.__name__
            with open(logs_path, 'a', encoding='utf-8') as filewrite:
                filewrite.write(f'Вызвана функция {func_name} с аргументами {args} {kwargs}. Результат: {result}\n')
            return result

        return new_function

    return _logger

@logger(logs_path='log.txt')
def hello_world(*args, **kwargs):
    print(args)
    print(kwargs)
    return 1


hello_world('John', 'Smith', '+71234567809', telegram='@johny', email='johny@smith.com')

