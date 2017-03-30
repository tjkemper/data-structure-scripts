from src.data_structures.avl import AVL


def test_avl_height():
    avl = AVL([])
    assert avl.height() == -1

    avl = AVL([1])
    assert avl.height() == 0

    avl = AVL([1, 1])
    assert avl.height() == 1

    avl = AVL([1, 1, 1])
    assert avl.height() == 1

    avl = AVL([1, 1, 1, 1])
    assert avl.height() == 2
