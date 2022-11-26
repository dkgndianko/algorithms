DELETE_COST = 1
INSERT_COST = 1
SUBSTITUTE_COST = 1


def levenshtein_distance(first: str, second: str) -> int:
    len_first, len_second = (len(first), len(second))
    if len_first == 0:
        return len_second
    if len_second == 0:
        return len_first
    if first[0] == second[0]:
        return levenshtein_distance(first[1:], second[1:])
    return min(*[
        cost + levenshtein_distance(a, b) for a, b, cost in [
            (first[1:], second, DELETE_COST),
            (first, second[1:], INSERT_COST),
            (first[1:], second[1:], SUBSTITUTE_COST)
        ]
    ])


def test():
    data = [
        ("alpha", "bravo"),
        ("barro", "bravo"),
        ("charlie", "delta"),
        ("charlie", "charles"),
        ("echo", "foxtrot"),
        ("echo", "eco"),
        ("golf", "hotel"),
        ("golf", "gold"),
        ("wolf", "wolf"),
    ]
    for x, y in data:
        distance = levenshtein_distance(x, y)
        print(f"d('{x}', '{y}') = {distance}")


if __name__ == "__main__":
    test()
