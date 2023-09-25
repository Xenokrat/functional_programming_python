"""Симуляция торгового автомата
Поддерживает 2 операции, вставить монетку и купить предмет
Если денег достаточно, то предмет будет выдан и изчезнет из автомата, если нет - ничего не произойдет
"""
from pymonad.tools import curry
from pymonad.state import State


coins = {
    "10 cents": 10,
    "5 cents": 5,
    "1 cent": 1,
}


@curry(2)
def insert_coin(coin, item_list):
    def insert_coin_fn(money):
        return item_list, money + coins[coin]
    return State(insert_coin_fn)

@curry(2)
def buy_item(item, item_list):
    def buy_item_fn(money):
        if money >= item_list[item]:
            item_cost = item_list[item]
            del item_list[item]
            return item_list, money - item_cost
        else:
            print("Not enough money")
            return item_list, money
    return State(buy_item_fn)

def run_vending_machine():
    item_list = {
        "Teddy Bear": 20,
        "Fluffy Tiger": 40,
        "Brown Bunny": 11,
        "Tomato": 37,
    }
    return (
        State.insert(item_list)
        .bind(insert_coin('10 cents'))
        .bind(insert_coin('10 cents'))
        .bind(insert_coin('10 cents'))
        .bind(buy_item("Teddy Bear"))
        .bind(buy_item("Fluffy Tiger"))
        .bind(insert_coin('10 cents'))
        .bind(insert_coin('10 cents'))
        .bind(buy_item("Fluffy Tiger"))
        .run(10)
    )


if __name__ == "__main__":
    print(run_vending_machine())