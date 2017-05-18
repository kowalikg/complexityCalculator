import zad2pannagabriella as gaba


def init(x):
    return x


def my_function(n):
    for i in range(0, n):
        for j in range(0, n):
            pass


def clean(x):
    pass


if __name__ == '__main__':
    generator = gaba.Generator(init, my_function, clean)

    generator.start(10)
    print(generator.get_function_info())
    print(generator.get_time_function()(100000))
    print(generator.get_size_function()(12))
