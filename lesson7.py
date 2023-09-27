"""
Мне не очень нравится, как я сделал это (через итератор).
Возможно можно как-то использовать State монаду.
"""

from pymonad.list import ListMonad


def ConquestCampaign(N: int, M: int, L: int, batalion: list[int]) -> int:
    cells_to_fill = N * M
    propagation = lambda x: ListMonad(
        (x[0], x[1]),
        (x[0] + 1, x[1]),
        (x[0] - 1, x[1]),
        (x[0], x[1] + 1),
        (x[0], x[1] - 1),
    )
    is_valid = (
        lambda x:
        ListMonad((x[0], x[1])) if 0 <= x[0] < N and 0 <= x[1] < M 
        else ListMonad()
    )
    def _inner(positions, days_cnt: int):
        if len(positions) == cells_to_fill:
            return days_cnt
        on_capture = (ListMonad(*positions)
            .bind(propagation)
            .bind(is_valid)
        )
        no_dub = ListMonad(*set(on_capture))  # удаление дубликатов
        return _inner(no_dub, days_cnt + 1)

    batalion_fix = list(map(lambda x: x - 1, batalion))
    positions = [(batalion_fix[2 * (i - 1)], batalion_fix[2 * (i - 1) + 1]) for i in range(L)]
    return _inner(positions, 1)

