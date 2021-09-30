

class Node:
    """Used with AVL BST."""
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Adelson-Velsky and Landis Binary Search Tree."""
    def __init__(self, starting_node=None):
        self.root = starting_node
        if starting_node:
            self.root = Node(starting_node)


    def __str__(self) -> str:
        """Return content of BST in human-readable form."""
        values = []
        self._str_helper(self.root, values)
        return "pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, curr, values) -> None:
        """Helper method for __str__."""
        # base case
        if not curr:
            return
        # store value of current node
        values.append(str(curr.value))
        # recursive case for left subtree
        self._str_helper(curr.left, values)
        # recursive case for right subtree
        self._str_helper(curr.right, values)

    def add_node(self, value: int) -> None:
        """Adds a Node to the BST. Time complexity log(n)."""
        new_node = Node(value)
        curr = self.root
        if curr is None:
            self.root = new_node
        else:
            while curr:
                prev = curr
                if curr.value <= value:
                    curr = curr.right
                else:
                    curr = curr.left

            if prev.value <= value:
                prev.right = new_node
            else:
                prev.left = new_node

    def rem_root(self) -> None:
        """Removes the root Node from the BST. Time complexity log(n)."""
        if not self.root:
            return
        # Simple cases without having to traverse the BST.
        leftC = self.root.left
        rightC = self.root.right
        if leftC is None and rightC is not None:
            self.root = rightC
        elif leftC is not None and rightC is None:
            self.root = leftC
        elif leftC is None and rightC is None:
            self.root = None
        # More complex scenario where the left most Node of the right sub-branch
        # of the Root Node becomes the new Root.
        else:
            # S is the successor, N is the current Node.
            S,N = self.root.right, self.root.right
            # Finding the leftmost Node in the right sub branch.
            while N.left:
                S = N
                N = N.left
            # Special case when the root's right child becomes the new root.
            if S == N:
                temp = self.root.left
                self.root = N
                self.root.left = temp
            else:
                S.left = N.right
                temp1 = self.root.right
                temp2 = self.root.left
                self.root = N
                N.right = temp1
                N.left = temp2

    def rem_node(self, val: int) -> None:
        """Removes a Node from the BST. Time complexity log(n)."""
        if not self.root:
            return
        # Calls rem_root() function if the root is being removed.
        elif self.root.value == val:
            self.rem_root()
        else:
            # Finding the Node to remove while keeping track of the parent Node.
            curr = self.root
            while curr:
                if curr.value == val:
                    break
                elif curr.right is None and curr.left is None:
                    return
                elif curr.value <= val:
                    prev = curr
                    curr = curr.right
                else:
                    prev = curr
                    curr = curr.left

            leftC = curr.left
            rightC = curr.right
            cv = curr.value
            pv = prev.value
            # Simple cases without having to traverse the BST.
            if leftC is None and rightC is not None and cv >= pv:
                prev.right = rightC
            elif leftC is None and rightC is not None and cv < pv:
                prev.left = rightC
            elif leftC is not None and rightC is None and cv >= pv:
                prev.right = leftC
            elif leftC is not None and rightC is None and cv < pv:
                prev.left = leftC
            elif leftC is None and rightC is None and cv >= pv:
                prev.right = None
            elif leftC is None and rightC is None and cv < pv:
                prev.left = None
            else:
                # More complex scenario where the left most Node of the right sub-branch
                # of the current Node being removed becomes the replacement Node.
                S, N = curr.right, curr.right
                while N.left:
                    S = N
                    N = N.left

                S.left = N.right
                N.right = curr.right
                N.left = curr.left
                # Checking to see if the replacement Node is going to be the left or
                # right child of the current Node's parent.
                if cv >= pv:
                    prev.right = N
                else:
                    prev.left = N

    def search(self, val: int) -> bool:
        """Searches the BST for the value, returns T/F if it exists. Time Complexity log(n)."""
        curr = self.root
        while curr:
            if curr.value == val:
                return True
            elif curr.value <= val:
                curr = curr.right
            else:
                curr = curr.left

        return False

if __name__ == "__main__":
    tree1 = BST(10)
    print(tree1)
    tree1.add_node(7)
    tree1.add_node(15)
    tree1.add_node(13)
    tree1.add_node(17)
    tree1.add_node(16)
    tree1.add_node(18)
    print(tree1)
    tree1.rem_node(19)
    print(tree1)
