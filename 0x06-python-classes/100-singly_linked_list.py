#!/usr/bin/python3

class Node:
    """Singly-linked list Node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly-linked list class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            holder = self.__head
            while (holder.next_node is not None and
                    holder.next_node.data < value):
                holder = holder.next_node
            new.next_node = holder.next_node
            holder.next_node = new

    def __str__(self):

        values = []
        holder = self.__head

        while holder is not None:
            values.append(str(holder.data))
            holder = holder.next_node

        return ('\n'.join(values))
