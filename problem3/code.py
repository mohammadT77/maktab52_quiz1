import argparse


def swapcase_decorator(gen):
    def wrapper(*arg, **kwargs):
        for i in gen(*arg, **kwargs):
            yield i.swapcase()

    return wrapper


@swapcase_decorator
def duplicate_words_gen(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    def filter_func(s: str):
        _s = s.lower()
        return bool(len(_s) - len(set(_s)))

    # OR
    return filter(filter_func, content.split())

    # OR
    return (i for i in content.split() if filter_func(i))

    # OR
    for i in content.split():
        if filter_func(i):
            yield i


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', metavar='FILE_PATH', help='enter file path')

    args = parser.parse_args()

    for i in duplicate_words_gen('test.txt'):
        print(i)
