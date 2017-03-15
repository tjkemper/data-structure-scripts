from data_structures.bst import BST


class AVL(BST):
    """An AVL tree with all the fixings (subclass of BST).

    Distinct integers. left <= node < right.

    Attributes:
        root (Node): Root of tree.
        size  (int): Size of tree (number of nodes).
    """

    def __init__(self, integers):
        BST.__init__(self, integers)

    def _insert_helper(self, curr_node, new_node):
        """Perform binary search on AVL tree and insert new_node.

        ASSERT: curr_node is not None.

        After insertion, retain AVL rep invariant (keep it balanced).

        :param curr_node: Current node in AVL tree while traversing.
        :param new_node:  The node to insert.
        """
        if new_node.data <= curr_node.data:
            if curr_node.left:
                # Traverse left.
                self._insert_helper(curr_node.left, new_node)
            else:
                # Insert left.
                curr_node.left = new_node
                new_node.parent = curr_node
        else:
            if curr_node.right:
                # Traverse right.
                self._insert_helper(curr_node.right, new_node)
            else:
                # Insert right.
                curr_node.right = new_node
                new_node.parent = curr_node

        # Maintain node height.
        self.set_node_height(curr_node)

        self._balance_node(curr_node)

    def _delete_helper(self, curr_node, value):
        """Perform binary search on AVL tree and delete node with value.

        After insertion, retain AVL rep invariant (keep it balanced).

        :param curr_node: Current node in AVL tree while traversing.
        :param value:     The value to delete from the BST.
        :return:          If exists, return value. Otherwise, return None.
        """
        if not curr_node:
            return None  # Node with value does not exist.

        if curr_node.data != value:
            # Have not found node to delete. Continue traversing.
            result = None

            if value <= curr_node.data:
                result = self._delete_helper(curr_node.left, value)
            else:
                result = self._delete_helper(curr_node.right, value)

            # Maintain node height.
            self.set_node_height(curr_node)

            self._balance_node(curr_node)

            return result
        else:
            # Delete curr_node.
            if curr_node.left and curr_node.right:
                self._delete_helper_children_and(curr_node)
            else:
                child = self._get_single_child(curr_node)
                self._delete_helper_children_nand(curr_node, child)

            # Maintain node height.
            self.set_node_height(curr_node)

            self._balance_node(curr_node)

            return value  # Because we found value to be deleted.

    def _balance_node(self, node):
        """Balance node.

        Node is balanced iff:
            |left subtree height - right subtree height| <= 1

        :param node: The node to balance.
        """
        diff = self.subtree_height_diff(node)
        if diff > 1:
            # Left subtree heavy.
            left_diff = self.subtree_height_diff(node.left)
            if left_diff >= 0:
                self.right_rotate(node)
            else:
                self.zigzag(node)
        elif diff < -1:
            # Right subtree heavy.
            right_diff = self.subtree_height_diff(node.right)
            if right_diff <= 0:
                self.left_rotate(node)
            else:
                self.zagzig(node)

    def subtree_height_diff(self, node):
        """Get difference in height between left and right subtrees.

        \b
        Return value
            > 0 if left is heavy.
            < 0 if right is heavy.
            = 0 if heights are the same.

        :param node: Root of some tree.
        :return:     The height difference.
        """
        left_height  = self.node_height(node.left)
        right_height = self.node_height(node.right)
        return left_height - right_height

    def left_rotate(self, node):
        """Left rotate.

        :param node: The node to rotate left.
        """
        node_x = node
        node_y = node.right

        if not node_y:
            raise Exception("Cannot rotate left.")

        # Maintain pointers.
        if node_x == self.root:
            self.root = node_y
        elif node_x.data <= node_x.parent.data:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.parent = node_x.parent
        node_x.parent = node_y
        node_x.right = node_y.left
        if node_x.right:
            node_x.right.parent = node_x
        node_y.left = node_x

        # Maintain node heights.
        self.set_node_height(node_x)
        self.set_node_height(node_y)

    def right_rotate(self, node):
        """Right rotate.

        :param node: The node to rotate right.
        """
        node_x = node
        node_y = node.left

        if not node_y:
            raise Exception("Cannot rotate right.")

        # Maintain pointers.
        if node_x == self.root:
            self.root = node_y
        elif node_x.data <= node_x.parent.data:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.parent = node_x.parent
        node_x.parent = node_y
        node_x.left = node_y.right
        if node_x.left:
            node_x.left.parent = node_x
        node_y.right = node_x

        # Maintain node heights.
        self.set_node_height(node_x)
        self.set_node_height(node_y)

    def zigzag(self, node):
        """Zigzag.

        Left rotate then right rotate.

          o
         /
        o
         \
          o

        :param node: The node to zigzag.
        """
        if not node.left:
            raise Exception("Cannot zigzag.")

        self.left_rotate(node.left)
        self.right_rotate(node)

    def zagzig(self, node):
        """Zagzig.

        Right rotate then left rotate.

        o
         \
          o
         /
        o

        :param node: The node to zagzig.
        """
        if not node.right:
            raise Exception("Cannot zagzig.")

        self.right_rotate(node.right)
        self.left_rotate(node)
