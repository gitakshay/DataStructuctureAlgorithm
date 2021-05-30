class BstNode:

    def __init__(self, key, parent=None, left_child=None, right_child=None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        show = f"KEY : {self.key} "
        if self.parent:
            show += f"  PARENT: {self.parent.key}"
        if self.left_child:
            show += f"  LEFT CHILD: {self.left_child.key}"
        if self.right_child:
            show += f"  RIGHT CHILD: {self.right_child.key}"

        return show

    def next_larger(self):
        """Returns the node with the next larger key (the successor) in the BST.
        """
        if self.right_child is not None:
            return self.right_child.find_min()
        current = self
        # if you are on the right to someone and dont have any children, you
        # will be the largest unless your ancestor were left to someone ,
        # then you can never be bigger then ancestor's parent
        while current.parent is not None and \
                current is current.parent.right_child:
            current = current.parent
        return current.parent

    def find(self, element):
        if self.key == element:
            return self
        elif element > self.key:
            if self.right_child:
                return self.right_child.find(element)
            else:
                return
        else:
            if self.left_child:
                return self.left_child.find(element)
            else:
                return

    def find_max(self):
        if self.right_child:
            return self.right_child.find_max()
        else:
            return self

    def find_min(self):
        if self.left_child:
            return self.left_child.find_min()
        else:
            return self

    def insert(self, node):
        if node.key > self.key:
            if self.right_child:
                self.right_child.insert(node)
            else:
                node.parent = self
                self.right_child = node
        elif node.key < self.key:
            if self.left_child:
                self.left_child.insert(node)
            else:
                node.parent = self
                self.left_child = node
        else:
            raise Exception("Bst Invariance rule violated!!")

    def delete(self):
        """
        if v is a leaf

          delete leaf v

        else if v has 1 child

          bypass v

        else replace v with successor
        """
        if self.left_child is None or self.right_child is None:
            # if self.parent is None:
            #    self = self.left_child or self.right_child
            #    self.parent = None
            #    print(self.key)
            #    return "Deleted root"
            if self is self.parent.left_child:
                self.parent.left_child = self.left_child or self.right_child
                if self.parent.left_child is not None:
                    self.parent.left_child.parent = self.parent
            else:
                self.parent.right_child = self.left_child or self.right_child
                if self.parent.right_child is not None:
                    self.parent.right_child.parent = self.parent
            return self
        else:
            s = self.next_larger()
            s.key, self.key = self.key, s.key
            return s.delete()

    def check_ri(self):

        if self.left_child:
            if self.left_child.key > self.key:
                raise Exception("BST ri violated")
            else:
                self.left_child.check_ri()
        if self.right_child:
            if self.right_child.key < self.key:
                raise Exception("BST ri violated")
            else:
                self.right_child.check_ri()
        else:
            return


class Bst:

    def __init__(self):
        self.root = None

    def insert(self, element):
        node = BstNode(element)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def find(self, element):
        if self.root:
            return self.root.find(element)

    def find_min(self):
        if self.root:
            return self.root.find_min()

    def find_max(self):
        if self.root:
            return self.root.find_max()

    def delete(self, element):
        node = self.find(element)
        if node is None:
            return None
        if node is self.root:
            # This is done to deal with a special case for when the root has
            # only one child. We create a pseudo node and attach the root
            # to its left and attaches pseudo as root's parent.
            # We then delete the root node. But since BST root's is still
            #  pointed at deleted root.
            # For this
            pseudonode = BstNode(0, None, self.root)
            self.root.parent = pseudonode
            deleted = self.root.delete()
            self.root = pseudonode.left_child
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def check_ri(self):
        if self.root:
            self.root.check_ri()
