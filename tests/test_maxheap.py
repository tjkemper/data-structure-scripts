from src.data_structures.maxheap import MaxHeap


def test_insert():
    heap = MaxHeap([])
    assert heap.size() == 0

    heap.insert(42)
    assert heap.size() == 1


def test_extract_max():
    heap = MaxHeap([7, 8, 9])

    max_key = heap.extract_max()
    assert max_key == 9

    max_key = heap.extract_max()
    assert max_key == 8

    max_key = heap.extract_max()
    assert max_key == 7

    max_key = heap.extract_max()
    assert max_key == -1


