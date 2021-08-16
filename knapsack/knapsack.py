from typing import List
from collections import namedtuple

Candidate = namedtuple('Candidate', ['id', 'value', 'weight'])
CandidateResult = namedtuple('CandidateResult', ['id', 'taken'])
KnapsackResult = namedtuple('knapsackResult', ['total', 'results'])


def knapsack(candidates: List[Candidate], target: float) -> KnapsackResult:
    """
    This is the implementation of 0-1 knapsack. See https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem.
    :param candidates: (List[Candidate]) list of candidates
    :param target: (float) the total sum of values to meet or to get close to
    :return: (KnapsackResult) the result holding the maximum total sum of values met and the list of candidates telling
    for each if it is chosen or not
    """
    if len(candidates) == 0:
        return KnapsackResult(0, [])
    first = candidates[0]
    others = candidates[1:]
    if first.weight > target:
        _t, _r = knapsack(others, target)
        return KnapsackResult(_t, [CandidateResult(first.id, False)] + _r)
    with_others = knapsack(others, target)
    with_first = knapsack(others, target - first.weight)
    if with_others.total > with_first.total + first.value:
        total = with_others.total
        results = [CandidateResult(first.id, False)] + with_others.results
    else:
        total = with_first.total + first.value
        results = [CandidateResult(first.id, True)] + with_first.results
    return KnapsackResult(total, results)



# from utils.memoization import memoize
# def generate_knapsack_key(c, t):
#     return '_'.join([str(_c.id) for _c in c]) + "_{}".format(t)


# knapsack = memoize(knapsack, generate_knapsack_key)
