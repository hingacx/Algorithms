
class Node:
    """
    Used with Single Linked List Class.
    Creates a Node with a key:value pair.
    """
    def __init__(self, key: str, value: int) -> None:
        self.key = key
        self.value = value
        self.next = None

class SLL:
    """
    SSL short for Single Linked List.
    A SSL implementation with various methods.
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        """Returns the SLL in human readable form."""
        if self.head is None:
            return "Empty"
        else:
            out = "SLL: " + str(self.head.key) + ": " + str(self.head.value)
            curr = self.head.next
            while curr:
                out += " -> " + str(curr.key) + ": " + str(curr.value)
                curr = curr.next
            return out

    def add_node(self, key: str, val: int) -> None:
        """Add a new Node to linked list. θ(n) time complexity."""
        new_node = Node(key, val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head.next
            prev = self.head
            while curr:
                prev = curr
                curr = curr.next
            prev.next = new_node

    def rem_node(self, key: str) -> None:
        """Removes a Node from linked list. O(n) time complexity."""
        if not self.head:
            return
        elif self.head.key == key:
            self.head = self.head.next
        else:
            # Need to keep track of prev Node to relink the list after removal if necessary.
            curr = self.head.next
            prev = self.head
            while curr:
                # If Node is not the last Node, break the loop to save time.
                if curr.key == key:
                    prev.next = curr.next
                    return
                prev = curr
                curr = curr.next

    def set_value(self, key: str, val: int) -> None:
        """Changes an existing Node's value. O(n) time complexity."""
        if not self.head:
            return
        elif self.head.key == key:
            self.head.value = val
        else:
            curr = self.head.next
            while curr:
                # If Node is not the last Node, break the loop to save time.
                # Updates the Node's value.
                if curr.key == key:
                    curr.value = val
                    return
                curr = curr.next

    def reverse(self) -> None:
        """Reverses the linked list. θ(n) time complexity."""
        # Already reversed by definition.
        if not self.head:
            return
        # Already reversed by definition.
        elif self.head.next is None:
            return
        else:
            curr = self.head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            self.head = prev

    def sort(self) -> None:
        """Sorts the linked list in ascending order by value (Bubble Sort). O(n^2) time complexity."""
        # Already sorted by definition.
        if self.head is None:
            return
        # Already sorted by definition.
        elif self.head.next is None:
            return
        else:
            curr = self.head.next
            prev = self.head
            flag = True
            while flag:
                if prev.value > curr.value:
                    # Call a helper function to swap the Nodes.
                    self.swap_adj(prev, curr)
                    curr = self.head
                    prev = None
                prev = curr
                curr = curr.next
                if curr is None:
                    flag = False

    def swap_adj(self, v: object, u:object) -> None:
        """Swaps adjacent Nodes in the Linked list. O(n) time complexity."""
        # If self.head is being swapped.
        if v == self.head:
            temp = u.next
            u.next = v
            v.next = temp
            self.head = u
            return

        curr = self.head
        prev = None

        while curr:
            if curr == v:
                break
            prev = curr
            curr = curr.next
        temp = u.next
        u.next = v
        v.next = temp
        prev.next = u

    def count(self) -> int:
        """Returns the number of Nodes in the linked list. θ(n) time complexity."""
        # Empty Linked list.
        if not self.head:
            return 0
        else:
            count = 0
            curr = self.head
            while curr:
                count += 1
                curr = curr.next
            return count

    def get_node(self, index: int) -> str:
        """Returns the Node's key at the given index. O(n) time complexity."""
        if 0 > index or index > self.count()-1:
            return "None"
        elif not self.head:
            return "None"
        else:
            curr = self.head
            while index > 0:
                curr = curr.next
                index -= 1
            # Returns the key of the Node at the given index.
            return curr.key

if __name__ == "__main__":
    sll = SLL()
    sll.add_node('a', 5)
    sll.add_node('b', 10)
    sll.add_node('c', 15)
    sll.add_node('d', 6)
    print(sll)
    sll.set_value('g', 11)
    print(sll)

