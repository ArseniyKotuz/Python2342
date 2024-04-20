from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def calculate(num):
    total = sum((x for x in range(0, num**2)))
    return total

if __name__ == '__main__':
    calculate(10)
    calculate(100)
    calculate(1000)
    calculate(5000)
