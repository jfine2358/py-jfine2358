''' $ python3 itertools.py
[('1', '2', '3')]

[[], [], []]
()
[('1', '2', '3')]

[[], ['2'], ['3', '3']]
()
[('1', '2', '3')]

[['3'], [], []]
('3', '2')
[('3', '2', '1')]
'''

# I find this page unhelpful.
# https://docs.python.org/3/reference/compound_stmts.html#function-definitions
# https://andypi.co.uk/2018/04/28/make-code-easier-read-explicitly-named-parameters-python-3/
# https://www.python.org/dev/peps/pep-0570/ # Python Positional-Only Parameters

# Finally, I find this.
# https://www.python.org/dev/peps/pep-3102/ # Keyword-Only Arguments

def zipclose(*argv, close):
    '''As zip(*argv), but call close before raising StopIteration.

    Sentinel value close=None means don't call close. So just like
    zip.  Otherwise, call close(iterators, value) just before raising
    StopIteration.

    The iterators argument is tuple(map(iter, argv)) The value
    argument is incomplete 'next item', as a tuple. Always, len(value)
    < len(argv).

    For an example close function, see residue_zip_close.
    '''

    iterators = tuple(map(iter, argv))

    while True:
        value = []

        try:
            for it in iterators:
                value.append(next(it))
        except StopIteration:
            if close is not None:
                # Maybe use yield from?
                close(iterators, tuple(value))
            raise StopIteration
        yield tuple(value)


class ZipResidueError(Exception):
    pass


def residue_zip_close(iterators, value):
    '''
    zipclose(*argv, close=unequal_zip_close)

    '''

    if value:
        raise ZipResidueError

    for it in iterators:
        try:
            next(it)
        except StopIteration:
            pass
        else:
            raise ZipResidueError


def test_zipclose(*argv):

    def close(iterators, value):
        print(list(map(list, iterators)))
        print(value)

    value = list(zipclose(*argv, close=close))
    print(value)

zc1 = zipclose('1', '2', '3', close=None)

print(list(zc1))

print()
test_zipclose('1', '2', '3')

print()
test_zipclose('1', '22', '333')

print()
test_zipclose('333', '22', '1')



# Idea: async zip
# Idea: greedy async zip
