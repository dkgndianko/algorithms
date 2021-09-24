from itertools import chain
from functools import reduce
class Flattened(object):

    def __init__(self, l) -> None:
        self.iter_list = iter(l)
        self.current_list = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_list:
            try:
                element = next(self.current_list)
            except StopIteration:
                self.current_list = None
                element = next(self)
        else:
            element = next(self.iter_list)
            if isinstance(element, list):
                self.current_list =  Flattened(element)
                element = next(self)
        return element

def flatten_with_yeild(l):
    for element in l:
        if isinstance(element, list):
            gen = flatten_with_yeild(element)
            for el in gen:
                yield el
        else:
            yield element

def flatten_with_reduce(l):
    return reduce(lambda acc, el: acc + (flatten_with_reduce(el) if isinstance(el, list) else [el]), l, [])

def flatten_with_chain(l):
    return chain(*[flatten_with_chain(el) if isinstance(el, list) else [el] for el in l])

def test_flatten():
    input_list = [2, [2, 3, 4], 5, [6, 7, 8, 9], [[10], [11, [12, 13, 14], 15]]]
    functions = [Flattened, flatten_with_yeild, flatten_with_reduce, flatten_with_chain]
    for flatten_function in functions:
        result = flatten_function(input_list)
        print(f"{flatten_function.__name__}: {list(result)}")


if __name__ == '__main__':
    # main()
    test_flatten()