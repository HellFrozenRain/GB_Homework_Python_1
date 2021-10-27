from functools import wraps

def wrapper(func):

    @wraps(func)
    def my_wrapper(*args, **kwargs):
        args_type = [f'{arg}: {type(arg)}' for arg in args]
        kwargs_type = [f'{kwargs[kwarg]}: {type(kwargs[kwarg])}' for kwarg in kwargs]
        result_types = [*args_type, *kwargs_type]
        print(f"{func.__name__}({', '.join(result_types)})")
        return func(*args)

    return my_wrapper

@wrapper
def calc_cube(*args):

    return list(map(lambda x: x ** 3, args))

print(calc_cube(3, 5, 7.5, x = '6', y = [1, 'a']))
