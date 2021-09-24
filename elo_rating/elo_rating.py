import math
from typing import Tuple
def calculate_Q(rate: float, C: int = 400) -> float:
    return pow(10, rate/C)

def logistic_curve(x, x0, k, l):
    return l /(1 + math.exp(-k(x - x0)))

def get_expected_score(q1: float, q2: float) -> float:
    return q1 / (q1 + q2)

def get_expected_scores(first_player_rating, second_player_rating) -> Tuple[float, float]:
    q1 = calculate_Q(first_player_rating)
    q2 = calculate_Q(second_player_rating)
    e1 = get_expected_score(q1, q2)
    e1 =  round(e1, 5)
    e2 = round(1 - e1, 5)
    return (e1, e2)

def get_rate_correction(expected_score: float, actual_score: float, multiplier: float = 32.0) -> float:
    return multiplier * (actual_score - expected_score) 


def reajust_rates(first_player_rating: float, second_player_rating: float, first_player_actual_score: float) -> Tuple[float, float]:
    first_player_expected_score, second_player_expected_score = get_expected_scores(first_player_rating, second_player_rating)
    first_player_k_factor = get_k_factor(first_player_rating)
    second_player_k_factor = get_k_factor(second_player_rating)
    first_player_rate_correction = get_rate_correction(first_player_expected_score, first_player_actual_score, first_player_k_factor)
    print(f"A expected {first_player_expected_score} but got {first_player_actual_score}. That gives a correction of {first_player_rate_correction}")
    second_player_rate_correction = get_rate_correction(second_player_expected_score, 1 - first_player_actual_score, second_player_k_factor)
    return (first_player_rating + first_player_rate_correction, second_player_rating + second_player_rate_correction)

def get_k_factor(player_rating: float) -> float:
    return 32.0


def main():
    rate_A, rate_B = (250, 250)
    print(f"A: {rate_A}, B: {rate_B}")
    i = 1
    while True:
        a_score = input(f"{i}: Give score of A (between 0 and 1): ")
        if a_score is None:
            continue
        try:
            a_score = float(a_score)
        except ValueError:
            continue
        if a_score < 0 or a_score > 1:
            continue
        rate_A, rate_B = reajust_rates(rate_A, rate_B, a_score)
        print(f"{i}: ({a_score}, {round(1 - a_score, 5)}) => (A: {rate_A}, B: {rate_B})")
        i += 1


if __name__ == '__main__':
    main()