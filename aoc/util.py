import os.path
from time import perf_counter


def timeit(func):
    """Print the time of the function call when it returns."""
    def time_wrap(*args, **kwargs):
        print('{name}() go!'.format(name=func.__name__))
        start = perf_counter()
        returned = func(*args, **kwargs)
        print('{name}() took {elapsed:.3f} seconds.'.format(name=func.__name__,
                                                            elapsed=perf_counter() - start))
        return returned
    return time_wrap


def load_inputs_for_source(source_file):
    base, file = os.path.split(source_file)
    input_file = 'input{}.txt'.format(file.split('.')[0][-2:])
    input_path = '/'.join((base, 'input', input_file))

    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

