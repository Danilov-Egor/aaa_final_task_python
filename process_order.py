import random


def log(arg):
    if callable(arg):
        def wrapper(*args):
            return f'{arg.__name__} — {arg(*args)}c!'
        return wrapper
    else:
        def decorator(func):
            def wrapper2(*args):
                return arg.format(func(*args))
            return wrapper2
        return decorator


@log('\U0001F468\u200D\U0001F373 Приготовили за {}с!')
def bake(pizza):
    """Готовит пиццу"""
    return random.randint(1, 6)


@log('Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""
    return random.randint(1, 6)


@log('Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    return random.randint(1, 6)
