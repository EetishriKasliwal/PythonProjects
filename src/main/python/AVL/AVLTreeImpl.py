class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    def insert_node(self, root, key):
        """
        Inserts a node into the AVL tree
        :param root: the root/ head node
        :param key: value to be entered
        :return: root node
        """

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getTreeHeight(root.left), self.getTreeHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rotateRight(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.rotateLeft(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def delete_node(self, root, key):
        """
        recursive function to delete a node from tree
        :param root: the tree root/head node
        :param key: the tree value to be deleted
        :return: root of the modified subtree
        """
        # Step 1 - Perform standard BST delete_node
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)
        if root is None:
            return root

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getTreeHeight(root.left), self.getTreeHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def rotateLeft(self, tree_node):
        """
        left rotates over the node
        :param tree_node: the node to be rotated left
        :return: the new root node after rotation
        """
        node = tree_node.right
        temp_node = node.left
        node.left = tree_node
        tree_node.right = temp_node
        tree_node.height = 1 + max(self.getTreeHeight(tree_node.left), self.getTreeHeight(tree_node.right))
        node.height = 1 + max(self.getTreeHeight(node.left), self.getTreeHeight(node.right))
        return node

    def rotateRight(self, tree_node):
        """
        right rotates over the node
        :param tree_node: the node to be rotated right
        :return: the new root node after rotation
        """
        node = tree_node.left
        temp_node = node.right
        node.right = tree_node
        tree_node.left = temp_node
        tree_node.height = 1 + max(self.getTreeHeight(tree_node.left), self.getTreeHeight(tree_node.right))
        node.height = 1 + max(self.getTreeHeight(node.left), self.getTreeHeight(node.right))
        return node

    @staticmethod
    def getTreeHeight(root):
        """
        calculates and returns tree height.
        :param root: root/head node
        :return: tree height
        """
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        """
        get the balance of the tree
        :param root: root/head node
        :return: height difference
        """
        if not root:
            return 0
        return self.getTreeHeight(root.left) - self.getTreeHeight(root.right)

    def getMinValueNode(self, root):
        """
        finds node with minimum value
        :param root: root/head node
        :return: min value node
        """
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preorderTraversal(self, root):
        """
        displays pre order traversal of tree
        :param root: root/head node
        :return:  nothing
        """
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def inorderTraversal(self, root):
        """
        displays in order traversal
        :param root: root/head node
        :return: nothing
        """
        if not root:
            return
        self.inorderTraversal(root.left)
        print("{0} ".format(root.val), end="")
        self.inorderTraversal(root.right)
