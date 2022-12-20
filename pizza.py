class Pizza:
    pizza_icons = {'Margherita': '🧀',
                   'Pepperoni': '🍕',
                   'Hawaiian': '🍍'}

    def __eq__(self, other):
        if not isinstance(other, Pizza):
            raise Exception(f'{other} is not of class Pizza')
        return set(self.__class__.recipe) == set(other.__class__.recipe) and self.size == other.size


class Margherita(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
    
    def __init__(self, size='L'):
        self.size = size


class Pepperoni(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size='L'):
        self.size = size


class Hawaiian(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size='L'):
        self.size = size
