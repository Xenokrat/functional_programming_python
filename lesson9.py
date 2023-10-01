from functools import reduce


def _odometer(
    distance_time_tuple: tuple[int, int], 
    speed_time_tuple: tuple[int, int],) -> tuple[int, int]:

    delta = speed_time_tuple[1] - distance_time_tuple[1]
    return (distance_time_tuple[0] + delta * speed_time_tuple[0], speed_time_tuple[1])

def odometer(oksana: list[int]) -> int:
    better_oksana = [(oksana[2*i], oksana[2*i + 1]) for i in range(len(oksana) // 2)]
    # will give [(15, 1), (25, 2), (30, 3), (10, 5)]
    return reduce(_odometer, better_oksana, (0, 0))[0]