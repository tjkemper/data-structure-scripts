# Data Structure Scripts

Python scripts leveraging data structures.

### Data Structures
* [Max Heap](#maxheap-usage)
* [AVL Tree](#avl-usage)

### Setup
install `virtualenv`

```
pip3 install virtualenv
```

create virtual environment (ensure you are in root of repo).

```
virtualenv venv
. venv/bin/activate
pip install --editable .
```

### More on `virtualenv`
specify any python version for virtualenv.

```
virtualenv -p `which python3.6` venv
```


### Teardown
Go back to the *real* world.

```
deactivate
```

# `maxheap` usage

**Return max heap.**

```
maxheap input1.txt
```

**Pretty print max heap.**

```
maxheap input1.txt --pretty-print
```

**Return sorted list (descending).**

```
maxheap input1.txt --sort
```

**More information.**

```
maxheap --help
```

# `avl` usage

**Return sorted list (ascending).**
* Accompished by doing an **in order** traversal of the AVL tree.

```
avl input1.txt
```

**Pretty print AVL tree.**

```
avl input1.txt --pretty-print
```

**More information.**

```
avl --help
```
