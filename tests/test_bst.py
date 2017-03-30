from src.data_structures.bst import BST


def test_bst_height():
    bst = BST([])
    assert bst.height() == -1

    bst = BST([1])
    assert bst.height() == 0

    bst = BST([1, 1])
    assert bst.height() == 1

    bst = BST([1, 1, 1])
    assert bst.height() == 2

    bst = BST([1, 1, 1, 1])
    assert bst.height() == 3
