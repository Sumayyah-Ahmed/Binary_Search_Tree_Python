'''This python’s function demonstrates how to construct and interact with a BST.
It also asks the user to enter a number or type done and gives an option to search for a number.
At the end the program prints the minimum and the maximum number entered by the user. '''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        #Inserts a key into the BST
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if current_node is None:
            return Node(key)
        if key < current_node.key:
            current_node.left = self._insert_recursive(current_node.left, key)
        else:
            current_node.right = self._insert_recursive(current_node.right, key)
        return current_node

    def search(self, key):
        #Searches for a key and returns True or False
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    def in_order_traversal(self):
        #Performs in-order traversal and returns elements in a list
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.key)
            self._in_order_recursive(node.right, result)

    def find_min(self):
        #Finds the minimum value
        if self.root is None:
            return None
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def find_max(self):
        #Finds the maximum value
        if self.root is None:
            return None
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        while node.right is not None:
            node = node.right
        return node.key

# Example
if __name__ == "__main__":
    bst = BinarySearchTree()
    print("Please enter numbers to insert into the BST (type 'done' to finish):")
    while True:
        user_input = input("Please enter a number (or 'done'): ").strip()
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            bst.insert(number)
        except ValueError:
            print("Please enter a valid number.") 

    # Perform in-order traversal
    print("\nIn-order Traversal of the BST:", bst.in_order_traversal())

    # Search for an element
    key_to_search =int(input("\nEnter a number to search in the BST: ")) 
    print(f"\nSearching for {key_to_search}: {bst.search(key_to_search)}")

    # Find the min and max elements
    print("Minimum value in the BST:", bst.find_min())
    print("Maximum value in the BST:", bst.find_max())

