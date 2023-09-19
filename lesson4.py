# 4.1
from pymonad.tools import curry
from pymonad.maybe import Just, Maybe
from pymoand.list import ListMonad


@curry(2)
def add(x: int, y: int):
    return x + y

add10 = add(10)
Maybe.apply(add10).to_arguments(Just(10))  # Just(20)
ListMonad(1, 2, 3, 4, 5).map(add10)        # ListMonad [11, 12, 13, 14, 15]