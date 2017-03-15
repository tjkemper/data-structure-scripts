from util.pretty_print import get_spaces_array, print_slashes


class Node:
    """Node in a binary tree.

    Attributes:
        left   (Node): Left child.
        right  (Node): Right child.
        parent (Node): Parent.
        data    (int): Data contained in the node.
        height  (int): Height of node in tree.
    """

    def __init__(self, key):
        self.data = key
        self.left, self.right, self.parent = None, None, None
        self.height = 0


class BST:
    """A BST with all the fixings.

    Distinct integers. left <= node < right.

    Attributes:
        root (Node): Root of tree.
        size  (int): Size of tree (number of nodes).
    """

    def __init__(self, integers):
        """Initialize BST.

        :param integers: A list (of distinct integers) to make a BST.
        """
        self.root = None
        self.size = 0

        for i in integers:
            self.insert(i)

    def search(self, value):
        """Search for value in BST.

        :param value: Value to search for.
        :return:      If exists, return node with value. Otherwise, return None.
        """
        return self._search_helper(self.root, value)

    def _search_helper(self, node, value):
        """Perform binary search on BST.

        :param node:  Current node to compare.
        :param value: Value to search for.
        :return:      If exists, return node with value. Otherwise, return None.
        """
        if node is None or node.data == value:
            return node
        else:
            if value <= node.data:
                return self._search_helper(node.left, value)
            else:
                return self._search_helper(node.right, value)

    def insert(self, value):
        """Insert value into BST.

        :param value: The value to insert into the BST.
        """
        self.size += 1
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_helper(self.root, Node(value))

    def _insert_helper(self, curr_node, new_node):
        """Perform binary search on BST and insert new_node.

        ASSERT: curr_node is not None.

        :param curr_node: Current node in BST while traversing.
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

    def delete(self, value):
        """Delete value from BST.

        :param value: The value to delete from the BST.
        :return:      If exists, return value. Otherwise, return None.
        """
        return self._delete_helper(self.root, value)

    def _delete_helper(self, curr_node, value):
        """Perform binary search on BST and delete node with value.

        :param curr_node: Current node in BST while traversing.
        :param value:     The value to delete from the BST.
        :return:          If exists, return value. Otherwise, return None.
        """
        if not curr_node:
            return None  # Node with value does not exist.

        if curr_node.data != value:
            # Have not found node to delete. Continue traversing.
            result = None

            if value <= curr_node.data:
                result = self._delete_helper(curr_node.left,  value)
            else:
                result = self._delete_helper(curr_node.right, value)

            # Maintain node height.
            self.set_node_height(curr_node)

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

            return value  # Because we found value to be deleted.

    def _delete_helper_children_and(self, node):
        """Delete node, which has two children... Like an AND gate :)

        Find and delete predecessor. Set node's value to its predecessor's value.

        :param node: The node to be deleted.
        """
        predecessor = self.get_predecessor(node)
        self._delete_helper(self.root, predecessor.data)  # Delete the predecessor.
        node.data = predecessor.data

    def _delete_helper_children_nand(self, node, child):
        """Delete node, which has zero or one child... Like a NAND gate :)

        :param node:  The node to be deleted.
        :param child: The single child of node, or None if node has no children.
        """
        self.size -= 1
        if node == self.root:  # Oh man, special cases.
            self.root = child
        elif node.data <= node.parent.data:
            # node is left child of node.parent
            node.parent.left = child
        else:
            # node is right child of node.parent
            node.parent.right = child

        if child:
            child.parent = node.parent

    def _get_single_child(self, node):
        """Get single child. Assume node has < 2 children.

        :param node: Node to get child of.
        :return:     The single child of node, or None if node has no children.
        """
        if node.left:
            return node.left
        elif node.right:
            return node.right
        else:
            return None

    def get_predecessor(self, node):
        """Get Predecessor.

        :param node: Node to find the predecessor of.
        :return:     If exists, the predecessor of node. Otherwise, return None.
        """
        if not node or not node.left:
            return None
        else:
            return self._get_max(node.left)

    def _get_max(self, node):
        """Get Max of subtree rooted at node.

        Go right!

        :param node: Current node while finding the max.
        :return:     The maximum node in this subtree.
        """
        if not node.right:
            return node
        else:
            return self._get_max(node.right)

    def in_order(self):
        """In order traversal of BST (starting at root).

        :return: List of elements visited 'in order'.
        """
        integers = []
        self._in_order_helper(self.root, integers)
        return integers

    def _in_order_helper(self, node, integers):
        """In order traversal of BST.

        :param node:     Current node during traversal.
        :param integers: List of elements visited so far.
        """
        if node:
            if node.left:
                self._in_order_helper(node.left, integers)

            integers.append(node.data)

            if node.right:
                self._in_order_helper(node.right, integers)

    def height(self):
        """Return height of BST."""
        return self.node_height(self.root)

    def node_height(self, node):
        """Return height of node."""
        if node:
            return node.height
        else:
            return -1

    def set_node_height(self, node):
        """Set node height to max(left height, right height) + 1.

        Runs in O(1) time.

        :param node: The node to set height for.
        """
        node.height = max(self.node_height(node.left), self.node_height(node.right)) + 1

    def pretty_print(self):
        """Pretty print BST."""
        if self.height() == -1:
            print("Tree is empty.")
            return

        this_level = [self.root]
        height = self.height()
        spaces = get_spaces_array(height)
        num_keys = 1

        while height >= 0:
            next_level = []
            print(" " * spaces[height], end='')
            for n in this_level:
                num_spaces = " " * spaces[height+1]
                print(str(n.data) + num_spaces, end='')
                if n.left:
                    next_level.append(n.left)
                else:
                    next_level.append(Node('x'))
                if n.right:
                    next_level.append(n.right)
                else:
                    next_level.append(Node('x'))
            print()
            print_slashes(height, spaces, num_keys)
            height -= 1
            num_keys *= 2
            this_level = next_level
