# The Issue

The problem occurs where after trying to perform tab completion in, say,
IPython, the completion happens but a space is inserted afterwards, whether
this is needed or not.

# Why It Occurs

Continuum apparently doesn't really care all that much about Linux, so they
decided to compile with a broken readline.so file for their 'readline' recipe.

# The Fix

Remove Continuum/Anaconda's readline package, the associated shared object, and
install the correct one via pip.

## Determine where the shared object is

In the Python shell, you might get something like:

```
>> import readline 
>> readline._rl
 ~/anaconda/lib/python2.7/lib-dynload/readline.so
```

## Remove and Reinstall

```
conda remove readline
rm ~/anaconda/lib/python2.7/lib-dynload/readline.so
pip install readline
```
