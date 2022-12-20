import click
from pizza import *
import process_order as pro


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='L')
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str) -> None:
    """Готовит и доставляет пиццу"""
    print(pro.bake(pizza))
    if delivery:
        print(pro.delivery(pizza))
    else:
        print(pro.pickup(pizza))


@cli.command()
def menu(pizza_icons=Pizza.pizza_icons):
    """Выводит меню"""
    pizzas = {'Margherita': Margherita.recipe, 
              'Pepperoni': Pepperoni.recipe, 
              'Hawaiian': Hawaiian.recipe
              }

    for key, val in pizzas.items():
        print(f'- {key} {pizza_icons.get(key, "")}: {", ".join(val)}')


if __name__ == '__main__':
    cli()
