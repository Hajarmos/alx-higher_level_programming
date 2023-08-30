#!/usr/bin/python3

"""Define classes for a singly-linked list"""


class Node:
    """class singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class singly-linked list"""

    def __init__(self):
        """Initalize a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted
        position in the list (increasing order)
        Args:
            value (Node): The new Node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """print the entire list in stdout
        one node number by line"""
        vals = ""
        temp = self.__head
        while temp is not None:
            vals = vals + str(temp.data)
            if temp.next_node:
                vals = vals + '\n'
            temp = temp.next_node
        return vals
