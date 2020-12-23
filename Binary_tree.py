class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)  # adding a tree recursively

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)  # adding a tree recursively

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit root
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # visit root
        elements = [self.data]
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        # visit root
        elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True

        # search left part of the tree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        # search the right part of the tree
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete_by_right_min(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_right_min(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_right_min(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_by_right_min(min_val)
        return self

    def delete_by_left_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_left_max(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_left_max(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_by_left_max(max_val)
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete_by_left_max(18)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    # print(numbers_tree.search(34))
    # print(numbers_tree.search(5))
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.calculate_sum())

    food = ["fish", "shrimp", "rice", "spaghetti", "pizza", "eggs", "cheese", "grape"]
    food_tree = build_tree(food)
    print(food_tree.in_order_traversal())

    print("rice is in the list? ", food_tree.search("rice"))
    print("candy is in the list? ", food_tree.search("candy"))
