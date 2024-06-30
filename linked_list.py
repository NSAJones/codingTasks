"""This file contains an implementation of a linked list"""

class Node:
    """This class holds a single piece of data for a linked list"""
    def __init__(self,data) -> None:
        self.data = data
        self.next = None



class LinkedList:
    """This class is a list that stores data in nodes"""
    def __init__(self,*items) -> None:
        self.head = None

        for i in items:
            self.append(i)

    def __len__(self) -> int:
        """Returns length of the linked list"""

        count = 1
        node = self.head
        
        # Return zero if there is no head
        if node is None:
            return 0
        else:
            # Count the number of nodes
            while node.next is not None:
                count += 1
                node = node.next
            return count

    def append(self,data) -> None:
        """Adds data to the end of the linked list"""

        # Create new node to append
        new_node = Node(data)

        # Get the first node
        end = self.head

        # Check head exists
        if end is not None:
            while end.next is not None:
                end = end.next
        
            # Add new node to end
            end.next = new_node
        else:
            # Set head to new node
            self.head = new_node
    
    def _get_node(self,index) -> Node:
        """Gets node at an index"""

        # Get first node
        node = self.head

        for _ in range(index):
            # Raise error if the next node is not available
            if node.next is None:
                raise IndexError("Linked list out of range")
            
            # Get next node
            node = node.next
        
        # Return node
        return node
    
    def insert(self, index, data) -> None:
        """Inserts data at given index"""
        
        # Account for inserting at 0 with self.head as None
        if self.head is None and index == 0:
            self.head = Node(data)

        else:
            # Create new node with data and get node behind index
            new_node = Node(data)
            prev_node = self._get_node(index-1)

            # Put the new node in front of the node at index
            new_node.next = prev_node.next
            prev_node.next = new_node


    def __setitem__(self, index, data) -> None:
        """Sets item at given index via python syntax"""

        # Get node at index and set data
        node = self._get_node(index)
        node.data = data


    def __getitem__(self, index) -> any:
        """Gets item at given index via python syntax"""
        
        # Get node at index and return data
        node = self._get_node(index)
        return node.data
    
    def pop(self, index) -> any:
        """Deletes item at given index and returns it's value"""

        # Check node to delete isn't head
        if index == 0:
            # Get data from head, then set the new head
            data = self.head.data
            self.head = self.head.next

            return data
        else:
            # Get node behind node that is being deleted
            prev_node = self._get_node(index-1)

            # Get data of item at index
            data = prev_node.next.data

            # Replace previous node next with the next next
            prev_node.next = prev_node.next.next

            return data
            
    def index(self, item) -> int:
        """Returns index of given item"""

        # Get head
        node = self.head
        index = 0

        # Get next value while node is not none
        while node is not None:
            if node.data is item:
                return index
            
            # Get next value and uptick index
            node = node.next
            index += 1
        
        # Raise error if item not found
        raise ValueError(f"{item} not in linked list")

    def delete(self, item) -> None:
        """Delete a given item"""

        # Get head
        node = self.head

        # Get next value while node is not none
        while node is not None:
            if node.data is item:
                return node
            
            # Get next value
            node = node.next
        
        # Raise error if item not found
        raise ValueError(f"{item} not in linked list")
    
    def __str__(self) -> str:
        """Returns string representation of linked list"""

        str_between = " -> "
        print_str = ""
        node = self.head

        while node is not None:
            print_str += str(node.data)
            print_str += str_between

            node = node.next
        
        # Remove trailing string
        print_str = print_str[:len(str_between)*-1]

        return print_str
    
    def __repr__(self) -> str:
        """Returns string to be used in print"""
        return str(self)
        
        


    
    

if __name__ == "__main__":
    # Test functionality of the linked list
    
    linked = LinkedList(1,2,3,4,5,6,7,8,9)
    print(linked)

    # Set index 4 to 10
    linked[4] = 10
    print("Set index 4 to 10",linked,sep="\n")

    # Remove index 2
    linked.pop(2)
    print("Remove index 2",linked,sep="\n")

    # Insert string into index 1
    linked.insert(1,"foo")
    print("Insert string into index 1",linked,sep="\n")

    # Get length of linked list
    print("Length of linked list is:",len(linked))

    # Get item at index of linked list
    print("Item at index 4 is:",linked[4])

    # Get index of item of linked list
    print("Index of 8 is:",linked.index(8))
