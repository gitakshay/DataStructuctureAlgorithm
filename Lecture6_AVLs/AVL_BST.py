from BST_MY import Bst


def get_height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    #print(f"NODE RECIEVED : {node.key}")
    # if node.left_child:
    #    print(f"NODE LEFT CHILD : {node.left_child.key} NODE LEFT CHILD Height: {node.left_child.height} ")
    # if node.right_child:
    #    print(f"NODE RIGHT CHILD : {node.right_child.key} NODE RIght CHILD Height: {node.right_child.height} ")

    node.height = max(get_height(node.left_child),
                      get_height(node.right_child))+1
    #print("Setting this node height to ",node.height)


class AVL(Bst):
    def right_rotate(self, node):
        y = node.left_child
        y.parent = node.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left_child is node:
                y.parent.left_child = y
            elif y.parent.right_child is node:
                y.parent.right_child = y
        node.left_child = y.right_child
        if node.left_child is not None:
            node.left_child.parent = node

        y.right_child = node
        node.parent = y

        update_height(node)
        update_height(y)

    def left_rotate(self, node):
        y = node.right_child
        y.parent = node.parent

        if node.parent is None:
            self.root = y
        else:
            if node.parent.left_child is node:
                node.parent.left_child = y
            elif node.parent.right_child is node:
                node.parent.right_child = y

        node.right_child = y.left_child
        if node.right_child is not None:
            node.right_child.parent = node

        y.left_child = node
        node.parent = y

        update_height(node)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            print(f"NODE KEY: {node.key} NODE_HEIGHT : {node.height}")
            if get_height(node.left_child) >= 2+get_height(node.right_child):
                if get_height(node.left_child.left_child) >= get_height(node.left_child.right_child):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left_child)
                    self.right_rotate(node)
            elif get_height(node.right_child) >= 2+get_height(node.left_child):
                if get_height(node.right_child.right_child) >= get_height(node.right_child.left_child):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right_child)
                    self.left_rotate(node)

            node = node.parent

    def insert(self, element):
        node = super().insert(element)
        self.rebalance(node)
        return node


if __name__ == "__main__":
    tree = AVL()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    print(tree.root)
