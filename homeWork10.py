def call_times(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            result = func(*args, **kwargs)
            with open(file_name, 'a') as f:
                f.write(f'{func.__name__} была вызвана {count} раза.\n')
            return result
        count = 0
        return wrapper
    return decorator


@call_times('call_count.txt')
def func():
    pass