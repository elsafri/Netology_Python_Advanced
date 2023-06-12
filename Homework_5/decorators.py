import datetime


def logger1(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(f'\nName function: {old_function.__name__}\n')
            f.write(f'current date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n')
            f.write(f'arguments: {args} and {kwargs}\n')
            f.write(f'function return: {result}\n')

            return result

    return new_function


def logger2(path):
    def _logger2(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a') as f:
                f.write(f'\nName function: {old_function.__name__}\n')
                f.write(f'current date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n')
                f.write(f'arguments: {args} and {kwargs}\n')
                f.write(f'function return: {result}\n')
            return result

        return new_function

    return _logger2

