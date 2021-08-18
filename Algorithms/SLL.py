
class Node:
    """Used with Single Linked List Class."""
    def __init__(self, value: int) -> None:
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
            out = "SLL: " + str(self.head.value)
            curr = self.head.next
            while curr:
                out += " -> " + str(curr.value)
                curr = curr.next
            return out

    def add_node(self, val: int) -> None:
        """Add a new Node to linked list. θ(n) time complexity."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head.next
            prev = self.head
            while curr:
                prev = curr
                curr = curr.next
            prev.next = new_node

    def rem_node(self, val: int) -> None:
        """Removes a Node from linked list. O(n) time complexity."""
        if not self.head:
            return
        elif self.head.value == val:
            self.head = self.head.next
        else:
            # Need to keep track of prev Node to relink the list after removal if necessary.
            curr = self.head.next
            prev = self.head
            while curr:
                # If Node is not the last Node, break the loop to save time.
                if curr.value == val:
                    prev.next = curr.next
                    return
                prev = curr
                curr = curr.next

    def reverse(self):
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

    def sort(self):
        """Sorts the linked list in ascending order (Bubble Sort). O(n^2) time complexity."""
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



sll = SLL()
sll.add_node(5)
sll.add_node(12)
sll.add_node(11)
sll.add_node(10)
sll.add_node(2)
print(sll)
sll.sort()
print(sll)