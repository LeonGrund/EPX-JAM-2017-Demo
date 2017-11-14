#import treeOperations

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return (str(self.data))


class Operations:
    def preOrder(root):

        pre = ''
        if (root is None):
            return ''
        elif (root.left is None and root.right is None):
            return str(root.data)

        if (root.left is not None):
            pre += Operations.preOrder(root.left) + ' ' + str(root.data)

        if (root.right is not None):
            pre += ' ' + str(root.data) + ' '+ Operations.preOrder(root.right)
        new_pre = ''
        for i in pre:
            if i in pre.split() and i not in new_pre:
                new_pre += i + ' '
        return new_pre

if __name__ == "__main__":
    test_Tree = Tree(1, None, Tree(2, None, Tree(5, Tree(3, None, Tree(4)), Tree(6, None, None))))
    test_results = Operations.preOrder(test_Tree)
    print(test_results)