from pymonad.list import ListMonad
from pymonad.tools import curry
from pymonad.maybe import Just, Nothing, Maybe


def show(walk):
    """
    Не нашел метода getValue в библиотеке
    В итоге: возвращаю True, если канатоходец держится, и False, если упал
    """
    print(walk != Nothing)

@curry(2)
def to_left(num, cnt):
    return (
        Nothing if abs(num + cnt[0] - cnt[1]) > 4 
        else Just((num + cnt[0], cnt[1]))
    )
@curry(2)
def to_right(num, cnt):
    return (
        Nothing if abs(num + cnt[1] - cnt[0]) > 4 
        else Just((cnt[0], cnt[1] + num))
    )
banana = lambda x: Nothing

show(Just((0, 0)).bind(to_left(2)).bind(to_right(5)).bind(to_left(-2)))  # False
show(Just((0, 0)).bind(to_left(2)).bind(to_right(5)).bind(to_left(-1)))  # True
show(Just((0, 0)).bind(to_left(2)).bind(to_right(5)).bind(banana).bind(to_left(-2)))  # False
