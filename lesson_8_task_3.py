def type_logger(func):
    def wrapper(*args):
        if len(args) == 1:
            print(f'{args[0]}:{type(args[0])}')
        else:
            for el in args:
                print(f'{el}:{type(el)}')
            calc = func(*args)
            return calc

    return wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        print(i ** 3)


calc_cube(5, 6, 8)
