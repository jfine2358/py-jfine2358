# `None` is special

## Introduction

Python's founder, Guido van Rossum, wrote \[1]:
> None is so central to using Python that you really can't be using
Python without knowing about None.

This page tells you everything an ordinary Python programmer needs to
know about `None`. (And experts might want to look also at the
(not yet written) next page).

If you use Python, and want help with `None`, please do read on.


## Why `None`?

Sometimes a value is required.  But we're not able to provide one. In
Python, we can use `None` to solve this problem.  For example, here's
an uninitialized list, of length 3.

```python
[None, None, None]
```

In it, `None` is used as a placeholder for a value that is not yet
known.  In Python, it's usually best to use `None` to represent the
absence of a value.

## How is `None` special?

The special properties of `None` follow from its purpose. To represent
the absence of a value.


### The CLI hides `None`

The CLI shows the value of the expression it just evaluated.
```python
>>> 2
2
>>> 2 + 2
4
```

Except where the value is `None`. Then the CLI hides it. Usually, it's not interesting.
```python
>>> None
>>>
```

But the CLI hides `None` as a value, whatever the name of the identifier.
```python
>>> iden = None
>>> iden
>>>
```


Sometimes this is a surprise.
```python
>>> value = ['zero', None, 'two']
>>> value[0]
'zero'
>>> value[1]
>>> value[2]
'two'
```

### Making `None` visible in the CLI

To show `None` in the CLI, do something to make it visible. For
example, use `print`.
```python
>>> val = None
>>> print(val)
None
```

Or `str`.
```python
>>> val = None
>>> str(val)
'None'
```

The CLI shows `None` when it's part of a larger expression. Such as a
tuple.

```python
>>> val = None
>>> (2 + 2, val)
(4, None)

```

### `None` is a constant

The literal `42` has the same value everywhere. The value of `42`
can't be changed. It's always the number 42.

```python
>>> 42 = 0
SyntaxError: can't assign to literal
```

By the way, don't confuse this with
```python
>>> 42 == 0
False
```

Similarly, `None` is available everywhere, and cannot be changed.
```python
>>> None = 0
SyntaxError: can't assign to keyword
```

And similarly, neither can `True` and `False`.
```python
>>> True = 1
SyntaxError: can't assign to keyword
>>> False = 0
SyntaxError: can't assign to keyword
```

In your code, `None` will always have the same value. (And similarly
`True` and `False`.)  Just at `42` always has the same value.


### `None` is the default return value

When function execution *falls off the bottom*, the function
returns `None`. This represents the absence of a value.

```python
>>> def fn():
...     pass  # A do-nothing placeholder statement.
>>> fn()
>>> fn() is None
True
```

Similarly, a `return` statement without an explicit value always
returns `None`.

```python
>>> def fn():
...     return  # No explicit value given.
>>> fn()
>>> fn() is None
True
```

Some languages have procedures. They are like functions, but don't
return a value. Python doesn't have procedures. Instead it has
functions that always return `None`.


###  A list gotcha

The list method `.append` adds an entry to the end of a list. It is
like a procedure. It returns `None`. Here's an example.

```python
>>> my_list = [0, 1, 2]
>>> my_list.append(3) # Return None, so supresses by CLI.
>>> my_list
[0, 1, 2, 3]
```

All fine, until we forget that `.append` changes the list *and then
returns `None`*.

```python
>>> my_list = [0, 1, 2]
>>> longer_list = my_list.append(3)
>>> longer_list.append(4)
AttributeError: 'NoneType' object has no attribute 'append'
>>> my_list
[0, 1, 2, 3]
```

What's happened? The `my_list.append(3)` returns `None`. So
```python
>>> longer_list is None
True
```

### `None` can signal failure

Dictionary key access raises an exception, if the key isn't found.

```python
>>> {}['dne']
KeyError: 'dne'
```

Sometimes, getting an exception is a nuisance. To avoid this, the
`.get` method returns `None`, if the key isn't found.

```python
>>> {}.get('dne') is None
True
```

Here, `None` is the default not-found value. You can supply your own.

```python
>>> {}.get('dne', 42)
42
```

### `None` as a placeholder default

Here's an example
```python
def insort_right(a, x, lo=0, hi=None):
    # ...
    if hi is None:
        hi = len(a)
```

Here, `hi` has a default value. But that value cannot be computed,
until `a` is known. So we use `None` to as a placeholder. And if `hi`
is `None`, then we replace it by `len(a)`.


### `None` has its own type

Here's the main official statement about `None`, from the
[standard types page](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy).

> `None`

> This type has a single value. There is a single object with this
> value. This object is accessed through the built-in name `None`. It
> is used to signify the absence of a value in many situations, e.g.,
> it is returned from functions that don’t explicitly return
> anything. Its truth value is false.


### `None` can't be subclassed

This is advanced, and belongs in the next page.
```python
>>> NoneType = type(None)
>>> class myNoneType(NoneType): pass
TypeError: type 'NoneType' is not an acceptable base type

```

### `None` can't be subclassed

This is advanced, and belongs in the next page.

`None` and a few other things are special-cased by CPython. The
compiler won't bother to write bytecode instructions when an
if-statement obviously evaluates false. That might surprise some
folks.


## Thanks

This page arose from a thread [2] on the python-ideas list. I thank
Steve Dower, Paul Moore, Steve D'Aprano, Chris Barker, David Mertz,
Jörn Heissler, Anthony Risinger, Michael Selik, Chris Angelico for
their contributions and encouragement.


## Epigraphs

> But the most wonderful thing about Tiggers is I'm the only one.

[Richard Morton Sherman](http://disney.wikia.com/wiki/The_Wonderful_Thing_About_Tiggers)

> [A cynic is] a man who knows the price of everything and the value of nothing.

[Oscar Wilde](https://en.wikiquote.org/wiki/Oscar_Wilde)

## References

   \[1] [The story of None, True and False ...](
   http://python-history.blogspot.com/2013/11/the-history-of-bool-true-and-false.html
   ), Guido van Rossum, 2013


   \[2] https://mail.python.org/pipermail/python-ideas/2018-July/052246.html


