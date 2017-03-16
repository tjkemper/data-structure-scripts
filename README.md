# Data Structure Scripts

CLI for data structures.

### Data Structures
* [Max Heap](#maxheap-usage)
* [AVL Tree](#avl-usage)

### Setup

**Ensure you have `python3` and `pip3`**

```
python3 --version
pip3 --version
```

**Clone repository.**

```
git clone https://github.com/tjkemper/data-structure-scripts.git
cd data-structure-scripts/
```

**`make` all the things!** *(Sets up virtual environment)*

```
make
```

**Activate virtual environment.**

```
. venv/bin/activate
```

### Teardown
**Deactivate virtual environment.** *(Go back to the real world)*

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
