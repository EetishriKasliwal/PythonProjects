import random
import AVL.AVLTreeImpl as avl

for test in range(10):
    print('Test: ', test+1)
    myTree = avl.AVLTree()
    root = None
    num_list_len = random.randint(5, 20)
    nums = []

    # Insert
    for _ in range(num_list_len):
        num = random.randint(-100, 100)
        nums.append(num)
        root = myTree.insert_node(root, num)

    # Preorder Traversal
    print("Preorder Traversal after insertion -")
    myTree.preorderTraversal(root)
    print()

    # Inorder Traversal
    print("Inorder Traversal after insertion -")
    myTree.inorderTraversal(root)
    print()

    # Delete
    key = random.choice(nums)
    print('key: ', key)
    root = myTree.delete_node(root, key)

    # Preorder Traversal
    print("Preorder Traversal after deletion -")
    myTree.preorderTraversal(root)
    print()

    # Inorder Traversal
    print("Inorder Traversal after insertion -")
    myTree.inorderTraversal(root)
    print()

    print()
