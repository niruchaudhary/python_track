# 1. queue use a FIFO
# heapqueue is a remove shortest element and append any element as a index wise
queue = []

queue.append('g')
queue.append('f')
queue.append('h')

print("*************Initial queue****************")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# 2. stack use a (FILO) first in last out

stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('*************Initial stack**************')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# sorting

a = [5, 1, 4, 3]
print("sorted", sorted(a))
print(a)

# Linked List
print("************Linked List********************")


# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.append(6)
    llist.push(7);
    llist.push(1);
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)

    print('Created linked list is: ')
    llist.printList()
    print("\n")


# Linear searching
print("******************Linear search********************")


def search(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    result = search(arr, N, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

# binary search using devide and conqure algorithm

print("****************8Binary search***************************")


def binary_search(list_num, to_search):
    first_index = 0
    size = len(list_num)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2
    mid_element = list_num[mid_index]

    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element != to_search:
                is_found = False
                return " Does not matched in the list"

        elif mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"

        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"


list_container = [16, 18, 20, 50, 60, 81, 84, 89]
print(binary_search(list_container, 81))
print(binary_search(list_container, 10))
